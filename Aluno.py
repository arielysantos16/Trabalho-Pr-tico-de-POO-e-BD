from datetime import date, datetime
import string

from click import INT
from sqlalchemy import Float, create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy import select, func, desc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

class Aluno():
    __tablename__ = 'Aluno'
    ra = Column(Integer, primary_key=True)
    data_nasc = Column(Float)
    nome = Column(String)
    turma = Column(String)