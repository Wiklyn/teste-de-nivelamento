from pydantic import BaseModel
from datetime import date


class HealthInsuranceProviderSchema(BaseModel):
    id: int
    registro_ans: str | None
    cnpj: str | None
    razao_social: str | None
    nome_fantasia: str | None
    modalidade: str | None
    logradouro: str | None
    numero: str | None
    complemento: str | None
    bairro: str | None
    cidade: str | None
    uf: str | None
    cep: str | None
    ddd: str | None
    telefone: str | None
    fax: str | None
    endereco_eletronico: str | None
    representante: str | None
    cargo_representante: str | None
    regiao_de_comercializacao: int | None
    data_registro_ans: date | None

    class Config:
        from_attributes = True
