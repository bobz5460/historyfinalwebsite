from flask import render_template, url_for, redirect, flash, request
from app import app
@app.route("/")
def home():
    return
@app.route("/main")
def main():
    return render_template("main.html")