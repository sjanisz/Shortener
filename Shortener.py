from app import app
from models import *
from views import *

def create_tables():
    db.database.create_tables([User], safe=True)

if __name__ == '__main__':
    app.run(debug=True)