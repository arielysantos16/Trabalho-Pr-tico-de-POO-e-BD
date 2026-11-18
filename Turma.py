from sqlalchemy import Float, create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy import select, func, desc
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from Base import Base

class Turma(Base):
    __tablename__ = 'turmas'
    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    
    alunos = relationship('Aluno', back_populates='turma_obj')

    def __repr__(self):
        return f"Turma({self.id}, {self.nome!r})"