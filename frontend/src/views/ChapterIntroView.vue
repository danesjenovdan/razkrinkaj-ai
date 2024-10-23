<script setup lang="ts">
</script>

<template>
  <main>
    <div>
      <h1>Uvod v poglavje {{ $route.params.id }}</h1>
      <p>Besedilo</p>
    </div>
    <div class="button-wrapper">
      <RouterLink :to="{ name: 'chapter-question', params: { id: $route.params.id, questionId: 1 } }" class="button">ZAČNI</RouterLink>
    </div>
  </main>
</template>

<style>
</style>
