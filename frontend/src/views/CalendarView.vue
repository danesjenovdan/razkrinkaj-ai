<script setup lang="ts">
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStore } from '@/stores/store'
import ScoreHeader from '@/components/ScoreHeader.vue'
import DaysToElection from '@/components/DaysToElection.vue'
import ConsentPrompt from '@/components/ConsentPrompt.vue'
import CalendarDay from '@/components/CalendarDay.vue'
import PageFooter from '@/components/PageFooter.vue'

const router = useRouter()
const route = useRoute()
const store = useStore()

function onResetClick() {
  if (
    window.confirm(
      'Ali ste prepričani, da želite začeti znova? To bo izbrisalo vse odgovore.',
    )
  ) {
    store.clearAllProgress()
    router.push({ name: 'intro' })
  }
}

const scrollToMore = () => {
  document
    .querySelector('a[name="more"]')
    ?.scrollIntoView({ behavior: 'smooth' })
}

onMounted(() => {
  store.clearCurrentChapter()
  store.ensureFinishedChaptersSent()
})
</script>

<template>
  <div class="bg-kvizle-color-0">
    <ScoreHeader
      :title="store.introductionTitle"
      :description="store.introductionDescription"
      :score="store.score"
    />
    <main>
      <div class="page-gutter">
        <DaysToElection />
        <ConsentPrompt />
        <div class="calendar">
          <CalendarDay
            v-for="[id, chapter] in store.chapters"
            :key="id"
            :chapter="chapter"
          />
        </div>
      </div>
    </main>
  </div>
  <PageFooter />
</template>

<style scoped lang="scss">
main {
  .calendar {
    display: grid;
    align-content: start;
    justify-content: center;
    grid-template-columns: repeat(auto-fit, 8.5625rem);
    gap: 1.25rem;
    width: 100%;
    margin-top: 2rem;
    max-width: min(65rem, 100%);
    margin-inline: auto;
    margin-bottom: 8.125rem;
  }
}
</style>
