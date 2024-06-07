from flask import jsonify
from models.models import Company
import models.database as db

def get_company_by_id(company_id):
    company = Company.query.get(company_id)
    return company

def get_companies():
    return Company.query.all()

def create_company(infos):
    new_company = Company(infos.id, infos.name, infos.address, infos.cp, infos.tel, infos.type)
    db.session.add(new_company)
    db.session.commit()
    return new_company

# Voir si bonne manière de faire la modif
def update_company(infos):
    company = get_company_by_id(infos.id)
    company.name = infos.name
    company.address = infos.address
    company.cp = infos.cp
    company.tel = infos.tel
    
    db.session.commit()

def delete_company(id): #vérifier structure
    company = get_company_by_id(id)
    db.session.delete(company)

def stringify_company(company):
    company_string = {
        "id" : company.id,
        "name" : company.name,
        "address" : company.address,
        "cp" : company.cp,
        "tel": company.tel,
        "type": company.type
    }
    return company_string