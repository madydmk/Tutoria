import sys
sys.dont_write_bytecode = True
from flask import Flask, jsonify, request, session
import os
from flask_cors import CORS, cross_origin
from flask_graphql import GraphQLView
from resolvers import schema 
from queries import studentsQuery, companiesQuery
from models.models import Students
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv('SECRET_KEY')

# Configurer le endpoint GraphQL
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema.schema,
        graphiql=True  # Permet d'utiliser l'interface GraphiQL
    )
)

@app.route('/')
def index():
    return 'Hello, World!'
# Connexion
@app.route("/logIn", methods=["POST"])
def sign_in():
    if not request.content_type.__contains__('application/json'):
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    input_data = request.get_json()
    
    mutation = '''
        mutation LogIn($email: String!, $password: String!) {
            sign_in(email: $email, password: $password) {
                success
                student {
                    id
                    firstName
                    lastName
                    mail
                }
            }
        }
    '''

    result = schema.execute(
        mutation,
        variable_values={
            'email': input_data.get('email'),
            'password': input_data.get('password')
        }
    )

    if result.errors:
        return jsonify({'errors': [str(error) for error in result.errors]}), 400

    if result.data['sign_in']['success']:
        return jsonify(result.data['sign_in']['student']), 200
    else:
        return jsonify({'error': 'Invalid credentials'}), 401
    
@app.route("/logOut", methods=["POST"])
def log_out():
    if 'student_id' in session:
        session.pop('student_id')
        return jsonify({'success': True}), 200
    return jsonify({'error': 'User not logged in'}), 401

@app.route('/signIn1', methods=["POST"])
def connect():
    user_name = request.form['name']
    pwd = request.form['password']
    if pwd != '' and pwd:
        pwd = (pwd.strip != '', pwd, '')
    
    #auth
    data = {"message": "Données provenant du backend Flask"}
    return jsonify(data)

# Deconnexion
@app.route('/signOut')
@cross_origin(origin='*', headers=['Content-type', 'Authorization'])
def signeOut():
    data = {"message": "Données provenant du backend Flask"}
    return jsonify(data)

@app.route("/student/<id>", methods=["GET"])
@cross_origin(origin='*', headers=['Content-type', 'Authorization'])
def student(id):
    json_student = studentsQuery.stringify_student(schema.Query.resolve_get_student_by_id(schema.Query, id))
    return json_student

@app.route("/students", methods=["GET"])
@cross_origin(origin='*', headers=['Content-type', 'Authorization'])
def students():
    students = schema.Query.resolve_get_all_students(schema.Query) #models.Students.query.all()
    student_list = []
    
    for student in students:
        student_list.append(studentsQuery.stringify_student(student))
    return jsonify(student_list)

@app.route("/companies", methods=["GET"])
@cross_origin(origin='*', headers=['Content-type', 'Authorization'])
def companies():
    companies = schema.Query.resolve_get_all_companies(schema.Query)
    companies_list = [companiesQuery.stringify_company(company) for company in companies]
    return jsonify(companies_list)

@app.route("/company/<id>", methods=["GET"])
@cross_origin(origin='*', headers=['Content-type', 'Authorization'])
def get_company_by_id(id):
    company = schema.Query.resolve_get_company_by_id(schema.Query, id)
    return companiesQuery.stringify_company(company=company)

@app.route("/company/<id>/students", methods=["GET"])
@cross_origin(origin='*', headers=['Content-type', 'Authorization'])
def get_company_students(id):
    #get company by id, get student by id company
    students = studentsQuery.get_students_by_company(None, companyId=id)
    student_list = []
    
    for student in students:
        student_data = studentsQuery.stringify_student(student)
        student_list.append(student_data)

    return student_list

@app.route("/new_company", methods=["POST"])
@cross_origin(origin='*', headers=['Content-type', 'Authorization'])
def add_company():
    new_company = request.form['new_company']
    print(request)
    schema.CreateCompany(new_company)

@app.route("/new_student", methods=["POST"])
@cross_origin(origin='*', headers=['Content-type', 'Authorization'])
def add_student():
    if request.content_type.__contains__('application/json'):
        input_data = request.get_json()
        new_student = studentsQuery.jsonToStudent(input_data)
        result = studentsQuery.resolve_create_student(new_student)

        if result is None:
            return jsonify({'errors': ["Impossible de créer cet utilisateur"]}), 400
        return jsonify(studentsQuery.stringify_student(result)), 200
    else:
        return jsonify({'errors': [str(error) for error in result.errors]}), 415

if __name__ == '__main__':
    port = os.environ.get('FLASK_RUN_PORT', 5000)
    app.run(port=port)