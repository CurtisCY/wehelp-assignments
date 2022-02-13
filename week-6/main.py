from flask import Flask, render_template, request, redirect, url_for
from flask import session
import mysql.connector
import os

#Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user=os.getenv('SQLUSER'), #Read username/password from environment variable
  password=os.getenv('SQLPASSWORD'),
  database="week6"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM member")
# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/",
)

app.secret_key = "12345"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/member")
def member():
    if "username" in session:
        loginUsername = request.args.get("name")
        if loginUsername == None:
            loginUsername = session['name']
            # print(session['name'])
        return render_template('member.html', name = loginUsername )
    return redirect("/")

@app.route("/error")
def error():
    errorMessage = request.args.get("message")
    return render_template("error.html", errorMessage=errorMessage)

@app.route("/signin", methods=["GET","POST"])
def signin():
    usernameInput = request.form["username"]
    passwordInput = request.form["password"]

    mycursor.execute(f"SELECT name, username, password FROM member WHERE username='{usernameInput}' AND password='{passwordInput}'")
    myresult = mycursor.fetchall()

    

    if len(myresult)==0:
            message = "帳號、或密碼輸入錯誤"
            return redirect(url_for("error", message=message))
  
    elif len(myresult) !=0:
            session['username'] = usernameInput
            #print(session['username'])
            myresultList = list(myresult[0])
            name = myresultList[0]
            session['name'] = name
            return redirect(url_for("member", name = name))


@app.route("/signup", methods=["GET","POST"])
def signup():
    nameInput = request.form["name"]
    usernameInput = request.form["username"]
    passwordInput = request.form["password"]

    mycursor.execute(f"SELECT username FROM member WHERE username='{usernameInput}'")
    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        sql = "INSERT INTO member (name, username, password) VALUES (%s, %s, %s)"
        val = (nameInput, usernameInput, passwordInput)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
        return redirect("/")
    elif len(myresult) != 0:
        message = "帳號已經被註冊"
        return redirect(url_for("error", message=message))

    

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

app.run(port=3000)
