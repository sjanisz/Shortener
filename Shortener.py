from flask import Flask
from flask import render_template
from markupsafe import escape
from peewee import SqliteDatabase

app = Flask(__name__)

@app.route("/")
def index():
    db = SqliteDatabase("shortener.db")
    db.connect()
    return render_template("index.html")

@app.route("/success")
def testRoute():
    return render_template("success.html")

# def testMe(a, b):
#     return a + b