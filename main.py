import os
from flask import Flask, render_template
from flask.ext.restful import Resource, Api
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader
from resource import *
import assets

app = Flask(__name__)
api = Api(app)
api.add_resource(Questionnaire, '/quizmaster/api/questionnaires/<id>')
api.add_resource(QuestionnaireList, '/quizmaster/api/questionnaires/')
assets_env = Environment(app)
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)

@app.route('/quizmaster/')
def serve_index():
    return render_template("index.html")

# main program that launches the app
if __name__ == '__main__':
    default_port = 5001
    host = 'localhost'
    debug = True
    port = int(os.getenv('PORT', default_port))
    if not port == default_port:
        host = '0.0.0.0'
        debug = False

    app.run(host=host, port=port, debug=debug)
