from flask import Flask,render_template,request
from backend.models import *
from flask import current_app as app #to get the app which we defined in the main folder

@app.route("/")
def home():
    return render_template("index.html")



@app.route("/login",methods=["GET","POST"])
def signin():
    error_message = None  # Initialize error message
    if request.method=="POST":
        uname=request.form.get("user_name")
        pwd=request.form.get("password")
        usr=User_info.query.filter_by(email=uname,password=pwd).first()
        if usr and usr.role==0: #user is exist and is admin
            return render_template("admin_dashboard.html")
        elif usr and usr.role==1:
            return render_template("user_dashboard.html")
        else:
            return render_template("login.html",msg="Invalid user credentials.Please enter a valid user details!!")
    return render_template("login.html",msg="",msg2="") #signup page is directing to login


#for the signup page
@app.route("/register",methods=["GET","POST"])
def signup():
    if request.method=="POST":
        uname=request.form.get("user_name")
        pwd=request.form.get("password")
        name=request.form.get("full_name")
        lcn=request.form.get("location")
        pinc=request.form.get("pin_code")
        user=User_info.query.filter_by(email=uname).first()
        if user:
            return render_template("signup.html", show_popup_wrong=True, msg="User already exist !!!")
        new_user=User_info(email=uname,password=pwd,full_name=name,address=lcn,pin_code=pinc)
        db.session.add(new_user)
        db.session.commit()
        return render_template("signup.html", show_popup=True, msg="Registration successful!")

    return render_template("signup.html", show_popup=False)




# @app.route('/login_page')
# def login():
#     return render_template("user_dashboard.html")