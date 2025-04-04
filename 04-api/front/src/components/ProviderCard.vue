<script setup lang="ts">
import { defineProps } from 'vue'
import type { IProvider } from '../models/IProvider'

defineProps<{ provider: IProvider }>()
</script>

<template>
  <div class="card">
    <h2 class="razao-social">{{ provider.razao_social }}</h2>
    <div class="data">
      <div class="card__sub-section">
        <p>Nome Fantasia: {{ provider.nome_fantasia }}</p>
        <div class="card__sub-section__row">
          <p>Modalidade: {{ provider.modalidade }}</p>
          <p>CNPJ: {{ provider.cnpj }}</p>
          <p>Região: {{ provider.regiao_de_comercializacao }}</p>
        </div>
        <div class="card__sub-section__row">
          <p>Registro ANS: {{ provider.registro_ans }}</p>
          <p>Data do Registro: {{ provider.data_registro_ans }}</p>
        </div>
      </div>
      <div class="card__sub-section">
        <p class="card__sub-section__title">Endereço</p>
        <div class="card__sub-section__row">
          <p>Loradouro: {{ provider.logradouro }}</p>
          <p>Número: {{ provider.numero }}</p>
          <p>Complemento: {{ provider.complemento }}</p>
        </div>
        <div class="card__sub-section__row">
          <p>Bairro: {{ provider.bairro }}</p>
          <p>Cidade: {{ provider.cidade }}</p>
          <p>UF: {{ provider.uf }}</p>
          <p>CEP: {{ provider.cep }}</p>
        </div>
      </div>
      <div class="card__sub-section">
        <p class="card__sub-section__title">Contato</p>
        <div class="card__sub-section__row">
          <p>
            Telefone: <span v-if="provider.telefone && provider.ddd">({{ provider.ddd }})</span>
            {{ provider.telefone }}
          </p>
          <p>E-mail: {{ provider.endereco_eletronico }}</p>
        </div>
        <p>
          Fax: <span v-if="provider.fax && provider.ddd">({{ provider.ddd }})</span>
          {{ provider.fax }}
        </p>
      </div>
      <div class="card__sub-section">
        <p class="card__sub-section__title">Representante</p>
        <p>{{ provider.representante }} - {{ provider.cargo_representante }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.card {
  border: 0.1rem solid rgba(0, 0, 0, 0.356);
  border-radius: 0.3rem;
  padding: 1rem;
  display: grid;
  gap: 0.5rem;
}

.data {
  display: grid;
  gap: 1rem;
}

h2 {
  font-size: 1.3rem;
}

.card__sub-section {
  display: grid;
  gap: 0.2rem;
}

.card__sub-section__row {
  display: flex;
  gap: 5rem;
}

.card__sub-section__title {
  border-bottom: 0.1rem rgba(0, 0, 0, 0.178) solid;
  font-size: 1.1rem;
  margin-block-end: 0.2rem;
}

@media (max-width: 980px) {
  .card__sub-section__row {
    display: grid;
    gap: 0.2rem;
  }
}
</style>
