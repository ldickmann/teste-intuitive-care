# Teste Interface & API - Intuitive Care

Este projeto implementa a interface e as APIs que permitem consultas e manipulação de dados relacionados às operadoras, utilizando tecnologias modernas tanto no backend quanto no frontend.

## Tecnologias Utilizadas

### API (Backend)

- **FastAPI** – Framework Python para construção de APIs RESTful. Veja a configuração e definição dos endpoints em [interface_api/api/main.py](c:\Users\ldick\testes\teste-intuitive-care\interface_api\api\main.py).
- **Pandas** – Para a manipulação e análise dos dados utilizados nas buscas, como visto em [interface_api/api/services/search.py](c:\Users\ldick\testes\teste-intuitive-care\interface_api\api\services\search.py).
- **fuzzywuzzy** e **Unidecode** – Utilizados para buscas aproximadas e normalização dos dados.
- **Configurações por meio de Settings** – Configurações globais da API definidas em [interface_api/api/core/config.py](c:\Users\ldick\testes\teste-intuitive-care\interface_api\api\core\config.py).

### Frontend

- **Vue 3** – Framework para construção de interfaces reativas. O aplicativo frontend se inicia em [interface_api/frontend/src/main.js](c:\Users\ldick\testes\teste-intuitive-care\interface_api\frontend\src\main.js).
- **Vite** – Ferramenta de build e desenvolvimento rápida, conforme configurações em [interface_api/frontend/vite.config.js](c:\Users\ldick\testes\teste-intuitive-care\interface_api\frontend\vite.config.js).
- **Axios** – Utilizado para realizar chamadas HTTP à API, conforme exemplificado em [interface_api/frontend/src/views/HomeView.vue](c:\Users\ldick\testes\teste-intuitive-care\interface_api\frontend\src\views\HomeView.vue).

### Outros Recursos

- **Coleção Postman** – Disponível em [interface_api/colecao_postman/API Operadoras.postman_collection.json](c:\Users\ldick\testes\teste-intuitive-care\interface_api\colecao_postman\API Operadoras.postman_collection.json) para facilitar os testes de integração com a API.

## Como Executar

### API

1. Navegue até o diretório da API:

   ```sh
   cd interface_api
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
3. Execute a API:
   ```sh
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```
4. Acesse a documentação interativa em [http://localhost:8000/docs](http://localhost:8000/docs).

### Frontend

1. Navegue até o diretório do frontend:
   ```sh
   cd interface_api/frontend
   ```
2. Instale as dependências (caso esteja usando Yarn ou npm):
   ```sh
   yarn install
   ```
3. Inicie o servidor de desenvolvimento:
   ```sh
   yarn dev
   ```
4. Acesse a aplicação em [http://localhost:5173/](http://localhost:5173/) (a porta pode variar conforme a configuração do Vite).

## Considerações Finais

- Certifique-se de que o arquivo de dados configurado em [interface_api/api/core/config.py](c:\Users\ldick\testes\teste-intuitive-care\interface_api\api\core\config.py) esteja disponível e corretamente posicionado.
- Utilize a coleção Postman para testar os endpoints e validar a integração entre o frontend e a API.

---

Autor: Lucas Elias Dickmann
