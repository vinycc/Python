import sqlalchemy

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

# Criar Conexão com Banco SQLITE
# caso o arquivo não exista, ele será criado
engine = sqlalchemy.create_engine("sqlite:///servidor.db")
connection = engine.connect()


# Cria uma Sessão com o banco de dados
Base = declarative_base(engine)
session = Session()


connection.execute("""CREATE TABLE IF NOT EXISTS AUTOR (
                    ID INTEGER PRIMARY KEY,
                    NOME VARCHAR(255) NOT NULL)
                    """)

connection.execute("""CREATE TABLE IF NOT EXISTS LIVRO (
                        ID INTEGER PRIMARY KEY,
                        TITULO VARCHAR(255) NOT NULL,
                        PAGINAS INT NOT NULL,
                        AUTOR_ID INT NOT NULL)
                        """)


class Autor(Base):
    __tablename__ = 'autor'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255), nullable=False)

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = "LIVRO"
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255), nullable=False)
    paginas = Column('PAGINAS', Integer, nullable=False)
    autor_id = Column('AUTOR_ID', Integer, nullable=False)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


autor1 = Autor("Joaquim da Silva")
autor2 = Autor("Maria de Souza")

session.add(autor1)
session.add(autor2)
session.commit()

livro1 = Livro("Titulo do livro 1", 200, autor1.id)
livro2 = Livro("Titulo do livro 2", 150, autor2.id)

session.add(livro1)
session.add(livro2)
session.commit()

resultado = session.query(Autor).order_by(Autor.nome)
for r in resultado:
    print(r.id, r.nome)

resultado = session.query(Livro).order_by(Livro.titulo)
for r in resultado:
    print(r.id, r.titulo, r.paginas, r.autor_id)

# Exemplo de JOIN
resultado = session.query(Autor, Livro).filter(Autor.id == Livro.autor_id)
for r in resultado:
    print('-------------------------------')
    print("Titulo do livro: ", r.Livro.titulo)
    print("Nome do Autor: ", r.Autor.nome)

connection.close()
