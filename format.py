from flask.ext.restful import fields

class Answer(fields.Raw):
    def format(self, value):
        return True if value == "true" else False

# data structure for choices
choice_format = {
    'label': fields.String,
    'answer': Answer
}

# data structure for questions
question_format = {
    'number': fields.String,
    'label': fields.String,
    'explanation': fields.String,
    'choices': fields.Nested(choice_format),
}


# data structure for questionnaires
questionnaire_format = {
    '_id': fields.String,
    'name': fields.String,
    'questions': fields.Nested(question_format),
}


# flat data structure for questionnaires
questionnaire_flat_format = {
    '_id': fields.String,
    'name': fields.String
}
