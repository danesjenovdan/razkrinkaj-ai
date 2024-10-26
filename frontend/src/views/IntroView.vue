<script setup lang="ts">
import { ref } from 'vue'
import { useStore } from '@/stores/store'

const store = useStore()
store.initializeStore()

</script>

<template>
  <main>
    <div>
      <h1>{{ store.introductionTitle }}</h1>
      <div v-html="store.introductionDescription"></div>
    </div>
    <div class="button-wrapper">
      <RouterLink :to="{ name: 'chapters-list' }" class="button">{{ store.introductionButtonText }}</RouterLink>
    </div>
  </main>
</template>
