from graphene import ObjectType, String, Int, List
from graphene_sqlalchemy import SQLAlchemyObjectType
from models.models import Company as CompanyModel

class Company(SQLAlchemyObjectType):
    class Meta:
        model = CompanyModel
        exclude_fields = ('id',)  # Exclude id field from GraphQL schema

class Query(ObjectType):
    companies = List(Company)

    def resolve_companies(self, info):
        # Resolve and return all companies
        return CompanyModel.query.all()
    
    def companyById(self, id):
        return CompanyModel.query.id == id
