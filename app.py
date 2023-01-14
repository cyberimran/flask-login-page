from flask import Flask,request
from flask import render_template
d={"email":"contact.imrancoding@gmail.com","pass":"Imran@37"}
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        user_email=request.form["email"]
        user_pass=request.form["Pass"]
        if user_email==d["email"] and user_pass==d["pass"]:
            return render_template("dashboard.html")
        else:
            return render_template("wrong.html")
    return render_template('index.html')
app.run(port="7777")