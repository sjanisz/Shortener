from flask import render_template
from markupsafe import escape
from app import app
from models import *

@app.route("/")
def index():
    db = SqliteDatabase("shortener.db")
    db.connect()
    return render_template("index.html")

@app.route("/success")
def testRoute():
    return render_template("success.html")
