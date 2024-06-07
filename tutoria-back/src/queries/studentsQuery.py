from flask import jsonify
from models.models import Students
import models.database as db

def get_student_by_id(student_id):
    student = Students.query.get(student_id)
    return student

def resolve_create_student(new_student):
    print("Name: ", new_student.firstName)
    # new_student = Students(firstName = info["firstName"], lastName = info["lastName"], address = info["address"], cp = info["cp"], mail = info["mail"], tel = info["tel"], schoolId = info["schoolId"], cfaId = info["cfaId"], enterpriseId = info["enterpriseId"], password = info["password"])
    db.session.add(new_student)
    db.session.commit()
    return new_student

def get_all_students():
    return Students.query.all()

def get_student_by_id(student_id):
    student = Students.query.get(student_id)
    return student

def update_student(parent, info, id, **kwargs): #mettre updated_student à la place de kwargs
    student = Students.query.get(id)

    if student:
        for key, value in kwargs.items():
            if hasattr(student, key):
               setattr(student, key, value)
        db.session.commit()
        return student
    else:
        return None

def get_students_by_company(parent, companyId):
    students = Students.query.filter(Students.enterpriseId==companyId, Students.schoolId==companyId, Students.cfaId==companyId)
    return students

def stringify_student(student):
    student_string = {
        'id': student.id,
        'firstName' : student.firstName,
        'lastName' : student.lastName,
        'address' : student.address, 
        'cp' : student.cp,
        'mail' : student.mail,
        'tel' : student.tel,
        'schoolId' : student.schoolId,
        'cfaId' : student.cfaId,
        'enterpriseId' : student.enterpriseId,
        'password' : student.password
    }
    return student_string

def jsonToStudent(info):
    address = info["address"] if "address" in info.keys() else "null"
    cp = info["cp"] if "cp" in info.keys() else "null"
    mail = info["mail"] if "mail" in info.keys() else"null"
    tel = info["tel"] if "tel" in info.keys() else None
    schoolId = info["schoolId"] if "schoolId" in info.keys() else "-1"
    cfaId = info["cfaId"] if "cfaId" in info.keys() else "-1"
    enterpriseId = info["enterpriseId"] if "enterpriseId" in info.keys() else "null"
    password = info["password"] if info["password"] != None else "null"

    return Students(firstName = info["firstName"], lastName = info["lastName"], address = address, cp = cp, mail = mail, tel = tel, schoolId = schoolId, cfaId = cfaId, enterpriseId = enterpriseId, password = password)
