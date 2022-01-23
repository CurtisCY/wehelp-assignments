from flask import Flask, render_template, request, redirect, url_for
from flask import session

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
        return render_template('member.html')
    return redirect("/")

@app.route("/error")
def error():
    errorMessage = request.args.get("message")
    return render_template("error.html", errorMessage=errorMessage)

@app.route("/signin", methods=["GET","POST"])
def signin():
    account = request.form["Account"]
    password = request.form["Password"]
    if (account == "test" and password == "test"):
        session['username'] = account
        return redirect("/member")
    elif (account == "" or password == ""):
        message = "請輸入帳號、密碼"
        return redirect(url_for("error", message=message))
    else :
        message = "帳號、或密碼輸入錯誤"
        return redirect(url_for("error", message=message))

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

app.run(port=3000)
