# Flask looks for files called app so this is what we have named our file
from flask import Flask, jsonify, redirect, url_for, render_template


# Create an instance of our app
app = Flask(__name__)


# using a decorator to create our api/url for the user to access our data in the browser
@app.route("/login/")  # localhost:5000 is default port for Flask
# This function runs when the URL/API is accessed
def login():
    return render_template("login.html")


# using a decorator to create our api/url for the user to access our data in the browser
@app.route("/")
# This function runs when the URL/API is accessed
def profile():
    return render_template("profile.html")


# using a decorator to create our api/url for the user to access our data in the browser
@app.route("/edit_profile/")
# This function runs when the URL/API is accessed
def edit_profile_fail():
    return render_template("edit_profile.html")


# # using a decorator to create our api/url for the user to access our data in the browser
# @app.route("/edit_profile/?username=<username>&password=<password>/")
# # This function runs when the URL/API is accessed
# def edit_profile():
#     return render_template("edit_profile.html")

