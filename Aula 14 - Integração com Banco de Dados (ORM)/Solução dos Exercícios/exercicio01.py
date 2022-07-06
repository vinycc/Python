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
    
connection.execute("""CREATE TABLE IF NOT EXISTS FUNCIONARIO (
                        ID INTEGER PRIMARY KEY,
                        NOME VARCHAR(255),
                        IDADE INTEGER,
                        SALARIO FLOAT)""")

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

# Abre o arquivo de texto
arquivo = open("funcionarios.txt", "r", encoding='UTF-8')

lista_funcionario = []

# percorre o arquivo de texto
for linha in arquivo:

    # separa linha pelo caracter ; e gera lista [nome, idade, salario]
    lista = linha.split(';')

    # cria um objeto Funcionario
    func = Funcionario(lista[0], int(lista[1]), float(lista[2]))

    # insere o objeto na lista
    lista_funcionario.append(func)

# insere lista de objetos no banco de dados
session.add_all(lista_funcionario)
session.commit()


# ----------------------------------------------------------
# Nome, idade e salário de cada funcionário cadastrado
print('-' * 30)
funcionarios = session.query(Funcionario)
for f in funcionarios:
    print(f.nome, f.idade, f.salario)


# ----------------------------------------------------------
# Funcionário com menor salário
print('-' * 30)
print('Funcionario com menor salário:')

funcionarios = session.query(Funcionario).order_by(Funcionario.salario)
print(funcionarios[0].nome, funcionarios[0].idade, funcionarios[0].salario)

# utilizando first()
obj = session.query(Funcionario).order_by(Funcionario.salario).first()
print(obj.nome, obj.idade, obj.salario)


# ----------------------------------------------------------
# Funcionário mais velho
print('-' * 30)
print('Funcionario mais velho:')

funcionarios = session.query(Funcionario).order_by(Funcionario.idade.desc())
print(funcionarios[0].nome, funcionarios[0].idade, funcionarios[0].salario)

# utilizando FIRST()
obj = session.query(Funcionario).order_by(Funcionario.idade.desc()).first()
print(obj.nome, obj.idade, obj.salario)


# ----------------------------------------------------------
# A média dos salários dos funcionários
print('-' * 30)
soma = 0
cont = 0
funcionarios = session.query(Funcionario)
for f in funcionarios:
    soma += f.salario
    cont += 1
media = soma / cont
print('Média dos salários: ', round(media, 2))

arquivo.close()
connection.close()
