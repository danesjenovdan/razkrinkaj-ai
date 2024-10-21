<script setup lang="ts">
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <div>
      <h1>Razkrinkaj.AI</h1>
      <p>Uvodno</p>
      <p>Besedilo</p>
    </div>
    <div class="button-wrapper">
      <RouterLink :to="{ name: 'chapters-list' }">ZAČNI</RouterLink>
    </div>
  </main>
</template>
