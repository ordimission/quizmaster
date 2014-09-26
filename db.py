from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.quizmaster

def create_all(script_name):
    print "Importing "+script_name

def get_questionnaire(id):
    return db.questionnaires.find_one({"_id":id})	
    #return db.questionnaires.find_one({"_id":ObjectId(str(id))})

def get_questionnaires():
    return list(db.questionnaires.find())


