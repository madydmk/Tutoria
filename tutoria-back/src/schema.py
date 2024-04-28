import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from queries.studentsQuery import resolve_create_student
from models import Students as StudentModel

class Students(SQLAlchemyObjectType):
    class Meta:
        model = StudentModel

class CreateStudent(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    student = graphene.Field(Students)

    def mutate(self, info, name):
        student = resolve_create_student(None, info, name)
        return CreateStudent(student=student)

class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()

class Query(graphene.ObjectType):
    # Définissez vos requêtes ici
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)
