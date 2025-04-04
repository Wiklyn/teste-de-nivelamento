-- 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR " no último trimestre
SELECT
	id,
	data,
	reg_ans,
	cd_conta_contabil,
	descricao,
	TO_CHAR(vl_saldo_inicial, 'FMR$ 999G999G990D99') AS vl_saldo_inicial,
	TO_CHAR(vl_saldo_final, 'FMR$ 999G999G990D99') AS vl_saldo_final,
	ABS(vl_saldo_final) - ABS(vl_saldo_inicial) AS despesa
FROM
	demonstracoes_contabeis
WHERE
	descricao LIKE 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR%'
	AND data >= (
		SELECT MAX(data) - INTERVAL '3 months'
    	FROM demonstracoes_contabeis
	)
ORDER BY
	despesa
LIMIT 10;


-- 10 operadoras com maiores despesas nessa categoria no último ano
SELECT
	DISTINCT(cd_conta_contabil),
	id,
	reg_ans,
	data,
	descricao,
	TO_CHAR(vl_saldo_inicial, 'FMR$ 999G999G990D99') AS vl_saldo_inicial,
	TO_CHAR(vl_saldo_final, 'FMR$ 999G999G990D99') AS vl_saldo_final,
	ABS(vl_saldo_final) - ABS(vl_saldo_inicial) AS despesa
FROM
	demonstracoes_contabeis
WHERE
	descricao LIKE 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTENCIA A SAUDE MEDICO HOSPITALAR%'
	AND EXTRACT(YEAR FROM data) = 2024
ORDER BY
	despesa
LIMIT 10;
