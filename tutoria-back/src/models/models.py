import os
from sqlalchemy import Column, engine, ForeignKey, Integer, String, Float, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URI = os.getenv('CONNEXION_STRING')

engine = create_engine(DATABASE_URI)
Base = declarative_base()
db_session = scoped_session(sessionmaker(bind=engine))
Base.query = db_session.query_property()

db = SQLAlchemy(query_class=Base)

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    adress = Column(String(100), nullable=True)
    cp = Column(String(5), nullable=True)
    tel = Column(String(10), nullable=True)
    type = Column(Integer, nullable=False) #1: Ecole, 2: CFA, 3: Entreprise
    # Students = relationship('students', back_populates='company')

#Relation Company - Student
class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=True)
    last_name = Column(String(100), nullable=True)
    adress = Column(String(100), nullable=True)
    cp = Column(String(5), nullable=True)
    mail = Column(String(100), nullable=False)
    tel = Column(String(10), nullable=True)
    schoolId = Column(Integer, ForeignKey('company.id'), nullable=True)
    cfaId = Column(Integer, ForeignKey('company.id'), nullable=True)
    enterpriseId = Column(Integer, ForeignKey('company.id'), nullable=True)
    
class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True, autoincrement=True)
    intitle = Column(String(100), nullable=False)
    descr = Column(String(100), nullable=True)
    course = Column(String(10000), nullable=True)
    annexe = Column(String(100), nullable=True) #idDoc?
    idCompany = Column(Integer, ForeignKey('company.id'), nullable=False)
    # studentsCourses = relationship('students', back_populates='course') # Relation Formation - Company: 

# Relation Formation + Certification - Student

class Certifications(Base):
    __tablename__ = "certifications"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    score= Column(Float)
    idCompany = Column(Integer, ForeignKey('company.id'), nullable=False) #enlever
    # certifiedStudent= relationship('students', back_populates='certifications')

class Documents (Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    path = Column(String(100), nullable=False)
    idCompany = Column(Integer, ForeignKey('company.id'), nullable=True)
    idStudent = Column(Integer, ForeignKey('students.id'), nullable=True)

