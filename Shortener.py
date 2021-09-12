from app import app, db
from models import *
from views import *

def create_tables():
    db.create_tables([Verb, Adjective, Noun, Map], safe=True) 

if __name__ == '__main__':
    db.connect()
    create_tables()
    PopulateTablesWithDummyData()
    
    app.run(debug=True)