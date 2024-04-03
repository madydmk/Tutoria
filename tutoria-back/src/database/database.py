# from sqlalchemy import create_engine, null

# # Remplacez 'username', 'password', 'hostname', 'database_name' par vos informations
# DATABASE_URI = 'mysql://username:password@hostname/database_name'
# connection = null
# def open():
#     engine = create_engine(DATABASE_URI)
#     connection = engine.connect()
#     return connection

# def close():
#     if connection!= null:
#         connection.close()

from sqlalchemy import create_engine
# from models import Model
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# 'username', 'password', 'hostname', 'database_name'
DATABASE_URI = 'mysql://root:Diakitem1.@127.0.0.1:3306/Tutoria'

engine = create_engine(DATABASE_URI)
connection = engine.connect()

# def init_db():
#     Model.metadata.create_all(bind=engine)


# Model = declarative_base(name='Model')
# Model.query = db_session.query_property()
    
#Create session to exec operations: insert, update...
    
Session = sessionmaker(bind=engine)
session = Session()