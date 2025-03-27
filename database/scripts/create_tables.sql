CREATE DATABASE intuitive_care;

CREATE TABLE IF NOT EXISTS operadoras_ans (
  Registro_ANS INT UNSIGNED NOT NULL COMMENT 'Número de registro da operadora na ANS',
  CNPJ VARCHAR(14) NOT NULL COMMENT 'Cadastro Nacional da Pessoa Jurídica da operadora',
  Razao_Social VARCHAR(255) NOT NULL COMMENT 'Nome legal da operadora',
  Nome_Fantasia VARCHAR(255) DEFAULT NULL COMMENT 'Nome comercial da operadora',
  Modalidade VARCHAR(100) NOT NULL COMMENT 'Modalidade da operadora (Ex: Medicina de Grupo, Autogestão)',
  Logradouro VARCHAR(255) NOT NULL COMMENT 'Endereço da sede da operadora (Rua, Avenida, etc.)',
  Numero VARCHAR(20) DEFAULT NULL COMMENT 'Número do endereço da sede',
  Complemento VARCHAR(100) DEFAULT NULL COMMENT 'Complemento do endereço (sala, andar, etc.)',
  Bairro VARCHAR(100) NOT NULL COMMENT 'Bairro da sede',
  Cidade VARCHAR(100) NOT NULL COMMENT 'Cidade da sede',
  UF CHAR(2) NOT NULL COMMENT 'Unidade Federativa da sede',
  CEP VARCHAR(8) NOT NULL COMMENT 'Código de Endereçamento Postal da sede',
  DDD VARCHAR(2) DEFAULT NULL COMMENT 'Código de Discagem Direta',
  Telefone VARCHAR(20) DEFAULT NULL COMMENT 'Número de telefone principal',
  Fax VARCHAR(20) DEFAULT NULL COMMENT 'Número de fax',
  Endereco_eletronico VARCHAR(255) NOT NULL COMMENT 'Endereço de e-mail principal',
  Representante VARCHAR(255) NOT NULL COMMENT 'Nome do representante legal da operadora',
  Cargo_Representante VARCHAR(100) NOT NULL COMMENT 'Cargo do representante legal',
  Regiao_de_Comercializacao VARCHAR(1) DEFAULT NULL COMMENT 'Código da região de comercialização (se aplicável)',
  Data_Registro_ANS DATE NOT NULL COMMENT 'Data de registro da operadora na ANS',
  CONSTRAINT pk_operadoras_ans PRIMARY KEY (Registro_ANS),
  CONSTRAINT uq_operadoras_ans_CNPJ UNIQUE (CNPJ)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = 'Tabela para armazenar informações cadastrais das operadoras de planos de saúde registradas na ANS, extraídas do arquivo relatorio_cadop.csv';

CREATE TABLE IF NOT EXISTS despesas_operadoras (
  id INT AUTO_INCREMENT PRIMARY KEY,
  data_movimentacao DATE NOT NULL COMMENT 'Data da movimentação',
  registro_ans INT UNSIGNED NOT NULL COMMENT 'Número de registro da operadora na ANS',
  codigo_conta_contabil VARCHAR(20) NOT NULL COMMENT 'Código da conta contábil',
  descricao VARCHAR(255) NOT NULL COMMENT 'Descrição da conta contábil',
  saldo_inicial DECIMAL(18, 2) NOT NULL COMMENT 'Saldo inicial do período',
  saldo_final DECIMAL(18, 2) NOT NULL COMMENT 'Saldo final do período',
  CONSTRAINT fk_registro_ans FOREIGN KEY (registro_ans) REFERENCES operadoras_ans (Registro_ANS)
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = 'Tabela para armazenar as despesas das operadoras.';