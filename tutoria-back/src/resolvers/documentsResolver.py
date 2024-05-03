import os
import shutil

from flask import request
from models.models import Documents
import database.database as db

def get_document_by_id(id):
    Documents.query.get(Documents.id == id)

def get_document_by_owner_id(ownerId):
    return Documents.query.filter(Documents.idCompany == ownerId or Documents.idStudent==ownerId)

#Enregistrer les infos du fichier en base puis l'enregistrer dans un dossier idCompany/fichier
def add_new_document(path, name, companyId=None, studentId=None) :
    doc : Documents
    if companyId!=None or studentId!=None:
        if companyId != None : 
            doc.idCompany = companyId
            path = companyId+"/"+path
        if studentId != None : 
            doc.idStudent = studentId
            path = studentId+"/"+path

        doc.name = name
        doc.path = path
        db.session.add(doc)
        save_doc(name, path)


def save_doc(path, name):

    # Specify the source file path
    #source_file = os.path + '/Documents/' + path

    # Specify the destination directory path
    # destination_directory = os.path + '/Documents/' + path

    # # Copy the file to the destination directory
    # shutil.copy(path, destination_directory)
    pass