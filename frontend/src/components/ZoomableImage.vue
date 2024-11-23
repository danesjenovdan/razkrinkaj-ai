<script setup lang="ts">
import type { ImageDescription } from '@/types'
import { onBeforeUnmount, onMounted, ref, watch } from 'vue'
import PinchScrollZoom, {
  type PinchScrollZoomExposed,
} from '@coddicat/vue-pinch-scroll-zoom'
import { preloadImageUrl } from '@/utils/image'

const props = defineProps<{ image: ImageDescription }>()

const zoomer = ref<PinchScrollZoomExposed>()
const isZoomed = ref(false)
const pageWidth = ref(0)
const pageHeight = ref(0)
const zoomedImgWidth = ref(0)
const zoomedImgHeight = ref(0)

function onZoomClick() {
  if (isZoomed.value) {
    isZoomed.value = false
    document.body.style.overflow = ''
    window.history.go(-1)
  } else {
    pageWidth.value = window.innerWidth
    pageHeight.value = window.innerHeight
    zoomedImgWidth.value = pageWidth.value
    zoomedImgHeight.value =
      pageWidth.value * (props.image.height / props.image.width)
    if (pageHeight.value < zoomedImgHeight.value) {
      zoomedImgHeight.value = pageHeight.value
      zoomedImgWidth.value =
        pageHeight.value * (props.image.width / props.image.height)
    }

    isZoomed.value = true
    document.body.style.overflow = 'hidden'
    window.history.pushState(null, '', '#zoomed')
  }
}

function onPopState() {
  isZoomed.value = false
  document.body.style.overflow = ''
}

watch(
  () => props.image,
  () => {
    preloadImageUrl(props.image.original_url)
  },
)

onMounted(() => {
  if (window.location.hash === '#zoomed') {
    window.history.replaceState(
      null,
      '',
      window.location.pathname + window.location.search,
    )
  }
  window.addEventListener('popstate', onPopState)
  preloadImageUrl(props.image.original_url)
})

onBeforeUnmount(() => {
  document.body.style.overflow = ''
  window.removeEventListener('popstate', onPopState)
})
</script>

<template>
  <div :class="{ 'zoomable-image': true, zoomed: isZoomed }">
    <img
      class="normal-image"
      :src="image.url"
      :alt="image.alt"
      :width="image.width"
      :height="image.height"
    />
    <PinchScrollZoom
      v-if="isZoomed"
      ref="zoomer"
      centered
      :width="pageWidth"
      :height="pageHeight"
      :content-width="zoomedImgWidth"
      :content-height="zoomedImgHeight"
      :min-scale="1"
      :max-scale="5"
    >
      <img
        :src="image.original_url"
        :alt="image.alt"
        :width="zoomedImgWidth"
        :height="zoomedImgHeight"
        :style="{
          width: `${zoomedImgWidth}px`,
          height: `${zoomedImgHeight}px`,
        }"
        draggable="false"
      />
    </PinchScrollZoom>
    <button type="button" @click="onZoomClick">
      <svg
        v-if="!isZoomed"
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 12 12"
      >
        <path
          fill="#000"
          d="M5.174 9.73c.98 0 1.884-.315 2.626-.846l2.272 2.293a.754.754 0 0 0 1.071 0 .765.765 0 0 0 0-1.078L8.872 7.807a4.557 4.557 0 0 0 .841-2.642C9.713 2.644 7.68.6 5.173.6 2.668.6.636 2.644.636 5.165c0 2.522 2.032 4.565 4.539 4.565Zm0-7.608A3.038 3.038 0 0 1 8.2 5.165c0 .632-.194 1.24-.561 1.759l-.298.42-.418.3a2.992 2.992 0 0 1-1.749.565c-1.668 0-3.026-1.366-3.026-3.044s1.357-3.043 3.026-3.043Z"
        />
      </svg>
      <span v-else>&times;</span>
    </button>
  </div>
</template>

<style scoped lang="scss">
.zoomable-image {
  position: relative;

  &.zoomed {
    position: static;
  }

  .pinch-scroll-zoom {
    position: fixed;
    inset: 0;
    z-index: 1000;
    background: #000;

    img {
      width: initial;
      height: initial;
      max-width: initial;
    }
  }

  img.normal-image {
    display: block;
    width: 100%;
    height: auto;
    padding: 0.25rem;
    border-radius: 3px;
    border: 0.5px solid #000;
    background: var(--color-bg-white);
  }

  button {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    bottom: 0.5rem;
    right: 0.5rem;
    z-index: 1001;
    padding: 0.25rem;
    background: var(--color-bg-white);
    border: 0.5px solid #000;
    border-radius: 3px;
    cursor: pointer;

    svg {
      width: 0.75rem;
      height: 0.75rem;
    }

    span {
      display: block;
      width: 1.5rem;
      height: 1.5rem;
      font-size: 1.5rem;
      line-height: 1;
    }
  }
}
</style>
