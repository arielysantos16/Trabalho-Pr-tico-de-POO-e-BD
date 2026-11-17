from datetime import date, datetime
import string

#from click import INT
from sqlalchemy import select, update, delete, insert, func, asc, desc
from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

#Criando o BD
engine = create_engine('sqlite:///escola.db')

Base = declarative_base()

#Criando as tabelas
aluno_materia = Table(
    'aluno_materia', Base.metadata,
    Column('ra', Integer, ForeignKey('alunos.ra'), primary_key=True),
    Column('id', Integer, ForeignKey('materia.id'), primary_key=True)
)

class Aluno(Base):
    __tablename__ = 'alunos'
    ra = Column(Integer, primary_key=True)
    data_nasc = Column(Date)
    nome = Column(String)
    turma = Column(String)
    
    materias = relationship('Materia', secondary=aluno_materia, back_populates='alunos')

    def __repr__(self):
        return f"Aluno({self.ra}, {self.nome!r})"

class Materia(Base):
    __tablename__ = 'materias'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    total_de_aulas = Column(Integer)
    
    alunos = relationship('Aluno', secondary=aluno_materia, back_populates='materias')

    def __repr__(self):
        return f"Materia({self.id}, {self.nome!r})"
    
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

#inserindo dados
web = Materia(id=1, nome='Programação de Sites Web', total_de_aulas=150)
poo = Materia(id=2, nome='Programação Orientada a Objetos', total_de_aulas=200)
bd = Materia(id=3, nome='Banco de Dados', total_de_aulas=120)
hardware = Materia(id=4, nome='Fundamentos de Hardware', total_de_aulas=120)

alunos = [
    Aluno(ra=1001, nome='Ana Bia', data_nasc=date(2009, 11, 13), turma='Info 2A', materias=[web]),
    Aluno(ra=1002, nome='João Miranda', data_nasc=date(2010, 4, 22), turma='Info 2A', materias=[web, poo, bd, hardware]),
    Aluno(ra=1003, nome='Matheus Alves', data_nasc=date(2010, 2, 10), turma='Info 2A', materias=[web, poo]),
    Aluno(ra=1004, nome='Valdete Almeida', data_nasc=date(2009, 9, 18), turma='Info 2B', materias=[web, poo, bd]),
]
session.add_all(alunos)
session.commit()

#Consultas com o select

#mostra tudo de materia
query_1 = select(Materia)
saida_1 = session.execute(query_1).all()
for linha in session.execute(query_1):
    print(linha.Materia)

#mostra os alunos que tem a materia de bd
query_2 = select(Aluno).where(Aluno.materias.any(Materia.nome == 'Banco de Dados'))
saida_2 = session.execute(query_2).all()
for linha in session.execute(query_2):
    print(linha.Aluno.nome, linha.Aluno.materias)

#mostra o nome e a turma de cada aluno
query_3 = select(Aluno.nome, Aluno.turma)
saida_3 = session.execute(query_3).all()
for linha in session.execute(query_3):
    print(linha.nome, '-', linha.turma)

session.close()