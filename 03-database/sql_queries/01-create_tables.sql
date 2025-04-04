-- Não coloquei mais restrições por não conhecer as regras do negócio e por
-- falta de compatibilidade entre as restrições apresentadas nos dicionários de
-- dados e os dados dos arquivos csv

BEGIN TRANSACTION;

CREATE TABLE demonstracoes_contabeis (
	id SERIAL PRIMARY KEY,
	data DATE,
	reg_ans INTEGER,
	cd_conta_contabil INTEGER,
	descricao VARCHAR(150),
	vl_saldo_inicial NUMERIC(12,2),
	vl_saldo_final NUMERIC(12,2)
)

CREATE TABLE operadoras (
	id SERIAL PRIMARY KEY,
	registro_ans VARCHAR(6),
	cnpj VARCHAR(14),
	razao_social VARCHAR(140),
	nome_fantasia VARCHAR(140),
	modalidade VARCHAR,
	logradouro VARCHAR(40),
	numero VARCHAR(20),
	complemento VARCHAR(40),
	bairro VARCHAR(30),
	cidade VARCHAR(30),
	uf VARCHAR(2),
	cep VARCHAR(8),
	ddd VARCHAR(4),
	telefone VARCHAR(20),
	fax VARCHAR(20),
	endereco_eletronico VARCHAR(255),
	representante VARCHAR(50),
	cargo_representante VARCHAR(40),
	regiao_de_comercializacao INTEGER CHECK (regiao_de_comercializacao IN (1, 2, 3, 4, 5, 6)),
	data_registro_ans DATE
)

COMMIT

-- ROLLBACK
