import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Students, Company  # Importer les modèles SQLAlchemy
import database.database as db

class StudentObject(SQLAlchemyObjectType):
    class Meta:
        model = Students


class Query(graphene.ObjectType):
    all_students = graphene.List(StudentObject)

    def resolve_all_students(self, info):
        return Students.query.all()

    def get_student_by_id(student_id):
        student = Students.query.get(student_id)
        return student
    
    def create_student(parent, info, name):
        new_student = Students(name=name)
        db.session.add(new_student)
        db.session.commit()
        return new_student
    
    def create_student(parent, info, name):
        new_student = Students(name=name)
        db.session.add(new_student)
        db.session.commit()
        return new_student
    
schema = graphene.Schema(query=Query)
