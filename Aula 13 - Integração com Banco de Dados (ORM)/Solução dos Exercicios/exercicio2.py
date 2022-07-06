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
    __tablename__ = 'Autor'
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    nome = Column('NOME', String(255))

    def __init__(self, nome):
        self.nome = nome


class Livro(Base):
    __tablename__ = "LIVRO"
    id = Column('ID', Integer, primary_key=True, autoincrement=True)
    titulo = Column('TITULO', String(255))
    paginas = Column('PAGINAS', Integer)
    autor_id = Column('AUTOR_ID', Integer)

    def __init__(self, titulo, paginas, autor_id):
        self.titulo = titulo
        self.paginas = paginas
        self.autor_id = autor_id


autor1 = Autor('João')
autor2 = Autor('Maria')

lista = [autor1, autor2]
session.add_all(lista)
session.commit()


livro1 = Livro('Titulo do livro 1', 300, autor1.id)
livro2 = Livro('Titulo do livro 2', 150, autor2.id)

lista = [livro1, livro2]
session.add_all(lista)
session.commit()

# Busca todos os autores
resultado = session.query(Autor).all()
for r in resultado:
    print(r.id, r.nome)

# Busca todos os livros
resultado = session.query(Livro).all()
for r in resultado:
    print(r.id, r.titulo, r.paginas, r.autor_id)

# Exemplo de busca utilizando um Join
resultado = session.query(Livro, Autor).filter(Livro.autor_id == Autor.id).all()
for r in resultado:
    print(r.Livro.titulo, r.Autor.nome)
