from tinydb import TinyDB, where
import json

db = TinyDB('db/tinydb.json')


def create_all(script_name):
    print "Importing "+script_name
    json_questionnaires=open(script_name).read()
    questionnaires = json.loads(json_questionnaires)
    for questionnaire in questionnaires:
        db.insert(questionnaire)



def get_questionnaire(id):
    questionnaires_matching_id = db.search(where('_id')==id)
    return questionnaires_matching_id[0]


def get_questionnaires():
    return list(db.all())


if __name__ == '__main__':
    create_all('db/questionnaires.json')

