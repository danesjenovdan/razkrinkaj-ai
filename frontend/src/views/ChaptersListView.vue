<script setup lang="ts">
import Header from '../components/Header.vue'
import ChapterElement from '../components/ChapterElement.vue'
import { useStore } from '@/stores/store'

const store = useStore()
store.initializeStore()

</script>

<template>
  <Header :score="store.score" />
  <main>
    <h1>Izberi poglavje</h1>
    <ChapterElement v-for="chapter in store.chapters" :chapter="chapter"></ChapterElement>
  </main>
</template>

<style>

</style>
