from sqlalchemy import Float, create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy import select, func, desc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

class Materia():
    __tablename__ = 'Materia'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    total_de_aulas = Column(Integer)
