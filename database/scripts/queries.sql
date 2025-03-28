-- 10 operadoras com maiores despesas no último ano - Query para consulta
SELECT
  d.registro_ans,
  o.Razao_Social,
  SUM(d.saldo_final - d.saldo_inicial) AS total_despesas
FROM
  despesas_operadoras d
  JOIN operadoras_ans o ON d.registro_ans = o.Registro_ANS
WHERE
  d.descricao LIKE '%SINISTROS CONHECIDOS%'
  AND d.data_movimentacao >= DATE_SUB(
    (
      SELECT
        MAX(data_movimentacao)
      FROM
        despesas_operadoras
    ),
    INTERVAL 12 MONTH
  )
GROUP BY
  d.registro_ans,
  o.Razao_Social
ORDER BY
  total_despesas DESC
LIMIT
  10;

-- 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre
USE intuitive_care;

SELECT
  d.registro_ans,
  o.Razao_Social,
  SUM(d.saldo_final - d.saldo_inicial) AS total_despesas
FROM
  despesas_operadoras d
  JOIN operadoras_ans o ON d.registro_ans = o.Registro_ANS
WHERE
  d.descricao LIKE '%SINISTROS CONHECIDOS%'
  AND d.data_movimentacao >= DATE_SUB(
    (
      SELECT
        MAX(data_movimentacao)
      FROM
        despesas_operadoras
    ),
    INTERVAL 3 MONTH
  )
GROUP BY
  d.registro_ans,
  o.Razao_Social
ORDER BY
  total_despesas DESC
LIMIT
  10;