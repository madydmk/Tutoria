from flask import Flask, jsonify, request
import json
import os
from flask_cors import CORS
import models as models
from resolvers.schema import schema, Query
from flask_graphql import GraphQLView

app = Flask(__name__)
# Définir le port à utiliser pour le serveur Flask
port = os.environ.get('FLASK_RUN_PORT', 5000)
#app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

CORS(app)
def stringify(student):
    return {
            'id': student.id,
            'name': student.first_name,
    }

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/api/data')
def get_data():
    # Récupérer des données depuis la base de données ou d'autres sources
    data = {"message": "Données provenant du backend Flask"}
    return json.dumps(data)

@app.route("/student/<id>", methods=["GET"])
def student(id):
    student = stringify(Query.get_student_by_id(id))
    #student_data = models.Students(student) 
    # status_code = 200 if success else 400
    return jsonify(student)

@app.route("/students", methods=["GET"])
def students():
    students = models.Students.query.all()
    student_list = []
    
    for student in students:
        student_data = stringify(student)

        student_list.append(student_data)
    return jsonify(student_list)

app.run(port=port)
