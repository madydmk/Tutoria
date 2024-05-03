import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import ObjectType, Mutation
from queries.studentsQuery import *
from models.models import Students as StudentModel

class Students(SQLAlchemyObjectType):
    class Meta:
        model = StudentModel

class CreateStudent(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        address = graphene.String()
        cp = graphene.String()
        mail = graphene.String()
        tel = graphene.String()
        schoolId = graphene.Int()
        cfaId = graphene.Int()
        enterpriseId = graphene.Int()
    student = graphene.Field(StudentModel)

    def mutate(self, info, new_student):
        student = resolve_create_student(None, info, new_student)
        return CreateStudent(student=student)
    
class UpdateStudent(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        first_name = graphene.String()
        last_name = graphene.String()
        address = graphene.String()
        cp = graphene.String()
        mail = graphene.String()
        tel = graphene.String()
        schoolId = graphene.Int()
        cfaId = graphene.Int()
        enterpriseId = graphene.Int()
    student = graphene.Field(StudentModel)

    def mutate(self, info, **kwargs):
        student = update_student(None, info, **kwargs)
        if student:
            return UpdateStudent(student=student)
        else:
            return None

class Mutation(ObjectType):
    update_student = UpdateStudent.Field()
    create_student = CreateStudent.Field()
    #create_company, update_company, delete_company
    # same for certifs, courses and docs

class Query(graphene.ObjectType):
    # requêtes
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)
