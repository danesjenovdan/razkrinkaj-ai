<script setup lang="ts">
import { ref } from 'vue'
import { useIntroductionStore } from '@/stores/introduction'

const store = useIntroductionStore()

</script>

<template>
  <main>
    <div>
      <h1>{{ store.title }}</h1>
      {{ store.introduction }}
    </div>
    <div class="button-wrapper">
      <RouterLink :to="{ name: 'chapters-list' }" class="button">ZAČNI</RouterLink>
    </div>
  </main>
</template>
