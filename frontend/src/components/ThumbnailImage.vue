<script setup lang="ts">
import type { ImageDescription } from '@/types'
import { onMounted, ref } from 'vue'
import { fixLocalUrl, preloadImageUrl } from '@/utils/image'

const props = defineProps<{ image: ImageDescription }>()

const isThumbnail = ref(!props.image.preloaded)

const isSVG = ref(!!props.image.svg)
const svgData = ref<string | null>(null)

function fetchSVG() {
  if (isSVG.value && !svgData.value) {
    fetch(fixLocalUrl(props.image.url))
      .then(response => response.text())
      .then(data => {
        svgData.value = data
      })
  }
}

onMounted(() => {
  if (!props.image.preloaded) {
    preloadImageUrl(props.image.url).then(() => {
      isThumbnail.value = false
    })
  }

  fetchSVG()
})
</script>

<template>
  <div class="thumbnail-image">
    <div v-if="isSVG && svgData" v-html="svgData"></div>
    <img
      v-else
      :class="{ 'is-thumbnail': isThumbnail }"
      :src="isThumbnail ? image.thumbnail_url : image.url"
      :alt="image.alt"
      :width="image.width"
      :height="image.height"
    />
  </div>
</template>

<style scoped lang="scss">
.thumbnail-image {
  overflow: hidden;

  img,
  svg {
    display: block;
    width: 100%;
    height: auto;

    &.is-thumbnail {
      filter: blur(3px);
    }
  }
}
</style>
