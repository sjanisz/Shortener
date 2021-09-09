from flask import Flask
from flask import request
from peewee import SqliteDatabase


@app.route("/shorten/<linkToShorten>", methods = ["POST"])
def shorten():
    pass