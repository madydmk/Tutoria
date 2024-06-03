import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv('CONNEXION_STRING')
engine = create_engine(DATABASE_URI)
connection = engine.connect()
    
Session = sessionmaker(bind=engine)
session = Session()