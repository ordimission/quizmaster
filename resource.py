import mongo_db
import tiny_db
import util
from flask.ext.restful import Resource, marshal_with, reqparse 
from format import *

db = eval('tiny_db')

# Questionnaire resource management

class Questionnaire(Resource):
	@marshal_with(questionnaire_format)
	def get(self,id):
		questionnaire = db.get_questionnaire(id)
		self.req_parser = reqparse.RequestParser()
		self.req_parser.add_argument('shuffle', default=0, type=int, required=False)
		self.req_parser.add_argument('size', default=len(questionnaire['questions']), type=int, required=False)
		self.args = self.req_parser.parse_args()
		if not self.args['shuffle'] == 0:
			ordered_questions = questionnaire['questions'];
			quizz_questions = util.shuffle(ordered_questions, self.args['size'] )
			questionnaire['questions'] = quizz_questions
		return questionnaire

# QuestionnaireList global resource management
class QuestionnaireList(Resource):
	@marshal_with(questionnaire_flat_format)
	def get(self):
		return db.get_questionnaires()
