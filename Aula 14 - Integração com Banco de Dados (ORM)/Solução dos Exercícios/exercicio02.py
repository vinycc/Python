from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base

# Criar Conexão com Banco SQLITE
# caso o arquivo de banco não exista, ele será criado
engine = create_engine("sqlite:///servidor.db")
connection = engine.connect()

# Criar sessão com o Banco de Dados
session = Session()

# Instância da classe Base do SQLAlchemy
Base = declarative_base(engine)

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


# Cria um arquivo de texto
arquivo = open('saida.txt', 'w', encoding='UTF-8')

# Realiza consulta no banco de dados
resultado = session.query(Funcionario).order_by(Funcionario.nome)
for r in resultado:
    arquivo.write(r.nome + ';' + str(r.idade) + ';' + str(r.salario) + '\n')

# fecha arquivo e conexao com o banco
arquivo.close()
connection.close()
