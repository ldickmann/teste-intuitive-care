# Teste Intuitive Care

## Sumário

- [Sobre](#sobre)
- [Estrutura de Diretórios](#estrutura-de-diretórios)
- [Pré-requisitos](#pré-requisitos)
- [Como Executar os Testes](#como-executar-os-testes)
  - [Data Transformation](#data-transformation)
  - [Database](#database)
  - [Interface & API](#interface--api)
  - [Web Scraping](#web-scraping)
- [Considerações Finais](#considerações-finais)

## Sobre

Este repositório contém diversos códigos realizados no teste da Intuitive Care, separados em diretórios que representam cada teste específico. Cada script foca em uma área da aplicação, permitindo análises isoladas e evoluções direcionadas.

## Estrutura de Diretórios

- **data_transformation**  
  Teste de Transformação de Dados – Realiza extração, transformação e limpeza dos dados.  
  Consulte o [README](data_transformation/README.md) para instruções detalhadas e execução dos scripts.

- **database**  
  Teste Banco de Dados – Contém scripts SQL para criação, importação e consulta dos dados.  
  Veja o [README](database/README.md) para orientações sobre a configuração e execução dos scripts.

- **interface_api**  
  Teste Interface & API – Implementa a API com FastAPI e a interface frontend (Vue 3), possibilitando a consulta de dados das operadoras.  
  As instruções de uso estão no [README](interface_api/README.md).

- **web_scraping**  
  Teste de Web Scraping – Realiza a extração e compactação de PDFs a partir de páginas web.  
  Detalhes sobre a configuração e execução encontram-se no [README](web_scraping/README.md).

## Pré-requisitos

- Python 3.x
- Node.js (para o frontend)
- Dependências específicas para cada teste (consulte os READMEs dentro de cada diretório)
- Banco de dados (para o teste banco de dados)

## Como Executar

### Data Transformation

1. Entre no diretório:
   ```sh
   cd data_transformation
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```sh
   python scripts/main.py
   ```

### Database

1. Siga as instruções do README para criação das tabelas, importação dos dados e execução das consultas.

### Interface & API

1. Crie um ambiente virtual e instale as dependências:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
2. Inicie o servidor da API:
   ```sh
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```
3. Para a interface frontend, acesse o diretório e execute:
   ```sh
   cd frontend
   yarn install
   yarn dev
   ```
4. A documentação interativa da API está disponível em [http://localhost:8000/docs](http://localhost:8000/docs).

### Web Scraping

1. Entre no diretório:
   ```sh
   cd web_scraping
   ```
2. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```sh
   python scripts/web_scraping.py
   ```

## Considerações Finais

- Use ambientes virtuais (virtualenv ou venv) para isolar as dependências de cada teste.
- Verifique se os arquivos de configuração e os dados necessários estão corretamente posicionados conforme descrito.
- Mantenha a documentação atualizada consultando as instruções específicas de cada teste.

---

Autor: Lucas Elias Dickmann
