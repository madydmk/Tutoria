import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import ObjectType, Mutation
from models.models import Students as StudentModel, db_session
from queries import studentsQuery, companiesQuery
import resolvers.documentsResolver as documentsResolver

class StudentObject(SQLAlchemyObjectType):
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
    student = graphene.Field(lambda: StudentObject)

    def mutate(self, info, **kwargs):
        student = StudentModel(**kwargs)
        db_session.add(student)
        db_session.commit()
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
    student = graphene.Field(lambda: StudentObject)

    def mutate(self, info, id, **kwargs):
        student = db_session.query(StudentModel).get(id)
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
    get_all_students = graphene.List(StudentObject)

        #Students
    def resolve_get_all_students(self):
        return studentsQuery.get_all_students()

    def resolve_get_student_by_id(self, student_id):
        return studentsQuery.get_student_by_id(student_id)

    def resolve_students_by_company_id(self, info, companyId):
        students = studentsQuery.get_students_by_company(companyId)
        return students

    #Campany
    def resolve_get_company_by_id(self, id):
        if id != None:
            return companiesQuery.get_company_by_id(id)
        return None

    def resolve_get_all_companies(self):
        return companiesQuery.get_companies()

    #Certifs
    def resolve_get_certif_by_student_id(self, studentId):
        pass

    def resolve_get_certif_by_company_id(self, companyId):
        pass

    # Courses

    # Documents
    def resolve_get_document_by_id(self, id):
        if id != None:
            return documentsResolver.get_document_by_id(id)
        return None

    def resolve_get_document_by_owner_id(self, ownerId):
        if ownerId != None : 
            return documentsResolver.get_document_by_owner_id(ownerId)
        return None

    def resolve_get_document_by_courseId(self, courseId):
        pass

schema = graphene.Schema(query=Query, mutation=Mutation)
