<script setup lang="ts">
import Header from '../components/Header.vue'
import ChapterElement from '../components/ChapterElement.vue'
import { useChaptersStore } from '@/stores/chapters'
import { useResultsStore } from '@/stores/results'

const chapters = useChaptersStore()
const results = useResultsStore()

</script>

<template>
  <Header :score="results.score" />
  <main>
    <h1>Izberi poglavje</h1>
    <ChapterElement v-for="chapter in chapters.chapters" :chapter="chapter"></ChapterElement>
  </main>
</template>

<style>

</style>
