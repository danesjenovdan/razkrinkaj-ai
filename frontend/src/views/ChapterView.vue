<script setup lang="ts">
import { computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useStore } from '@/stores/store'
import ScoreHeader from '@/components/ScoreHeader.vue'
import TheLoader from '@/components/TheLoader.vue'

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

const score = computed(() => {
  if (store.finishedChapters.has(chapterId)) {
    return store.score
  }
  return store.score + store.currentChapterScore
})

onMounted(() => {
  store.setCurrentChapter(chapterId)
  // clear just unlocked chapters for next time list is shown
  store.justUnlockedChapters = []
})

store.initChapterData(chapterId)
</script>

<template>
  <ScoreHeader
    v-if="showHeader"
    :title="store.introductionTitle"
    :score="score"
  />
  <RouterView v-if="store.chapterDataLoaded.get(chapterId)" :chapter />
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
