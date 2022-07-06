import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///servidor.db")
connection = engine.connect()


# Cria uma Sessão com o banco de dados
Base = declarative_base(engine)
session = Session()


connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255) NOT NULL,
                        IDADE INT NOT NULL,
                        SALARIO FLOAT NOT NULL)
                    """)


class Funcionario(Base):
    __tablename__ = 'FUNCIONARIO'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)
    idade = Column('IDADE', Integer, nullable=False)
    salario = Column('SALARIO', Float, nullable=False)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


lista = []
for i in range(3):
    nome = input("Informe o nome:")
    idade = int(input("Informe a idade:"))
    salario = float(input("Informe o salário:"))
    funcionario = Funcionario(nome, idade, salario)
    lista.append(funcionario)

session.add_all(lista)
session.commit()

resultado = session.query(Funcionario)
print('-'*40)
for f in resultado:
    print(f.id, f.nome, f.idade, f.salario)

resultado = session.query(Funcionario).filter(
    Funcionario.salario > 1500).order_by(Funcionario.nome.desc()).all()
print('-'*40)
for f in resultado:
    print(f.id, f.nome, f.idade, f.salario)

connection.close()
