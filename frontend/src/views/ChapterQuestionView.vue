<script setup lang="ts">
</script>

<template>
  <main>
    <div>
      Slika
      <div>
        <button>Resnično</button>
        <button>Umetno</button>
      </div>
    </div>
    <div class="button-wrapper">
      <RouterLink :to="{ name: 'chapter-result', params: { id: $route.params.id } }">Nadaljuj</RouterLink>
    </div>
  </main>
</template>
