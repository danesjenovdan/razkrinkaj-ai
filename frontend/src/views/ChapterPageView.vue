<script setup lang="ts">
import ButtonPrimary from "@/components/ButtonPrimary.vue";
import QuizPage from "@/components/QuizPage.vue";
import RichText from "@/components/RichText.vue";
import { useStore } from "@/stores/store.ts";
import type { Chapter } from "@/types";
import { preloadPageImages } from "@/utils/image.ts";
import { computed, ref, watch, onMounted } from "vue";
import { useRoute } from "vue-router";

const props = defineProps<{ chapter: Chapter }>();

const store = useStore();
const route = useRoute();
const pageIndex = computed(() => {
  const pageIndexParam = route.params.pageIndex as string;
  if (!pageIndexParam) {
    return 0;
  }
  return parseInt(pageIndexParam, 10);
});

const chapterDate = computed(() => {
  const dateParts = props.chapter.title.split(".").map(Number);
  return new Date(dateParts[2], dateParts[1] - 1, dateParts[0]);
});

const formattedTitle = computed(() => {
  if (!chapterDate.value || Number.isNaN(chapterDate.value.getTime())) {
    return props.chapter.title;
  }
  const formatter = new Intl.DateTimeFormat("sl-SI", {
    weekday: "long",
    day: "numeric",
    month: "long",
    year: "numeric",
  });
  const formattedDate = formatter.format(chapterDate.value);
  return formattedDate.charAt(0).toUpperCase() + formattedDate.slice(1);
});

const page = computed(() => {
  const p = props.chapter.pages?.[pageIndex.value];
  if (!p) {
    return null;
    // throw new Error('Page not found')
  }
  if (chapterDate.value && !Number.isNaN(chapterDate.value.getTime())) {
    const now = Date.now();
    const isLocked = now < chapterDate.value.getTime();
    if (isLocked) {
      return null;
      // throw new Error('Page is locked')
    }
  }
  return p;
});

const hasNextPage = computed(() => {
  return !!props.chapter.pages?.[pageIndex.value + 1];
});

const nextPageLink = computed(() => {
  return hasNextPage.value
    ? { name: "chapter-page", params: { pageIndex: pageIndex.value + 1 } }
    : { name: "chapter-result" };
});

const showNextButton = ref(false);

watch(pageIndex, () => {
  showNextButton.value = false;
});

function onQuizDone() {
  showNextButton.value = true;

  if (!hasNextPage.value) {
    // save score and answers
    if (!store.finishedChapters.has(props.chapter.id)) {
      store.finishedChapters.set(props.chapter.id, {
        score: store.currentChapterScore,
        answers: new Map(store.currentChapterAnswers),
      });
      store.inProgressChapters.delete(props.chapter.id);
      store.sendFinishedChapterDataToApi(props.chapter.id);
      store.saveLocalStorage();
    }
  }
}

const nextPage = computed(() => {
  return props.chapter.pages?.[pageIndex.value + 1];
});

watch(nextPage, () => {
  if (nextPage.value) {
    preloadPageImages(nextPage.value);
  }
});

onMounted(() => {
  if (nextPage.value) {
    preloadPageImages(nextPage.value);
  }
});
</script>

<template>
  <main v-if="!page" :key="'no-page'" class="no-page">
    <h1>page not found</h1>
  </main>
  <main v-else :key="pageIndex">
    <div class="page-gutter">
      <div class="narrow">
        <div class="intro">
          <h1>{{ formattedTitle }}</h1>
        </div>
      </div>
      <div v-if="page.type === 'text'" class="page-content">
        <RichText :title="page.title" :content="page.text" />
        <ButtonPrimary
          class="button"
          button-text="NADALJUJ"
          :link="nextPageLink"
          icon="hand"
        />
      </div>
      <div v-else-if="page.type === 'quiz'" class="page-content">
        <QuizPage :page="page" @done="onQuizDone" />
        <ButtonPrimary
          v-if="showNextButton"
          class="button"
          button-text="NADALJUJ"
          :link="nextPageLink"
          icon="hand"
          color="white"
        />
      </div>
      <div v-else>unknown page type</div>
    </div>
  </main>
</template>

<style scoped lang="scss">
main.no-page {
  margin-top: 3rem;

  h1 {
    font-size: 1.5rem;
    font-weight: 600;
    text-align: center;
  }
}

main {
  .narrow {
    max-width: 603px;
    margin: 0 auto;
  }

  .intro {
    padding-block: 4.4375rem 0;

    @media (max-width: 576px) {
      padding-block: 2rem 0;
    }

    h1 {
      margin-bottom: 0;
      font-size: 1.3125rem;
      font-weight: 600;
      text-align: center;
    }
  }

  .page-content {
    padding-bottom: 7rem;

    @media (max-width: 576px) {
      padding-bottom: 4rem;
    }
  }

  .button {
    gap: 1.5rem;
    justify-content: center;
    max-width: 455px;
    margin-inline: auto;
    text-align: center;
  }
}
</style>
