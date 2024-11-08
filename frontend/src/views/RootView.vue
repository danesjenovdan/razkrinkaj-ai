<script setup lang="ts">
import { useStore } from '@/stores/store'
import { onMounted } from 'vue'

const store = useStore()
store.initHomeData()

onMounted(() => {
  document.addEventListener(
    'error',
    event => {
      if (event.target instanceof HTMLImageElement) {
        const img = event.target
        if (!img.getAttribute('src')?.startsWith('http')) {
          img.src = `${store.apiUrl}${img.getAttribute('src')}`
        }
      }
    },
    true,
  )
})
</script>

<template>
  <RouterView v-if="store.homeDataLoaded" />
  <div v-else>root loading...</div>
</template>
