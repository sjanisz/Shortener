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

# Returns link
def AddNewLinkMapToDatabase(link):
    # TODO: validate if link is valid (ping?)

    # result = Map.select().where(Map.destination_address == link)
    # no need to handle existing links because it should not be unique

    # get random Verb + Adjective + Noun
    # TODO: avoid duplicates (query db agains above set)
    verb = Verb.select().order_by(fn.Random()).get()
    adjective = Adjective.select().order_by(fn.Random()).get()
    noun = Noun.select().order_by(fn.Random()).get()

    createdMap = Map.create(destination_address=link, verb=verb, adjective=adjective, noun=noun)

    # TODO: change way of receiving host address (including port)
    return f"localhost:5000/{createdMap.verb.name}{createdMap.adjective.name}{createdMap.noun.name}"