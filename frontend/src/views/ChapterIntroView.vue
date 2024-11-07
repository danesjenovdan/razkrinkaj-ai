<script setup lang="ts">
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
    <div>
      <h1>{{ chapter.title }}</h1>
      <div v-html="chapter.description"></div>
    </div>
    <div>
      <div>{{ firstPage.id }}</div>
      <h2>{{ firstPage.title }}</h2>
      <div>{{ firstPage.type }}</div>
      <div>{{ firstPage.text }}</div>
    </div>
    <!-- <div v-if="chapter.pages.length > 0" class="button-wrapper">
      <RouterLink
        :to="{
          name: 'chapter-page',
          params: { id: $route.params.id, pageId: 1 },
        }"
        class="button"
        >ZAČNI</RouterLink
      >
    </div> -->
  </main>
</template>

<style></style>
