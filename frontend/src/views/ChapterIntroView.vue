<script setup lang="ts">
</script>

<template>
  <main>
    <div>
      <h1>Uvod v poglavje {{ $route.params.id }}</h1>
      <p>Besedilo</p>
    </div>
    <div class="button-wrapper">
      <RouterLink :to="{ name: 'chapter-question', params: { id: $route.params.id, questionId: 1 } }">ZAČNI</RouterLink>
    </div>
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
