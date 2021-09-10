from flask import Flask
from peewee import *

app = Flask(__name__)

db = SqliteDatabase("shortener.db")