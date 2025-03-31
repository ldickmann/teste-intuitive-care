<template>
  <div class="home-view">
    <h1>Busca de Operadoras</h1>

    <div class="search-container">
      <input
        v-model="searchTerm"
        @keyup.enter="performSearch"
        type="text"
        placeholder="Digite o nome, CNPJ ou cidade da operadora" />
      <button @click="performSearch">Buscar</button>
    </div>

    <div
      v-if="isLoading"
      class="loading">
      <p>Carregando...</p>
    </div>

    <div
      v-if="errorMessage"
      class="error-message">
      <p>{{ errorMessage }}</p>
    </div>

    <div v-if="results && results.length">
      <h2>Resultados da Busca:</h2>
      <ul class="operadoras-list">
        <li
          v-for="(result, index) in results"
          :key="index"
          class="operadora-card">
          <p>CNPJ: {{ result.cnpj }}</p>
          <p>Razão Social: {{ result.razao_social }}</p>
          <p>Nome Fantasia: {{ result.nome_fantasia }}</p>
          <p>Modalidade: {{ result.modalidade }}</p>
          <p>Logradouro: {{ result.logradouro }}</p>
          <p>Bairro: {{ result.bairro }}</p>
          <p>Cidade: {{ result.cidade }}</p>
          <p>CEP: {{ result.cep }}</p>
          <p>Telefone: {{ result.telefone }}</p>
          <p>Email: {{ result.email }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

// Composable para realizar a busca
function useSearch() {
  const isLoading = ref(false);
  const errorMessage = ref("");
  const results = ref([]);

  const search = async (term) => {
    isLoading.value = true;
    errorMessage.value = "";
    results.value = [];

    try {
      const response = await axios.get(`http://localhost:8000/api/buscar`, {
        params: { nome: term },
      });
      results.value = response.data;
    } catch (error) {
      errorMessage.value = "Erro ao buscar operadoras. Tente novamente.";
    } finally {
      isLoading.value = false;
    }
  };

  return { isLoading, errorMessage, results, search };
}

const searchTerm = ref("");
const { isLoading, errorMessage, results, search } = useSearch();

function performSearch() {
  if (searchTerm.value.trim()) {
    search(searchTerm.value);
  }
}
</script>

<style scoped>
.home-view {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 20px;
  gap: 20px;
}

.search-container {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}

input[type="text"] {
  padding: 8px;
  width: 300px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 8px 16px;
  background-color: #42b983;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #369870;
}

.loading {
  color: #666;
  margin-top: 10px;
}

.error {
  color: red;
  margin-top: 10px;
}

.operadoras-list {
  list-style-type: none;
  padding: 0;
}

.operadora-card {
  border: 1px solid #ccc;
  border-radius: 4px;
  padding: 10px;
  margin-bottom: 10px;
  background-color: #f9f9f9;
}
</style>
