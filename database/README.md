# Teste Banco de Dados - Intuitive Care

## Banco de Dados - Criação de scripts SQL

## Conteúdo

- **create_tables.sql**  
  Script para criação do banco de dados `intuitive_care` e das tabelas:

  - `operadoras_ans` – Armazena informações cadastrais das operadoras.
  - `despesas_operadoras` – Registra as despesas das operadoras, relacionando com as informações de cadastro.

- **import_data.sql**  
  Script para importação dos dados dos arquivos CSV:

  - `relatorio_cadop.csv` para os dados das operadoras.
  - Arquivos de despesas (ex.: `4T2023.csv` e `3T2023.csv`).

- **queries.sql**  
  Consultas SQL para:
  - Listar as 10 operadoras com maiores despesas no último ano.
  - Listar as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre.

## Como Utilizar

1. **Criação das Tabelas:**  
   Execute o script `create_tables.sql` para criar o banco de dados e as tabelas necessárias.

2. **Importação dos Dados:**  
   Utilize o script `import_data.sql` para carregar os dados dos arquivos CSV.  
   Atenção: Verifique os caminhos dos arquivos CSV e as configurações do MySQL Server.

3. **Execução das Consultas:**  
   Após a importação, execute o script `queries.sql` para visualizar os relatórios com as despesas.

## Requisitos

- MySQL Server 8.0 ou superior.
- Configuração correta dos diretórios de upload dos CSVs conforme especificado nos scripts.

## Autor

- Lucas Elias Dickmann
