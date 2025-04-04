-- Após criar as tabelas, os comandos desse arquivo devem ser executados para
-- que os dados do arquivos csv sejam copiados para as tabelas no banco de dados

-- Para evitar problemas de codificação dos arquivos, fiz a cópia dos arquivos
-- para o banco de dados usando o WSL.

-- Os caminhos devem ser substituidos pelos caminhos absolutos dos arquivos

-- Comandos para a tabela demonstracoes_contabeis
\copy demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM '/mnt/c/Users/aqui/vem/o/caminho/absoluto/03-database/csv_files/treated_csv_files/demonstracoescontabeis/1T2023.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';');
\copy demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM '/mnt/c/Users/aqui/vem/o/caminho/absoluto/03-database/csv_files/treated_csv_files/demonstracoescontabeis/1T2024.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';');
\copy demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM '/mnt/c/Users/aqui/vem/o/caminho/absoluto/03-database/csv_files/treated_csv_files/demonstracoescontabeis/2t2023.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';');
\copy demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM '/mnt/c/Users/aqui/vem/o/caminho/absoluto/03-database/csv_files/treated_csv_files/demonstracoescontabeis/2T2024.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';');
\copy demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM '/mnt/c/Users/aqui/vem/o/caminho/absoluto/03-database/csv_files/treated_csv_files/demonstracoescontabeis/3T2023.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';');
\copy demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM '/mnt/c/Users/aqui/vem/o/caminho/absoluto/03-database/csv_files/treated_csv_files/demonstracoescontabeis/3T2024.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';');
\copy demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM '/mnt/c/Users/aqui/vem/o/caminho/absoluto/03-database/csv_files/treated_csv_files/demonstracoescontabeis/4T2023.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';');
\copy demonstracoes_contabeis (data, reg_ans, cd_conta_contabil, descricao, vl_saldo_inicial, vl_saldo_final) FROM '/mnt/c/Users/aqui/vem/o/caminho/absoluto/03-database/csv_files/treated_csv_files/demonstracoescontabeis/4T2024.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';');

-- Comando para a tabela operadoras_ativas
\copy operadoras (registro_ans, cnpj, razao_social, nome_fantasia, modalidade, logradouro, numero, complemento, bairro, cidade, uf, cep, ddd, telefone, fax, endereco_eletronico, representante, cargo_representante, regiao_de_comercializacao, data_registro_ans) FROM 'mnt/c/Users/aqui/vem/o/caminho/absoluto/03-database/csv_files/treated_csv_files/demonstracoescontabeis/Relatorio_cadop.csv' WITH (FORMAT csv, HEADER true, ENCODING 'UTF8', DELIMITER ';');
