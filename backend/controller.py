from flask import Flask,render_template,request
from flask import current_app as app #to get the app which we defined in the main folder

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/login',methods=["GET","POST"])
def signin():
    if request.method=="POST":
        uname=request.form.get('user_name')
        pwd=request.form.get('password')
    return render_template("login.html") #signup page is directing to login

@app.route('/register')
def signup():
    return render_template("signup.html") #login is directing to signup

# @app.route('/login_page')
# def login():
#     return render_template("user_dashboard.html")