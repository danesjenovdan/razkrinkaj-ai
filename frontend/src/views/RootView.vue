<script setup lang="ts">
import { onMounted } from 'vue'
import { useStore } from '@/stores/store'
import TheLoader from '@/components/TheLoader.vue'

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
  <div v-else class="loader-container">
    <TheLoader />
  </div>
</template>

<style scoped lang="scss">
.loader-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
</style>
