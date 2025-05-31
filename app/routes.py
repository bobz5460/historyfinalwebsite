from flask import render_template, url_for, redirect, flash, request
from app import app

@app.route("/")
def home():
    return redirect(url_for('main'))

@app.route("/main")
def main():
    # List of assets needed for the moon landing page
    # These could be checked/created if not existing
    required_assets = [
        'earth.png',
        'lunar-module.png',
        'astronaut.png',
        'american-flag.png',
        'earth-from-moon.png'
    ]

    return render_template("main.html")