<script setup lang="ts">
import { onMounted } from 'vue'
import { useStore } from '@/stores/store'
import ScoreHeader from '@/components/ScoreHeader.vue'
import ChapterElement from '@/components/ChapterElement.vue'
import PageFooter from '@/components/PageFooter.vue'

const store = useStore()

onMounted(() => {
  store.clearCurrentChapter()
})
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
  <PageFooter />
</template>

<style scoped lang="scss">
main {
  padding-bottom: 2rem;

  @media (min-width: 768px) {
    padding-bottom: 3.38rem;
  }

  h1 {
    margin: 0;
    padding-block: 1.9rem 1.5rem;
    font-family: var(--font-family-heading);
    font-size: 1.5rem;
    text-align: center;
    text-transform: uppercase;

    @media (min-width: 768px) {
      padding-top: 3rem;
      font-size: 2.25rem;
    }
  }

  .chapters {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;

    @media (min-width: 768px) {
      gap: 0.875rem;
    }
  }
}
</style>
