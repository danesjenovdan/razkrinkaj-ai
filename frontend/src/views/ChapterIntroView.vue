<script setup lang="ts">
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import RichText from '@/components/RichText.vue'
import type { Chapter } from '@/types'
import { computed } from 'vue'

const props = defineProps<{ chapter: Chapter }>()

const firstPage = computed(() => {
  const fp = props.chapter.pages?.[0]
  if (!fp || fp.type !== 'text') {
    throw new Error('First page is not a text page')
  }
  return fp
})
</script>

<template>
  <main>
    <div class="chapter-info">
      <img
        v-if="chapter.image"
        :src="chapter.image.url"
        :alt="chapter.image.alt"
        :width="chapter.image.width"
        :height="chapter.image.height"
      />
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
  padding-bottom: 3.5rem;

  .chapter-info {
    margin-inline: calc(var(--page-gutter) * -1);
    padding-inline: var(--page-gutter);
    padding-block: 2.4rem;
    background: var(--color-bg-accent);
    text-align: center;

    img {
      width: 5rem;
      height: 5rem;
      margin-inline: auto;
      object-fit: cover;
      object-position: center;
      border-radius: 3px;
    }

    h1 {
      margin-top: 1.1rem;
      margin-bottom: 0.25rem;
      font-family: var(--font-family-heading);
      font-size: 1.3125rem;
      font-weight: 700;
    }

    .description {
      font-size: 0.875rem;
    }
  }
}
</style>
