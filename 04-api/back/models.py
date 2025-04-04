from sqlalchemy import Column, Integer, String, Date
from database import Base


class Provider(Base):
    __tablename__ = 'operadoras'

    id = Column(Integer, primary_key=True, index=True)
    registro_ans = Column(String)
    cnpj = Column(String)
    razao_social = Column(String)
    nome_fantasia = Column(String)
    modalidade = Column(String)
    logradouro = Column(String)
    numero = Column(String)
    complemento = Column(String)
    bairro = Column(String)
    cidade = Column(String)
    uf = Column(String)
    cep = Column(String)
    ddd = Column(String)
    telefone = Column(String)
    fax = Column(String)
    endereco_eletronico = Column(String)
    representante = Column(String)
    cargo_representante = Column(String)
    regiao_de_comercializacao = Column(Integer)
    data_registro_ans = Column(Date)
