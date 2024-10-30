from flask import Flask,render_template
from backend.models import db # trying to connect the app with database
app=None

# @app.route("/")
# def home():
#     return render_template("index.html")


def setup_app():
    app=Flask(__name__)
    #having db file. 
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///ticket_show.sqlite3" #this ticket_show file will be automatically reated in the instance folder
    db.init_app(app) #Flask app connected to db(SQL alchemy)
    app.app_context().push() #direct access to other modules. to avoid the error of working outside of application context
    app.debug=True
    print("Ticket show app is started")

setup_app()

from backend.controller import *    #to take all things from controller. controller used to divide the length of the app file. can splits common routes etc in controller

if __name__=="__main__":
    app.run(debug=True)