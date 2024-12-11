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

function calculateSizes() {
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
}

function onZoomClick() {
  if (isZoomed.value) {
    isZoomed.value = false
    document.body.style.overflow = ''
    window.history.go(-1)
  } else {
    calculateSizes()
    isZoomed.value = true
    document.body.style.overflow = 'hidden'
    window.history.pushState(null, '', '#zoomed')
  }
}

function onPopState() {
  isZoomed.value = false
  document.body.style.overflow = ''
}

function onResize() {
  if (isZoomed.value) {
    calculateSizes()
  }
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
  window.addEventListener('resize', onResize)
  window.addEventListener('popstate', onPopState)
  preloadImageUrl(props.image.original_url)
})

onBeforeUnmount(() => {
  document.body.style.overflow = ''
  window.removeEventListener('resize', onResize)
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
      <img
        v-if="!isZoomed"
        src="data:image/png;base64,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"
        alt=""
      />
      <span v-else>&times;</span>
    </button>
  </div>
</template>

<style scoped lang="scss">
.zoomable-image {
  position: relative;

  --_button-offset: 0.75rem;
  --_button-padding: 0.125rem;
  --_button-icon-size: 1.375rem;

  @media (min-width: 768px) {
    --_button-offset: 1rem;
  }

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

    @media (min-width: 768px) {
      padding: 0.5rem;
    }
  }

  button {
    display: flex;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: var(--_button-offset);
    left: var(--_button-offset);
    z-index: 1001;
    padding: var(--_button-padding);
    background: var(--color-bg-white);
    border: 0.5px solid #000;
    border-radius: 3px;
    cursor: pointer;

    @at-root body:not(.is-ios) &:hover {
      background: #fefffb;
      box-shadow:
        0px 0px 6px 0px #cbd844 inset,
        0px 0px 7px -1px #f3ff6f;
    }

    svg,
    img {
      width: var(--_button-icon-size);
      height: var(--_button-icon-size);
    }

    span {
      display: block;
      width: var(--_button-icon-size);
      height: var(--_button-icon-size);
      font-size: calc(var(--_button-icon-size) * 1.75);
      line-height: var(--_button-icon-size);
    }
  }

  &.zoomed {
    button {
      bottom: auto;
      top: var(--_button-offset);
    }
  }
}
</style>
