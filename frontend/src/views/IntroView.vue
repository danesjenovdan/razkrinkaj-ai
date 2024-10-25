<script setup lang="ts">
import { ref } from 'vue'
import { useStore } from '@/stores/store'

const store = useStore()
store.initializeStore()

</script>

<template>
  <main>
    <div>
      <h1>{{ store.introduction_title }}</h1>
      <div v-html="store.introduction_description"></div>
    </div>
    <div class="button-wrapper">
      <RouterLink :to="{ name: 'chapters-list' }" class="button">{{ store.introduction_button_text }}</RouterLink>
    </div>
  </main>
</template>
