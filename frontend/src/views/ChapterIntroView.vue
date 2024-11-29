<script setup lang="ts">
import type { Chapter } from '@/types'
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import RichText from '@/components/RichText.vue'
import ThumbnailImage from '@/components/ThumbnailImage.vue'
import { preloadPageImages } from '@/utils/image'
import { computed, onMounted } from 'vue'

const props = defineProps<{ chapter: Chapter }>()

const firstPage = computed(() => {
  const fp = props.chapter.pages?.[0]
  if (!fp || fp.type !== 'text') {
    throw new Error('First page is not a text page')
  }
  return fp
})

const nextPage = computed(() => {
  return props.chapter.pages?.[1]
})

onMounted(() => {
  if (nextPage.value) {
    preloadPageImages(nextPage.value)
  }
})
</script>

<template>
  <main>
    <div class="chapter-info">
      <ThumbnailImage v-if="chapter.image" :image="chapter.image" />
      <h1>{{ chapter.title }}</h1>
      <div v-html="chapter.description" class="description"></div>
    </div>
    <div class="page-content">
      <RichText :title="firstPage.title" :content="firstPage.text" />
      <ButtonPrimary
        class="button"
        :buttonText="firstPage.button_text"
        :link="{ name: 'chapter-page', params: { pageIndex: 1 } }"
        icon="arrow"
      />
    </div>
  </main>
</template>

<style scoped lang="scss">
main {
  padding-bottom: 2rem;

  @media (min-width: 768px) {
    padding-bottom: 3.38rem;
  }

  .chapter-info {
    margin-inline: calc(var(--page-gutter) * -1);
    padding-inline: var(--page-gutter);
    padding-block: 2.4rem;
    background: var(--color-bg-accent);
    text-align: center;

    .thumbnail-image {
      width: 5rem;
      height: 5rem;
      margin-inline: auto;
      border-radius: 3px;

      @media (min-width: 768px) {
        width: 6.8125rem;
        height: 6.8125rem;
      }

      :deep(img) {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
      }
    }

    h1 {
      margin-top: 1.1rem;
      margin-bottom: 0.5rem;
      font-family: var(--font-family-heading);
      font-size: 1.5rem;
      font-weight: 700;

      @media (min-width: 768px) {
        font-size: 2.25rem;
        margin-top: 1.8rem;
      }
    }

    .description {
      font-size: 1.125rem;

      @media (min-width: 768px) {
        font-size: 1.3125rem;
      }
    }
  }
}
</style>
