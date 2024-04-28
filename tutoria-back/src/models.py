from sqlalchemy import Column, engine, ForeignKey, Integer, String, Float, create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URI = 'mysql://root:Diakitem1.@127.0.0.1:3306/Tutoria'

engine = create_engine(DATABASE_URI)
Base = declarative_base()
db_session = scoped_session(sessionmaker(bind=engine))
Base.query = db_session.query_property()

db = SQLAlchemy(query_class=Base)

class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    adress = Column(String(100), nullable=False)
    cp = Column(String(5), nullable=False)
    tel = Column(String(10), nullable=False)
    type = Column(Integer, nullable=False) #1: Ecole, 2: CFA, 3: Entreprise
    # Students = relationship('students', back_populates='company')

#Relation Company - Student
class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    adress = Column(String(100), nullable=False)
    cp = Column(String(5), nullable=False)
    mail = Column(String(100), nullable=False)
    tel = Column(String(10), nullable=True)
    schoolId = Column(Integer, ForeignKey('company.id'), nullable=True)
    cfaId = Column(Integer, ForeignKey('company.id'), nullable=True)
    enterpriseId = Column(Integer, ForeignKey('company.id'), nullable=True)
    
class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True, autoincrement=True)
    intitle = Column(String(100), nullable=False)
    descr = Column(String(100), nullable=False)
    course = Column(String(10000), nullable=False)
    annexe = Column(String(100), nullable=False)
    idCompany = Column(Integer, ForeignKey('company.id'), nullable=False)
    # studentsCourses = relationship('students', back_populates='course') # Relation Formation - Company: 

# Relation Formation + Certification - Student

class Certifications(Base):
    __tablename__ = "certifications"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    score= Column(Float)
    idCompany = Column(Integer, ForeignKey('company.id'), nullable=False)
    # certifiedStudent= relationship('students', back_populates='certifications')

class Documents (Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    path = Column(String(100), nullable=False)
    idCompany = Column(Integer, ForeignKey('company.id'), nullable=False)
    idStudent = Column(Integer, ForeignKey('students.id'), nullable=False)

