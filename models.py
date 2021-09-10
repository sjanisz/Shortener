from peewee import *
from app import db

class Verb(Model):
    verb = CharField()

class Adjective(Model):
    adjective = CharField()

class Noun(Model):
    noun = CharField()

class Map(Model):
    destination_address = CharField()
    verb = ForeignKeyField(Verb)
    adjective = ForeignKeyField(Adjective)
    noun = ForeignKeyField(Noun)