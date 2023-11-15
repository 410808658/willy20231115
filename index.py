import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


from flask import Flask, render_template, request

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    X = "企管四B 410808658 羅爾玨的求職相關資訊<br>"
    X += "<a href=/me>我的個人簡介</a><br>"
    X += "<a href=/mis>MIS相關工作介紹</a><br>"
    X += "<a href=/quiz>職涯測驗結果</a><br>"
    return X

@app.route("/me")
def me():
    return render_template("about2.html")


@app.route("/mis")
def mis():
    return render_template("aboutwork.html")

@app.route("/quiz")
def quiz():
    return render_template("ucan.html")





# __name__ == "__main__":
 #   app.run()
