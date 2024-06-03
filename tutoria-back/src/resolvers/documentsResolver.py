# import os
# from flask_uploads import UploadSet, configure_uploads, IMAGES
# from flask import app, request
# from models.models import Documents
# import database.database as db

# uploads = UploadSet('uploads', IMAGES)
# app.config['UPLOADED_UPLOADS_DEST'] = 'src/files'
# configure_uploads(app, uploads)

# def get_document_by_id(id):
#     Documents.query.get(Documents.id == id)

# def get_document_by_owner_id(ownerId):
#     return Documents.query.filter(Documents.idCompany == ownerId or Documents.idStudent==ownerId)

# #Enregistrer les infos du fichier en base puis l'enregistrer dans un dossier idCompany/fichier
# def add_new_document(file, companyId=None, studentId=None) :
#     if file.filename == '':
#         return {'error': 'No selected file'}
    
#     if file:
#         # filename = uploads.save(file)
#         # document = Documents(name=file.filename, path=filename, idCompany=companyId, idStudent=studentId)
#         # db.session.add(document)
#         # db.session.commit()
#         return {'success': 'File uploaded successfully'}
#     else:
#         return {'error': 'Upload failed'}