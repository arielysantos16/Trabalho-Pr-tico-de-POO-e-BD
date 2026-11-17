from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
#juncao do Aluno com Materia
#teria q importar a classe/tabela  aluno, materia e a Base aqui ne?
aluno_materia = Table(
    'aluno_materia', Base.metadata,
    Column('ra', Integer, ForeignKey('alunos.ra'), primary_key=True),
    Column('id', Integer, ForeignKey('materia.id'), primary_key=True)
)