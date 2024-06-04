import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import ObjectType, Mutation
from queries.studentsQuery import resolve_create_student, update_student
from models.models import Students as StudentModel, db_session

class Students(SQLAlchemyObjectType):
    class Meta:
        model = StudentModel

class CreateStudent(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        firstName = graphene.String()
        lasName = graphene.String()
        address = graphene.String()
        cp = graphene.String()
        mail = graphene.String()
        tel = graphene.String()
        schoolId = graphene.Int()
        cfaId = graphene.Int()
        enterpriseId = graphene.Int()
    student = graphene.Field(lambda: Students)

    def mutate(self, info, **kwargs):
        student = StudentModel(**kwargs)
        db_session.add(student)
        db_session.commit()
        return CreateStudent(student=student)
    
class UpdateStudent(Mutation):
    class Arguments:
        id = graphene.Int()
        firstName = graphene.String()
        lastName = graphene.String()
        address = graphene.String()
        cp = graphene.String()
        mail = graphene.String()
        tel = graphene.String()
        schoolId = graphene.Int()
        cfaId = graphene.Int()
        enterpriseId = graphene.Int()
    student = graphene.Field(lambda: Students)

    def mutate(self, info, id, **kwargs):
        student = StudentModel.query.get(id)
        if student:
            for key, value in kwargs.items():
                setattr(student, key, value)
            db_session.commit()
            return UpdateStudent(student=student)
        return None

class Mutation(ObjectType):
    update_student = UpdateStudent.Field()
    create_student = CreateStudent.Field()

class Query(ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)