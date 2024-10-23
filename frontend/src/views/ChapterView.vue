<script setup lang="ts">
import { ref } from 'vue'
import { useResultsStore } from '@/stores/results'

import Header from '../components/Header.vue'

const results = useResultsStore()

</script>

<template>
  <Header :score="results.chapterScore" />
  <main>
    <RouterView />
  </main>
</template>

<style>

</style>
