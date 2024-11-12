<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useStore } from '@/stores/store'
import ScoreHeader from '@/components/ScoreHeader.vue'

const route = useRoute()
const store = useStore()

const idString = route.params.id as string
const chapterId = parseInt(idString, 10)
const chapter = store.chapters.get(chapterId)

if (Number.isNaN(chapterId)) {
  throw new Error('Invalid chapter id')
}

const showHeader = computed(() => {
  return route.name !== 'chapter-result'
})

store.initChapterData(chapterId)
</script>

<template>
  <ScoreHeader
    v-if="showHeader"
    :title="store.introductionTitle"
    :score="store.score"
  />
  <main>
    <RouterView v-if="store.chapterDataLoaded.get(chapterId)" :chapter />
    <div v-else>chapter loading...</div>
  </main>
</template>
