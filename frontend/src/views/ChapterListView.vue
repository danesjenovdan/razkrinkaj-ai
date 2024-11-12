<script setup lang="ts">
import { useStore } from '@/stores/store'
import ScoreHeader from '@/components/ScoreHeader.vue'
import ChapterElement from '@/components/ChapterElement.vue'

const store = useStore()
</script>

<template>
  <ScoreHeader :title="store.introductionTitle" :score="store.score" />
  <main>
    <h1>Izberi poglavje</h1>
    <div class="chapters">
      <ChapterElement
        v-for="[id, chapter] in store.chapters"
        :key="id"
        :chapter="chapter"
      />
    </div>
  </main>
</template>

<style scoped lang="scss">
main {
  padding-bottom: 3.5rem;

  h1 {
    margin: 0;
    padding-block: 1.75rem;
    font-family: var(--font-family-heading);
    font-size: 1.3125rem;
    text-align: center;
    text-transform: uppercase;
  }

  .chapters {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
  }
}
</style>
