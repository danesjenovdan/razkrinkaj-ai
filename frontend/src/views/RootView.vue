<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useStore } from '@/stores/store'
import { fixLocalUrl } from '@/utils/image'
import TheLoader from '@/components/TheLoader.vue'

const store = useStore()
store.loadLocalStorage()
store.initHomeData()

const is_iOS = ref(false)

function check_iOS() {
  // detects most iOS devices and older iPads on iPadOS < 13
  is_iOS.value = /iPad|iPhone|iPod/.test(navigator.userAgent)

  if (!is_iOS.value) {
    // newer iPads on iPadOS >= 13 pretend to be macs
    if (navigator.platform === 'MacIntel') {
      // check if primary pointer is coarse (touch)
      const pointerCoarse = window.matchMedia('(pointer: coarse)').matches
      if (pointerCoarse) {
        is_iOS.value = true
      }
    }
  }
}

onMounted(() => {
  check_iOS()

  if (is_iOS.value) {
    document.body.classList.add('is-ios')
  }

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
