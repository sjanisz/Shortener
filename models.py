from peewee import *
from app import db
from DatabaseInitializationData import *

class Verb(Model):
    name = CharField(unique=True)

    class Meta:
        database = db

class Adjective(Model):
    name = CharField(unique=True)

    class Meta:
        database = db

class Noun(Model):
    name = CharField(unique=True)

    class Meta:
        database = db

class Map(Model):
    destination_address = CharField()
    verb = ForeignKeyField(Verb)
    adjective = ForeignKeyField(Adjective)
    noun = ForeignKeyField(Noun)

    class Meta:
        database = db

def PopulateTablesWithDummyData():
    _populateVerbTableWithDummyData()
    _populateAdjectiveTableWithDummyData()
    _populateNounTableWithDummyData()

def _populateVerbTableWithDummyData():
    if(Verb.select().count() == 0):
        for verb in VerbInitData:
            Verb(name=verb).save()

def _populateAdjectiveTableWithDummyData():
    if(Adjective.select().count() == 0):
        for adjective in AdjectiveInitData:
            Adjective(name=adjective).save()

def _populateNounTableWithDummyData():
    if(Noun.select().count() == 0):
        for noun in NounInitData:
            Noun(name=noun).save()