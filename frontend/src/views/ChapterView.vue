<script setup lang="ts">
import { ref } from 'vue'
import { useStore } from '@/stores/store'
import { useRoute } from 'vue-router'
import Header from '../components/Header.vue'

const store = useStore()
const route = useRoute()

const chapterId = <string>route.params.id
const chapter = store.chapters.filter(c => c.id.toString() == chapterId)[0]

store.getChapterData(chapterId)

</script>

<template>
  <Header :score="store.chapterScore" />
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
