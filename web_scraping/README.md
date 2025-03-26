# Teste de Web Scraping - Intuitive Care

## Web Scraping - Extração e Compactação de PDFs

Este projeto realiza web scraping para a extração de links de arquivos PDF a partir de páginas web, efetuando o download dos mesmos e compactando-os em um arquivo ZIP.

## Estrutura do Projeto

- **scripts/**: Contém os scripts Python que orquestram o processo:
  - [`web_scraping.py`](c:\Users\ldick\testes\teste-intuitive-care\web_scraping\scripts\web_scraping.py): Script principal que executa o scraping, o download e a compactação.
  - [`download_pdfs.py`](c:\Users\ldick\testes\teste-intuitive-care\web_scraping\scripts\download_pdfs.py): Responsável pelo download dos PDFs.
  - [`utils.py`](c:\Users\ldick\testes\teste-intuitive-care\web_scraping\scripts\utils.py): Funções utilitárias para configuração do Selenium WebDriver e extração de links.
  - [`zip_pdfs.py`](c:\Users\ldick\testes\teste-intuitive-care\web_scraping\scripts\zip_pdfs.py): Responsável pela compactação dos PDFs baixados.
- **pdfs/**: Diretório onde os arquivos PDF serão salvos e o ZIP será criado.

## Requisitos

- Python 3.x
- Dependências: Consulte [requirements.txt](c:\Users\ldick\testes\teste-intuitive-care\web_scraping\requirements.txt) para a lista completa.

## Como Utilizar

1. **Instalar as dependências:**

   ```sh
   pip install -r requirements.txt
   ```

2. **Executar o script principal:**

   ```sh
   python -m scripts.web_scraping
   ```

O script principal acessa a URL configurada, extrai os links dos PDFs, baixa os arquivos para o diretório `pdfs/` e, por fim, compacta-os em `anexos_pdfs.zip`.

## Boas Práticas

- Utilize um ambiente virtual (virtualenv/venv) para isolar as dependências do projeto.
- Verifique os logs gerados para monitorar e depurar o processo de execução.
- Mantenha a estrutura de diretórios organizada para facilitar futuras manutenções.

## Autor

- Lucas Elias Dickmann
