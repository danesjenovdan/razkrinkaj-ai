<script setup lang="ts">
import { onMounted } from 'vue'
import { useStore } from '@/stores/store'
import { useRoute, useRouter } from 'vue-router'
import type { Page } from '@/types';

const store = useStore()
const route = useRoute()
const router = useRouter()

const chapterId = <string>route.params.id
const chapter = store.chapters.filter((c) => c.id.toString() == chapterId)[0]

onMounted(() => {
  if (!(chapter.id in store.finishedChapters)) {
    // mark this chapter as finished
    store.finishedChapters[chapter.id] = store.chapterScore
  }
})

</script>

<template>
  <main>
    <div>
      <div>
        <span>{{ chapter.title }}</span>
      </div>
      <h1>Poglavje zaključeno</h1>
      <p>Zbranih točk: {{ store.finishedChapters[chapter.id] }}</p>
      <p>Pravilni odgovori: </p>
      <p>Skupaj točk: {{ store.score }}</p>
    </div>
    <div class="button-wrapper">
      <button>Deli rezultat</button>
      <RouterLink :to="{ name: 'chapters-list' }">Nazaj na glavni menu</RouterLink>
    </div>
  </main>
</template>
