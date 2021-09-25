from flask import render_template
from flask import request
from markupsafe import escape
from app import app
from models import *

@app.route("/")
def indexRoute():
    return render_template("index.html")

@app.route("/shorten", methods=["POST"])
def shortenRoute():
    if request.method == "POST":
        linkToShorten = request.form["linkToShort"]
        createdLink = AddNewLinkMapToDatabase(linkToShorten)
        return render_template("success.html", shortenedLink = createdLink)
        # return createdLink
    else:
        # TODO: return render_template('login.html', error="wrong method")
        pass

#TODO: fix switching to success page
@app.route("/success")
def successRoute():
    return render_template("success.html")