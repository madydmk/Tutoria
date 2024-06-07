from flask import session
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import ObjectType, Mutation
from models.models import Students
from models.models import Company as CompanyModel
from queries import studentsQuery, companiesQuery
from queries.studentsQuery import db
import resolvers.documentsResolver as documentsResolver

class StudentObject(SQLAlchemyObjectType):
    class Meta:
        model = Students

class CompanyObject(SQLAlchemyObjectType):
    class Meta:
        model = CompanyModel
    
class CreateStudent(graphene.Mutation):
    class Arguments:
        firstName = graphene.String()
        lastName = graphene.String()
        address = graphene.String()
        cp = graphene.String()
        mail = graphene.String()
        tel = graphene.String()
        schoolId = graphene.Int()
        cfaId = graphene.Int()
        enterpriseId = graphene.Int()
        password = graphene.String()
    student = graphene.Field(lambda: StudentObject)

    def mutate(self, infos, **kwargs):
        print(kwargs)
        new_student = Students(**kwargs)
        db.session.add(new_student)
        db.session.commit()
        return CreateStudent(student=new_student)

class UpdateStudent(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        firstName = graphene.String()
        lastName = graphene.String()
        address = graphene.String()
        cp = graphene.String()
        mail = graphene.String()
        tel = graphene.String()
        schoolId = graphene.Int()
        cfaId = graphene.Int()
        enterpriseId = graphene.Int()
        password = graphene.String()

    student = graphene.Field(lambda: StudentObject)

    def mutate(self, id, **kwargs):
        student = db.session.query(Students).get(id)
        if student:
            for key, value in kwargs.items():
                setattr(student, key, value)
            db.session.commit()
            return UpdateStudent(student=student)
        return None

class CreateCompany(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        address = graphene.String()
        cp = graphene.String()
        tel = graphene.String()
        type = graphene.Int()
        password = graphene.String()

    company = graphene.Field(lambda: CompanyObject)

    def mutate(self, new_company, **kwargs):
        company = CompanyModel(**kwargs)
        print(company)
        db.session.add(company)
        db.session.commit()
        return CreateCompany(company=company)
   
class LogIn(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    success = graphene.Boolean()
    student = graphene.Field(lambda: StudentObject)

    def mutate(self, info, email, password):
        student = Students.query.filter_by(mail=email).first()
        if student and student.password == password:
            session['student_id'] = student.id
            return LogIn(success=True, student=student)
        return LogIn(success=False)

class LogOut(graphene.Mutation):
    success = graphene.Boolean()

    def mutate(self, info):
        if 'student_id' in session:
            session.pop('student_id')
            return LogOut(success=True)
        return LogOut(success=False)

class Mutation(ObjectType):
    update_student = UpdateStudent.Field()
    create_student = CreateStudent.Field()
    create_company = CreateCompany.Field()
    sign_in = LogIn.Field()
    log_out = LogOut.Field()

class Query(ObjectType):
    get_all_students = graphene.List(StudentObject)
    get_all_companies = graphene.List(CompanyObject)
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
