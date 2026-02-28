<script setup lang="ts">
import type { Chapter } from "@/types";
import { computed } from "vue";
import { useStore } from "@/stores/store.ts";

const props = defineProps<{ title: string; chapter: Chapter }>();

const store = useStore();

const answers = computed(() => {
  const pageIds = props.chapter.pages?.map((p) => p.id) || [];
  let chapterData;
  if (store.finishedChapters.has(props.chapter.id)) {
    chapterData = store.finishedChapters.get(props.chapter.id)!;
  } else if (store.inProgressChapters.has(props.chapter.id)) {
    chapterData = store.inProgressChapters.get(props.chapter.id)!;
  }
  if (!chapterData) {
    return [null, null, null];
  }
  let a1 = null;
  let a2 = null;
  let a3 = null;
  if (pageIds[0]) {
    a1 = chapterData.answers.get(pageIds[0]) || null;
  }
  if (pageIds[1]) {
    a2 = chapterData.answers.get(pageIds[1]) || null;
  }
  if (pageIds[2]) {
    a3 = chapterData.answers.get(pageIds[2]) || null;
  }
  return [a1, a2, a3];
});
</script>

<template>
  <div class="chapter-title">
    <h1>{{ title }}</h1>
    <div class="answer-icons">
      <template v-if="answers[0]">
        <div v-if="answers[0].correct" class="answer-icon">
          <img src="/check.svg" alt="" />
        </div>
        <div v-else class="answer-icon"><img src="/cross.svg" alt="" /></div>
      </template>
      <div v-else class="answer-icon"><img src="/question.svg" alt="" /></div>
      <template v-if="answers[1]">
        <div v-if="answers[1].correct" class="answer-icon">
          <img src="/check.svg" alt="" />
        </div>
        <div v-else class="answer-icon"><img src="/cross.svg" alt="" /></div>
      </template>
      <div v-else class="answer-icon"><img src="/question.svg" alt="" /></div>
      <template v-if="answers[2]">
        <div v-if="answers[2].correct" class="answer-icon">
          <img src="/check.svg" alt="" />
        </div>
        <div v-else class="answer-icon"><img src="/cross.svg" alt="" /></div>
      </template>
      <div v-else class="answer-icon"><img src="/question.svg" alt="" /></div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.chapter-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  max-width: 38rem;
  margin-inline: auto;
  padding-block: 1.3125rem;
  border-bottom: 1px solid var(--kvizle-color-8);

  h1 {
    margin-bottom: 0;
    font-size: 1rem;
    font-weight: 400;
  }

  .answer-icons {
    display: flex;
    gap: 0.5rem;
    background: var(--kvizle-color-0);

    .answer-icon {
      display: grid;
      width: 3rem;
      aspect-ratio: 1;
      border: 2px solid var(--kvizle-color-5);

      @media (max-width: 576px) {
        width: 2.5rem;
      }

      img {
        width: 100%;
        height: 100%;
      }
    }
  }
}
</style>
