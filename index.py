from flask import Flask, render_template, request

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    X = "作者:羅爾玨<br>"
    X += "<a href=/mis>資管導論</a><br>"
    X += "<a href=/today>日期時間</a><br>"
    X += "<a href=/about>羅爾玨網頁</a><br>"
    X += "<a href=/welcome?guest=羅爾玨>歡迎羅爾玨</a><br>"
    return X

@app.route("/mis")
def course():
    return "<h1>資訊管理導論</h1>"

@app.route("/today")
def today():
    now = datetime.now()
    return render_template("today.html",datetime = str(now))

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/welcome", methods=["GET", "POST"])
def welcome():
    user = request.values.get("guest")
    return render_template("welcome.html", name=user)
@app.route("/account", methods=["GET", "POST"])
def account():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]
        result = "您輸入的帳號是：" + user + "; 密碼為：" + pwd 
        return result
    else:
        return render_template("account.html")



# __name__ == "__main__":
 #   app.run()
