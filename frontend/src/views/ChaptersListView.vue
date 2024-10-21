<script setup lang="ts">
</script>

<template>
  <main>
    <h1>Izberi poglavje</h1>
    <RouterLink :to="{ name: 'chapter-intro', params: { id: 1 } }">Poglavje 1</RouterLink>
  </main>
</template>

<style>
/* @media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
} */
</style>
