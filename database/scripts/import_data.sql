-- Script para importar os dados dos CSVs com os registros das operadoras e as despesas das operadoras
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/relatorio_cadop.csv' INTO TABLE operadoras_ans CHARACTER SET utf8mb4 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (
  Registro_ANS,
  CNPJ,
  Razao_Social,
  Nome_Fantasia,
  Modalidade,
  Logradouro,
  Numero,
  Complemento,
  Bairro,
  Cidade,
  UF,
  CEP,
  DDD,
  Telefone,
  Fax,
  Endereco_eletronico,
  Representante,
  Cargo_Representante,
  Regiao_de_Comercializacao,
  @Data_Registro_ANS
)
SET
  Data_Registro_ANS = @Data_Registro_ANS;

-- Script para carregar os dados dos CSVs de despesas das operadoras (É preciso executar em para cada arquivo CSV)
-- Arquivo 4T2023.csv carregado com o script abaixo
USE intuitive_care;

-- Desativação da chave estrangeira para permitir a carga dos dados
SET
  foreign_key_checks = 0;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/4T2023.csv' INTO TABLE despesas_operadoras CHARACTER SET utf8mb4 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (
  @data_movimentacao,
  registro_ans,
  codigo_conta_contabil,
  descricao,
  @saldo_inicial,
  @saldo_final
)
SET
  data_movimentacao = STR_TO_DATE(@data_movimentacao, '%d/%m/%Y'),
  saldo_inicial = CAST(
    REPLACE(REPLACE(TRIM(@saldo_inicial), '.', ''), ',', '.') AS DECIMAL(18, 2)
  ),
  saldo_final = CAST(
    REPLACE(REPLACE(TRIM(@saldo_final), '.', ''), ',', '.') AS DECIMAL(18, 2)
  );

-- Reativação da chave estrangeira
SET
  foreign_key_checks = 1;

-- Arquivo 3T2023.csv carregado com o script abaixo
USE intuitive_care;

-- Desativação da chave estrangeira para permitir a carga dos dados
SET
  foreign_key_checks = 0;

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/3T2023.csv' INTO TABLE despesas_operadoras CHARACTER SET utf8mb4 FIELDS TERMINATED BY ';' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 ROWS (
  @data_movimentacao,
  registro_ans,
  codigo_conta_contabil,
  descricao,
  @saldo_inicial,
  @saldo_final
)
SET
  -- Modifcação do formato da data para importação de certos arquivos
  data_movimentacao = STR_TO_DATE(@data_movimentacao, '%Y-%m-%d'),
  saldo_inicial = CAST(
    REPLACE(REPLACE(TRIM(@saldo_inicial), '.', ''), ',', '.') AS DECIMAL(18, 2)
  ),
  saldo_final = CAST(
    REPLACE(REPLACE(TRIM(@saldo_final), '.', ''), ',', '.') AS DECIMAL(18, 2)
  );

-- Reativação da chave estrangeira
SET
  foreign_key_checks = 1;