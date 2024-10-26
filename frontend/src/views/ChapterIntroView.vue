<script setup lang="ts">
import { onMounted } from 'vue'
import { useStore } from '@/stores/store'
import { useRoute } from 'vue-router'

const store = useStore()
const route = useRoute()

const chapterId = route.params.id
const chapter = store.chapters.filter((c) => c.id.toString() == chapterId)[0]

onMounted(() => {
  // reset chapter score
  store.chapterScore = 0
})
</script>

<template>
  <main>
    <div>
      <h1>{{ chapter.title }}</h1>
      <div v-html="chapter.description"></div>
    </div>
    <div v-if="chapter.pages.length > 0" class="button-wrapper">
      <RouterLink :to="{ name: 'chapter-page', params: { id: $route.params.id, pageId: 1 } }" class="button">ZAČNI</RouterLink>
    </div>
  </main>
</template>

<style>
</style>
