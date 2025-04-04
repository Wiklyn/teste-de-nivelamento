<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import SearchBar from './components/SearchBar.vue'
import ProviderCard from './components/ProviderCard.vue'
import type { IProvider } from './models/IProvider'

const providers = ref<IProvider[]>([])

onMounted(async () => {
  try {
    const response = await fetch('http://127.0.0.1:8000/providers')
    if (!response.ok) {
      throw new Error(`Erro: ${response.status}`)
    }
    providers.value = await response.json()
  } catch (error) {
    console.error('Erro ao buscar os dados:', error)
  }
})

const currentPage = ref(1)
const pageSize = 10

// Total de páginas baseado no número de providers
const totalPages = computed(() => Math.ceil(providers.value.length / pageSize))

// Lista de providers filtrada pela página atual
const paginatedProviders = computed(() => {
  const start = (currentPage.value - 1) * pageSize
  return providers.value.slice(start, start + pageSize)
})

// // Função para mudar de página
const goToPage = (page: number) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page
  }
}

const searchFilter = ref('')

const filteredProviders = computed(() => {
  if (!searchFilter.value) return paginatedProviders.value

  return providers.value.filter((provider) =>
    Object.values(provider).some((value) =>
      String(value).toLowerCase().includes(searchFilter.value.toLowerCase()),
    ),
  )
})

const handleSearch = (search: string) => {
  searchFilter.value = search
}
</script>

<template>
  <main>
    <h1>Operadoras de Planos de Saúde com Registro Ativo</h1>
    <SearchBar @search="handleSearch" />
    <span class="card-tracking">
      Mostrando {{ paginatedProviders.length }} de {{ providers.length }} resultados (Página
      {{ currentPage }} de {{ totalPages }})
    </span>
    <!-- Paginação -->
    <div class="pagination">
      <button @click="goToPage(currentPage - 1)" :disabled="currentPage === 1">Anterior</button>

      <select v-model="currentPage" @change="goToPage(currentPage)">
        <option v-for="page in totalPages" :key="page" :value="page">Página {{ page }}</option>
      </select>

      <button @click="goToPage(currentPage + 1)" :disabled="currentPage === totalPages">
        Próximo
      </button>
    </div>
    <div class="provider-list">
      <ProviderCard v-for="provider in filteredProviders" :key="provider.id" :provider="provider" />
    </div>
    <!-- Paginação -->
    <div class="pagination">
      <button @click="goToPage(currentPage - 1)" :disabled="currentPage === 1">Anterior</button>

      <select v-model="currentPage" @change="goToPage(currentPage)">
        <option v-for="page in totalPages" :key="page" :value="page">Página {{ page }}</option>
      </select>

      <button @click="goToPage(currentPage + 1)" :disabled="currentPage === totalPages">
        Próximo
      </button>
    </div>
  </main>
</template>

<style scoped>
main {
  display: grid;
  gap: 1rem;
}

h1 {
  line-height: 2.5rem;
}

.provider-list {
  display: grid;
  gap: 1.5rem;
}

.pagination {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  justify-content: center;
}

button {
  padding: 0.5rem 1rem;
  cursor: pointer;
  border: 1px solid #ddd;
  background-color: #f8f8f8;
}

button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

select {
  padding: 0.5rem;
  font-size: 1rem;
}
</style>
