import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.models import *
from queries import studentsQuery, companiesQuery
import resolvers.documentsResolver as documentsResolver

class StudentObject(SQLAlchemyObjectType):
    class Meta:
        model = Students

class CreateStudent(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        address = graphene.String()
        cp = graphene.String()
        mail = graphene.String()
        tel = graphene.String()
        schoolId = graphene.Int()
        cfaId = graphene.Int()
        enterpriseId = graphene.Int()

    student = graphene.Field(StudentObject)

    def mutate(self, info, **kwargs):
        student = studentsQuery.resolve_create_student(info, **kwargs)
        return CreateStudent(student=student)
    
class UpdateStudent(graphene.Mutation):
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

    student = graphene.Field(StudentObject)

    def mutate(self, info, id, **kwargs):
        student = studentsQuery.update_student(info, id, **kwargs)
        if student:
            return UpdateStudent(student=student)
        else:
            return None

# Company
class CompanyObject(SQLAlchemyObjectType):
    class Meta:
        model = Company

class AddCompany(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        industry = graphene.String()
        adress = graphene.String()
        cp = graphene.String()
        tel = graphene.String()
        type = graphene.Int()
    company = graphene.Field(CompanyObject)

    def mutate(self, info, **kwargs):
        student = companiesQuery.create_company(info, **kwargs)
        return AddCompany(student=student)
    
class UpdateCompany(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        industry = graphene.String()
        adress = graphene.String()
        cp = graphene.String()
        tel = graphene.String()
        type = graphene.Int()

    company = graphene.Field(CompanyObject)

    def mutate(self, company, id, **kwargs):
        student = studentsQuery.update_student(company, id, **kwargs)
        if student:
            return UpdateCompany(company=company)
        else:
            return None

class Mutation(graphene.ObjectType):
    update_student = UpdateStudent.Field()
    create_student = CreateStudent.Field()
    #create_company, update_company, delete_company
    # same for certifs, courses and docs

class Query(graphene.ObjectType):
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
