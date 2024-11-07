<script setup lang="ts">
import { ref, computed } from 'vue'
import { useStore } from '@/stores/store'
import { useRoute } from 'vue-router'
import ScoreHeader from '../components/ScoreHeader.vue'

const store = useStore()
const route = useRoute()

const chapterId = <string>route.params.id
const chapter = store.chapters.filter(c => c.id.toString() == chapterId)[0]

store.getChapterData(chapterId)

const chapterScore = computed(() => {
  if (chapter.id in store.finishedChapters) {
    return store.finishedChapters[chapter.id]
  } else {
    return store.chapterScore
  }
})

</script>

<template>
  <ScoreHeader :score="chapterScore" />
  <main>
    <div v-if="chapter.pages">
      <RouterView />
    </div>
    <div v-else>
      loading...
    </div>
  </main>
</template>

<style>

</style>
