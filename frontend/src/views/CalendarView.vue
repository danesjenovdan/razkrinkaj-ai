<script setup lang="ts">
import { computed, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "@/stores/store.ts";
import ScoreHeader from "@/components/ScoreHeader.vue";
import DaysToElection from "@/components/DaysToElection.vue";
import CalendarDay from "@/components/CalendarDay.vue";
import CalendarElectionDay from "@/components/CalendarElectionDay.vue";
import PageFooter from "@/components/PageFooter.vue";

const store = useStore();
const route = useRoute();

const forceUnlock = computed(() => {
  return route.query.forceUnlock === "true";
});

onMounted(() => {
  store.clearCurrentChapter();
  store.ensureFinishedChaptersSent();
});
</script>

<template>
  <div class="bg-kvizle-color-0">
    <ScoreHeader
      :title="store.introductionTitle"
      :description="store.introductionDescription"
      :score="store.score"
    />
  </div>
  <div class="bg-kvizle-color-0">
    <main>
      <div class="page-gutter">
        <DaysToElection />
        <div class="calendar">
          <CalendarDay
            v-for="[id, chapter] in store.chapters"
            :key="id"
            :chapter="chapter"
            :force-unlock="forceUnlock"
          />
          <CalendarElectionDay />
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
    justify-content: center;
    grid-template-columns: repeat(auto-fit, 9.5rem);
    gap: 1.5rem;
    width: min(100%, 65rem);
    margin-inline: auto;
    margin-top: 2rem;
    margin-bottom: 8.125rem;

    @media (max-width: 576px) {
      grid-template-columns: repeat(2, 1fr);
      width: min(100%, 21rem);
    }
  }
}
</style>
