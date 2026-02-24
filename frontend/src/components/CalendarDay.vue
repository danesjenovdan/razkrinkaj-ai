<script setup lang="ts">
import type { Chapter } from "@/types";
import { computed, onMounted } from "vue";
import { useStore } from "@/stores/store.ts";
import { preloadPageImages } from "@/utils/image.ts";
import LockIcon from "./LockIcon.vue";
import QuestionIcon from "./QuestionIcon.vue";
// import { slugifyDot } from "@/utils/stringify.ts";

const props = defineProps<{
  chapter: Chapter;
}>();

const store = useStore();

const chapterDate = computed(() => {
  const dateParts = props.chapter.title.split(".").map(Number);
  let year = dateParts[2];
  if (Number.isNaN(year) || year === 0) {
    year = 2026;
  } else if (year < 100) {
    year += 2000;
  }
  return new Date(year, dateParts[1] - 1, dateParts[0]);
});

// const chapterSlug = computed(() => {
//   return slugifyDot(props.chapter.title);
// });

const isFinished = computed(() => store.finishedChapters.has(props.chapter.id));
const isLocked = computed(() => {
  const date = chapterDate.value;
  const now = Date.now();
  return now < date.getTime();
});
const isToday = computed(() => {
  const date = chapterDate.value;
  const today = new Date();
  return (
    date.getDate() === today.getDate() &&
    date.getMonth() === today.getMonth() &&
    date.getFullYear() === today.getFullYear()
  );
});
const isTomorrow = computed(() => {
  const date = chapterDate.value;
  const tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  return (
    date.getDate() === tomorrow.getDate() &&
    date.getMonth() === tomorrow.getMonth() &&
    date.getFullYear() === tomorrow.getFullYear()
  );
});

const didAnswerCorrectly = computed<boolean | null>(() => {
  if (store.finishedChapters.has(props.chapter.id)) {
    const chapterData = store.finishedChapters.get(props.chapter.id)!;
    const answers = Array.from(chapterData.answers.values());
    return answers.every((answer) => answer.correct);
  } else if (store.inProgressChapters.has(props.chapter.id)) {
    const chapterData = store.inProgressChapters.get(props.chapter.id)!;
    const answers = Array.from(chapterData.answers.values());
    return answers.every((answer) => answer.correct);
  }
  return null;
});

const isHidden = computed(() => {
  if (props.chapter.is_feedback && (isLocked.value || isFinished.value)) {
    return true;
  }
  return false;
});

const componentName = computed(() => (!isLocked.value ? "RouterLink" : "span"));

onMounted(() => {
  if (!isLocked.value) {
    store.initChapterData(props.chapter.id).then(() => {
      const firstPage = props.chapter.pages?.[0];
      if (firstPage) {
        preloadPageImages(firstPage);
      }
    });
  }
});
</script>

<template>
  <component
    :is="componentName"
    v-if="!isHidden"
    :class="{
      'calendar-day': true,
      today: isToday && didAnswerCorrectly === null,
      tomorrow: isTomorrow,
      disabled: isLocked,
      completed: isFinished,
      success: didAnswerCorrectly === true,
      fail: didAnswerCorrectly === false,
      'did-answer': didAnswerCorrectly !== null && !isLocked,
    }"
  >
    <!-- :to="
      !isLocked
        ? { name: 'chapter-intro', params: { slug: chapterSlug } }
        : undefined
    " -->
    <template v-if="isLocked">
      <h2 class="title">{{ chapter.title }}</h2>
      <div class="icon icon--lock">
        <LockIcon />
      </div>
    </template>
    <template v-else>
      <div class="text-content">
        <h2 class="title">{{ chapter.title }}</h2>
        <div v-if="isToday && didAnswerCorrectly === null" class="text">
          REŠI!
        </div>
      </div>
      <div class="answer-icons">
        <div class="answer-icon"><QuestionIcon /></div>
        <div class="answer-icon"><QuestionIcon /></div>
        <div class="answer-icon"><QuestionIcon /></div>
      </div>
    </template>
  </component>
</template>

<style scoped lang="scss">
@use "@sass-fairy/string";
@use "@sass-fairy/url";
@use "@/assets/variables" as vars;

.calendar-day {
  display: flex;
  flex-direction: column;
  aspect-ratio: 1;
  background: var(--kvizle-color-4);
  border: 2px solid var(--kvizle-color-2);
  overflow: hidden;
  text-decoration: none;
  transition:
    scale 0.15s ease-in-out,
    rotate 0.15s ease-in-out,
    box-shadow 0.15s ease-in-out;
  will-change: scale, rotate, box-shadow;

  .title {
    margin-bottom: 0;
    font-size: 1.5rem;
    font-weight: 500;
    text-align: center;

    @media (max-width: 576px) {
      font-size: 0.875rem;
    }
  }

  .text-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 0.75rem;
    padding-top: 0.5rem;

    .text {
      font-family: var(--font-family-alt);
      font-size: 2.25rem;
      line-height: 1;
      color: var(--kvizle-color-2);
      letter-spacing: 3%;
      text-decoration: none;
      text-shadow: 2px 2px 0 var(--kvizle-color-3);
      text-align: center;
      -webkit-text-fill-color: var(--kvizle-color-1);
      -webkit-text-stroke: 2px;

      @media (max-width: 576px) {
        font-size: 1.75rem;
      }
    }
  }

  .answer-icons {
    display: flex;
    background: var(--kvizle-color-0);
    border-top: 2px solid var(--kvizle-color-2);

    .answer-icon {
      flex: 1 0 0%;
      display: grid;
      aspect-ratio: 1;

      &:not(:last-child) {
        border-right: 2px solid var(--kvizle-color-2);
      }

      svg {
        height: 2rem;
        margin: auto;
      }
    }
  }

  &.today {
    background: var(--kvizle-color-5);
  }

  &.did-answer {
    background: var(--kvizle-color-7);
  }

  &.disabled {
    justify-content: center;
    align-items: center;
    gap: 1rem;
    background: var(--kvizle-color-0);
    cursor: default;

    .title {
      color: var(--kvizle-color-2);
    }

    .icon {
      width: 2.25rem;
      margin-inline: auto;

      svg {
        width: 100%;
        height: 100%;
      }
    }
  }

  &:not(.disabled) {
    &:hover {
      rotate: 3deg;
      scale: 1.05;
      box-shadow: 0 0 8px 2px var(--kvizle-color-6);

      &:not(.did-answer) {
        background: var(--kvizle-color-5);
      }
    }

    &:focus-visible {
      outline: 2px solid var(--kvizle-color-2);
      outline-offset: 2px;
    }
  }
}
</style>
