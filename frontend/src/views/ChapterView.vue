<script setup lang="ts">
import { computed, onMounted } from "vue";
import { useRoute } from "vue-router";
import { useStore } from "@/stores/store.ts";
import ScoreHeader from "@/components/ScoreHeader.vue";
import TheLoader from "@/components/TheLoader.vue";
import PageFooter from "@/components/PageFooter.vue";

const route = useRoute();
const store = useStore();

let chapterId = -1;
if (route.params.id === undefined && route.params.slug !== undefined) {
  const slug = route.params.slug as string;
  chapterId = store.getChapterIdBySlug(slug);
} else if (route.params.id !== undefined) {
  const idString = route.params.id as string;
  chapterId = parseInt(idString, 10);
}

const chapter = computed(() => {
  if (Number.isNaN(chapterId) || chapterId < 0) {
    return null;
    // throw new Error('Invalid chapter id')
  }
  const c = store.chapters.get(chapterId);
  if (!c) {
    return null;
    // throw new Error('Chapter not found')
  }
  return c;
});

const hideHeaderScore = computed(() => {
  return route.name === "chapter-result";
});

const showBackButton = computed(() => {
  return route.name === "chapter-result";
});

const score = computed(() => {
  if (store.finishedChapters.has(chapterId)) {
    return store.score;
  }
  return store.score + store.currentChapterScore;
});

onMounted(() => {
  if (chapter.value) {
    store.setCurrentChapter(chapterId);
    store.initChapterData(chapterId);
    // clear just unlocked chapters for next time list is shown
    store.justUnlockedChapters = [];
  }
});
</script>

<template>
  <div class="bg-kvizle-color-8 header-container">
    <ScoreHeader
      :title="store.introductionTitle"
      :score="score"
      :hide-score="hideHeaderScore"
      :back-button="showBackButton"
    />
  </div>
  <div class="bg-kvizle-color-0 main-container">
    <main v-if="!chapter" :key="'no-chapter'" class="no-chapter">
      <h1>chapter not found</h1>
    </main>
    <RouterView
      v-else-if="
        store.currentChapterId >= 0 && store.chapterDataLoaded.get(chapterId)
      "
      :chapter="chapter"
    />
    <div v-else class="loader-container">
      <TheLoader />
    </div>
  </div>
  <PageFooter />
</template>

<style scoped lang="scss">
.main-container {
  height: 100%;
  min-height: 18rem;

  main.no-chapter {
    margin-top: 3rem;

    h1 {
      font-size: 1.5rem;
      font-weight: 600;
      text-align: center;
    }
  }

  .loader-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100%;
  }
}
</style>
