from ..models import Students
import database.database as db

def get_student_by_id(student_id):
    student = Students.query.get(student_id)
    return student

def resolve_create_student(parent, info, name):
    new_student = Students(name=name)
    db.session.add(new_student)
    db.session.commit()
    return new_student