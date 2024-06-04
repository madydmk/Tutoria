from flask import jsonify
from models.models import Company, Students, User
import models.database as db
current_user = User
def get_connected_user():
    pass

def log_in():
    #check_db, check_pwd
    current_user = ''
    pass

def log_out():
    pass

def sign_in():
    pass

def sign_out():
    #supprimer compte
    #bool deleted: true
    pass
