import sqlalchemy

from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///server.db")
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
    nome = Column('NOME', String(255))
    idade = Column('IDADE', Integer)
    salario = Column('SALARIO', Float)

    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario = salario


lista_funcionarios = []
for i in range(3):                                  # cadastra 3 funcionarios
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    salario = float(input('Salario: '))
    func = Funcionario(nome, idade, salario)        # cria o objeto
    lista_funcionarios.append(func)                 # insere na lista

session.add_all(lista_funcionarios)                 # adiciona o Banco de dados
session.commit()

print('\nTodos os Funcionários:')
lista = session.query(Funcionario)
for func in lista:
    print(func.id, func.nome, func.idade, func.salario)

print('\nFuncionários com salário superior a R$1500:')
lista = session.query(Funcionario).filter(Funcionario.salario > 1500)
for func in lista:
    print(func.id, func.nome, func.idade, func.salario)
