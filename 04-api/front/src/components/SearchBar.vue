<script setup lang="ts">
import { ref } from 'vue'

const searchQuery = ref('')
const emit = defineEmits(['search'])

const search = (e) => {
  emit('search', e.target.value)
  console.log(e.target.value)
}
</script>

<template>
  <form @submit.prevent="submitSearch" role="search">
    <label class="sr-only" for="search-input">Digite sua busca:</label>
    <input
      type="search"
      id="search-input"
      v-model="searchQuery"
      @input="search"
      placeholder="Buscar operadoras..."
    />
  </form>
</template>

<style scoped>
form {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

input {
  padding: 0.5rem 1rem;
  font-size: 1rem;
  border: 0.1rem solid #ccc;
  border-radius: 0.3rem;
  width: 100%;
}

button {
  padding: 0.5em;
  border: none;
  background: rgb(34, 33, 33);
  color: white;
  border-radius: 0.3rem;
  cursor: pointer;
}

button:hover {
  background: rgba(34, 33, 33, 0.507);
}
</style>
