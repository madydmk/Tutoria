from flask import jsonify
from models.models import Students
import models.database as db

def get_student_by_id(student_id):
    student = Students.query.get(student_id)
    return student

def resolve_create_student(info):
    new_student = Students(first_name = info.first_name, last_name = info.last_name, address = info.address, cp = info.cp, mail = info.mail, tel = info.tel, schoolId = info.schoolId, cfaId = info.cfaId, enterpriseId = info.enterpriseId)
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
        'first_name' : student.first_name,
        'last_name' : student.last_name,
        'address' : student.address, 
        'cp' : student.cp,
        'mail' : student.mail,
        'tel' : student.tel,
        'schoolId' : student.schoolId,
        'cfaId' : student.cfaId,
        'enterpriseId' : student.enterpriseId
    }
    return student_string