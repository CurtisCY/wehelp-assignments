from flask import Flask, render_template, request, redirect, url_for
from flask import session
import mysql.connector
import os
import json

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

    # mycursor.execute(f"SELECT name, username, password FROM member WHERE username='{usernameInput}' AND password='{passwordInput}'")
    mycursor.execute("SELECT name, username, password FROM member WHERE username=%s AND password=%s",(usernameInput,passwordInput,))
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

    # mycursor.execute(f"SELECT username FROM member WHERE username='{usernameInput}'")
    mycursor.execute("SELECT username FROM member WHERE username=%s",(usernameInput,))
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

@app.route("/api/members")
def querymember():
    usernameInput = request.args.get('username')
    #mycursor.execute(f"SELECT id, name, username FROM member WHERE username='{usernameInput}'")
    mycursor.execute("SELECT id, name, username FROM member WHERE username=%s",(usernameInput,))
    myresult = mycursor.fetchall()

    if len(myresult)!=0:
        userData = list(myresult[0])
        userId = userData[0]
        name = userData[1]
        username = userData[2]

        #responseJsonData = '{"data":{"id":"' + f'{userId}' + '","name":"' + f'{name}' +'","username":"' + f'{username}' + '"}}'
        responseData = {
            "data":{
                "id": userId,
                "name": f'{name}',
                "username": f'{username}',
            }
        }
    elif len(myresult)==0:
        responseData = {
            "data": None
        }

    responseJsonData = json.dumps(responseData)

    print(responseJsonData)
    return responseJsonData

@app.route("/api/member", methods=["POST"])
def updatemember():
     if request.method == 'POST':
        #print(request.get_json())  # parse as JSON
        if "username" in session:
            newNameJson = json.loads(request.get_json())
            newNameDict = dict(newNameJson)
            newName = newNameDict['name']
            print(newName)
            print(session['username'])
            mycursor.execute("UPDATE member SET name=%s WHERE username=%s",(newName, session['username'],))
            # mycursor.execute("SELECT id, name, username FROM member WHERE username=%s",(session['username'],))
            myresult = mycursor.fetchall()
            print(myresult)
            mydb.commit()

            returnMessage = {
                "ok": True
            }
        
            return returnMessage
        elif "username" not in session:
            returnMessage = {
                "error": True
            } 
            return returnMessage



@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

app.run(port=3000)
