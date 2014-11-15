from tinydb import TinyDB, where

db = TinyDB('db/tinydb.json')

def create_all(script_name):
    print "Importing "+script_name

def get_questionnaire(id):
    return db.search(where('_id')==id)


def get_questionnaires():
    return list(db.all())


