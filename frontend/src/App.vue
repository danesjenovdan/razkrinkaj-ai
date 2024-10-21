<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <!-- <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" /> -->
    <!-- <nav>
      <RouterLink to="/">Intro</RouterLink>
      <RouterLink :to="{ name: 'chapters-list'}">Chapters List</RouterLink>
    </nav> -->
  </header>

  <RouterView />
</template>

<style scoped>


nav a.router-link-exact-active {
}

nav a.router-link-exact-active:hover {
}

nav a {
}

</style>
