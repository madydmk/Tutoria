from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    adress = Column(String(100), nullable=False)
    cp = Column(String(5), nullable=False)
    tel = Column(String(10), nullable=False)
    type = Column(Integer, nullable=False) #1: Ecole, 2: CFA, 3: Entreprise

