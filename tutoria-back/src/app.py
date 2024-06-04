from flask import Flask, jsonify, request
import os
from flask_cors import CORS
from flask_graphql import GraphQLView
from resolvers.schema import schema 
from queries import studentsQuery, companiesQuery

app = Flask(__name__)
CORS(app)

# Configurer le endpoint GraphQL
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # Permet d'utiliser l'interface GraphiQL
    )
)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route("/student/<id>", methods=["GET"])
def student(id):
    json_student = studentsQuery.stringify_student(schema.Query.resolve_get_student_by_id(schema.Query, id))
    return json_student

@app.route("/students", methods=["GET"])
def students():
    students = schema.Query.resolve_get_all_students(schema.Query) #models.Students.query.all()
    student_list = []
    
    for student in students:
        student_list.append(studentsQuery.stringify_student(student))
    return jsonify(student_list)

@app.route("/company/<id>", methods=["GET"])
def get_company_by_id(id):
    company = schema.Query.resolve_get_company_by_id(schema.Query, id)
    return companiesQuery.stringify_company(company=company)

@app.route("/company/<id>/students", methods=["GET"])
def get_company_students(id):
    #get company by id, get student by id company
    students = studentsQuery.get_students_by_company(None, companyId=id)
    student_list = []
    
    for student in students:
        student_data = studentsQuery.stringify_student(student)
        student_list.append(student_data)

    return student_list

@app.route("/new_company", methods=["POST"])
def add_company():
    new_company = request.form['new_company']
    schema.AddCompany(new_company)

@app.route("/new_student", methods=["POST"])
def add_student():
    new_student = request.form['new_student']
    schema.CreateStudent(new_student)

if __name__ == '__main__':
    port = os.environ.get('FLASK_RUN_PORT', 5000)
    app.run(port=port)
