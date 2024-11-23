<script setup lang="ts">
import { onMounted } from 'vue'
import { useStore } from '@/stores/store'
import { fixLocalUrl } from '@/utils/image'
import TheLoader from '@/components/TheLoader.vue'

const store = useStore()
store.loadLocalStorage()
store.initHomeData()

onMounted(() => {
  document.addEventListener(
    'error',
    event => {
      if (event.target instanceof HTMLImageElement) {
        const img = event.target
        const src = img.getAttribute('src')
        if (src) {
          const url = fixLocalUrl(src)
          if (url !== src) {
            img.src = url
          }
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
  height: 100%;
}
</style>
