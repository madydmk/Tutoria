from models.models import Certifications
import models.database as db

def get_certifications():
    Certifications.query.all()

def get_certification_by_id(id):
    if type(id) == int :
        Certifications.query.get(id)

def add_obtained_certification(certif):
    if certif.id != None and certif.score != None:
        db.session.add(certif)
        db.session.commit()
        return True
    return False

# On ne devrait pas pouvoir modifier une certif obtenue!
def update_certification(id, certification:Certifications):
    if(type(id) == int and id != None):
        certif = Certifications.query.get(id)
        certif.idCompany = certification.idCompany
        certif.name = certification.name
        certif.score = certification.score
        db.session.commit()
        return True
    return False

def delete_certification(id):
    if type(id) == int and id != None:
        db.session.delete(id)
        db.session.commit()
        return True
    return False