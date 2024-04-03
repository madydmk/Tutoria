from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
import src.database.models as models
import src.database.database as datab

app = Flask(__name__)
# Définir le port à utiliser pour le serveur Flask
port = os.environ.get('FLASK_RUN_PORT', 5000)

CORS(app)

datab

@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/api/data')
def get_data():
    # Récupérer des données depuis la base de données ou d'autres sources
    data = {"message": "Données provenant du backend Flask"}
    return jsonify(data)

@app.route("/student", methods=["POST"])
def student(id):
    student = models.Students.query.id == id
    student_data = {
            'id': student.id,
            'name': student.name,
        }
    # status_code = 200 if success else 400
    return jsonify(student_data)

@app.route("/students", methods=["GET"])
def students():
    students = models.Students.query.all()
    student_list = []
    for student in students:
        student_data = {
            'id': student.id,
            'name': student.name,
        }
        student_list.append(student_data)
    return jsonify(student_list)

app.run(port=port)