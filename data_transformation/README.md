# Teste de Transformação de Dados - Intuitive Care

## Transformação de Dados - Análise e Limpeza de Dados

Este projeto tem como objetivo realizar a extração, análise, transformação e limpeza dos dados presentes no diretório `data_transformation`.

## Estrutura do Projeto

- **data/**: Diretório contendo os dados brutos
- **scripts/**: Scripts Python que executam as tarefas de transformação dos dados:
  - [`main.py`](c:\Users\ldick\testes\teste-intuitive-care\data_transformation\scripts\main.py): Script principal que orquestra o processo de transformação.
  - [`extract_data.py`](c:\Users\ldick\testes\teste-intuitive-care\data_transformation\scripts\extract_data.py): Responsável pela extração dos dados dos arquivos brutos.
  - [`transform_data.py`](c:\Users\ldick\testes\teste-intuitive-care\data_transformation\scripts\transform_data.py): Realiza a transformação e limpeza dos dados extraídos.
  - [`zip_data.py`](c:\Users\ldick\testes\teste-intuitive-care\data_transformation\scripts\zip_data.py): Opcional, para compactação dos dados transformados.

## Requisitos

- Python 3.x
- Dependências: Consulte o arquivo [requirements.txt](c:\Users\ldick\testes\teste-intuitive-care\data_transformation\requirements.txt) (caso exista) para obter a lista completa de bibliotecas necessárias.

## Como Utilizar

1. **Instalar as dependências:**

   ```sh
   pip install -r requirements.txt
   ```

2. **Executar o script principal:**

   ```sh
   python -m scripts.main
   ```

O script principal executa a extração dos dados a partir dos arquivos contidos em `data/`, realiza a transformação e limpeza apropriadas e, se necessário, compacta os resultados.

## Boas Práticas

- Utilize um ambiente virtual (venv ou virtualenv) para isolar as dependências do projeto.
- Verifique os logs gerados para monitorar e depurar o processo de transformação.
- Mantenha a estrutura de diretórios organizada para facilitar futuras manutenções.

## Autor

- Lucas Elias Dickmann
