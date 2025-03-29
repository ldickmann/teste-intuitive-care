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
      <ul>
        <li
          v-for="(result, index) in results"
          :key="index">
          {{ result.name }} - {{ result.cnpj }} - {{ result.city }}
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

  async function search(query) {
    isLoading.value = true;
    errorMessage.value = "";
    results.value = [];
    try {
      const response = await axios.get("http://localhost:5000/search", {
        params: { query },
      });
      results.value = response.data;
    } catch (error) {
      errorMessage.value = "Erro ao buscar os dados.";
      console.error("Erro na busca:", error);
    } finally {
      isLoading.value = false;
    }
  }

  return {
    isLoading,
    errorMessage,
    results,
    search,
  };
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
  margin: 20px;
  font-family: Arial, sans-serif;
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
</style>
