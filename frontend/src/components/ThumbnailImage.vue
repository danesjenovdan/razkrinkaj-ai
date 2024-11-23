<script setup lang="ts">
import type { ImageDescription } from '@/types'
import { onMounted, ref } from 'vue'
import { preloadImageUrl } from '@/utils/image'

const props = defineProps<{ image: ImageDescription }>()

const isThumbnail = ref(!props.image.preloaded)

onMounted(() => {
  if (!props.image.preloaded) {
    preloadImageUrl(props.image.url).then(() => {
      isThumbnail.value = false
    })
  }
})
</script>

<template>
  <div class="thumbnail-image">
    <img
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

  img {
    display: block;
    width: 100%;
    height: auto;

    &.is-thumbnail {
      filter: blur(3px);
    }
  }
}
</style>
