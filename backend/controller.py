from flask import Flask,render_template
from flask import current_app as app #to get the app which we defined in the main folder

@app.route("/")
def home():
    return render_template("index.html")