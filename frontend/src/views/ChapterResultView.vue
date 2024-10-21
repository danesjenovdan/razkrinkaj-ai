<script setup lang="ts">
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <div>
      <h1>Razkrinkaj.AI</h1>
      <p>Besedilo</p>
      <p>Besedilo</p>
    </div>
    <div class="button-wrapper">
      <RouterLink :to="{ name: 'chapters-list' }">Nazaj na glavni menu</RouterLink>
    </div>
  </main>
</template>
