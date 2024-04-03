import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import Students, Company  # Importer les modèles SQLAlchemy

class StudentObject(SQLAlchemyObjectType):
    class Meta:
        model = Students

class CompanyObject(SQLAlchemyObjectType):
    class Meta:
        model = Company

class Query(graphene.ObjectType):
    all_students = graphene.List(StudentObject)
    all_companies = graphene.List(CompanyObject)

    def resolve_all_students(self, info):
        return Students.query.all()

    def resolve_all_companies(self, info):
        return Company.query.all()

schema = graphene.Schema(query=Query)
