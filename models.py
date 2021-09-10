from peewee import *
from app import db

class Verb(Model):
    verb = CharField()

    class Meta:
        database = db

class Adjective(Model):
    adjective = CharField()

    class Meta:
        database = db

class Noun(Model):
    noun = CharField()

    class Meta:
        database = db

class Map(Model):
    destination_address = CharField()
    verb = ForeignKeyField(Verb)
    adjective = ForeignKeyField(Adjective)
    noun = ForeignKeyField(Noun)

    class Meta:
        database = db