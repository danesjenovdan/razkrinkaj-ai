<script setup lang="ts">
import type { QuizPage } from "@/types";
import { computed, onMounted, ref } from "vue";
import { useStore } from "@/stores/store.ts";
import ButtonAnswer from "./ButtonAnswer.vue";
import RichText from "./RichText.vue";
import { preloadPageImages } from "@/utils/image.ts";

const props = defineProps<{ page: QuizPage }>();
const emit = defineEmits<{ done: [] }>();

const store = useStore();

const selectedAnswer = ref<number | null>(null);

const percentPeopleCorrect = ref(-1);

const chapterDate = computed(() => {
  const chapter = store.chapters.get(store.currentChapterId);
  const dateParts = (chapter?.title || "").split(".").map(Number);
  return new Date(dateParts[2], dateParts[1] - 1, dateParts[0]);
});

function onAnswerClick(index: number) {
  selectedAnswer.value = index;
  const correct = props.page.answers[index].correct;
  // const points = correct ? props.page.points : -props.page.points;
  const points = correct ? props.page.points : 0;
  // add points
  store.currentChapterScore += points;
  // store answer
  store.currentChapterAnswers.set(props.page.id, {
    answerIndex: index,
    correct,
    answerText: props.page.answers[index].text,
  });
  // update in progress chapters
  store.inProgressChapters.set(store.currentChapterId, {
    score: store.currentChapterScore,
    answers: new Map(store.currentChapterAnswers),
  });
  // add to streak if current date is the chapter date
  const today = new Date();
  const isSameDay =
    today.getDate() === chapterDate.value.getDate() &&
    today.getMonth() === chapterDate.value.getMonth() &&
    today.getFullYear() === chapterDate.value.getFullYear();
  if (isSameDay && correct) {
    store.attemptStreak += 1;
  } else if (isSameDay && !correct) {
    store.attemptStreak = 0;
  }

  store
    .sendProgressChapterDataToApi(store.currentChapterId)
    .then(() =>
      store.fetchPageCorrectPercent(store.currentChapterId, props.page.id),
    )
    .then((value) => {
      percentPeopleCorrect.value = value;
    })
    .finally(() => {
      // persist data to local storage
      store.saveLocalStorage();
      emit("done");
    });
}

onMounted(() => {
  preloadPageImages(props.page);

  if (
    store.finishedChapters.has(store.currentChapterId) ||
    store.inProgressChapters.has(store.currentChapterId)
  ) {
    const index = store.currentChapterAnswers.get(props.page.id)?.answerIndex;
    if (index != null) {
      selectedAnswer.value = index;
      store
        .fetchPageCorrectPercent(store.currentChapterId, props.page.id)
        .then((value) => {
          percentPeopleCorrect.value = value;
        });
      emit("done");
    }
  }
});
</script>

<template>
  <div class="quiz-page">
    <div v-if="page.image" class="question">
      <img
        :src="page.image.url"
        :alt="page.question || ''"
        class="question-image"
      />
    </div>
    <div v-else-if="page.question" class="question">
      {{ page.question }}
    </div>
    <div v-if="page.source_text && selectedAnswer !== null" class="source-text">
      <RichText :content="page.source_text" />
    </div>
    <div class="answers">
      <div v-for="(answer, index) in page.answers" :key="index" class="answer">
        <ButtonAnswer
          :button-text="answer.text"
          :correct="answer.correct"
          :revealed="selectedAnswer !== null"
          :selected="selectedAnswer === index"
          :points="page.points"
          @click="onAnswerClick(index)"
        />
      </div>
    </div>
    <div
      v-if="selectedAnswer !== null && page.answer_description"
      class="answer-description-wrapper"
    >
      <div class="answer-description">
        <RichText :content="page.answer_description" />
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@use "@/assets/mixins";

.quiz-page {
  padding-block: 2.5rem;

  .question {
    max-width: 38rem;
    margin-inline: auto;
    font-size: 1.75rem;
    font-weight: 500;
    text-align: center;

    @media (max-width: 576px) {
      font-size: 1.375rem;
    }

    .question-image {
      width: 100%;
      height: auto;
    }
  }

  .source-text {
    max-width: 38rem;
    margin-inline: auto;

    .rich-text {
      padding-block: 0.25rem;
      padding: 0.25rem;
      text-align: right;

      :deep(.rich-content) {
        p {
          font-size: 1rem;

          @media (max-width: 576px) {
            font-size: 0.875rem;
          }
        }

        a {
          display: inline-block;
          font-weight: 500;
          color: inherit;

          &:hover {
            text-decoration: none;
          }

          @include mixins.focus-visible;
        }
      }
    }
  }

  .answers {
    display: grid;
    gap: 0.6875rem;
    max-width: 38rem;
    margin-inline: auto;
    margin-top: 2.5rem;
  }

  .answer-description-wrapper {
    max-width: 38rem;
    margin-inline: auto;
    margin-top: 2.5rem;

    .answer-description {
      padding: 1.5rem;
      background-color: var(--kvizle-color-8);

      @media (max-width: 576px) {
        padding: 1.25rem;
      }

      .rich-text {
        padding-block: 0;
        font-size: 1.25rem;

        :deep(.rich-content) {
          p {
            font-size: 1.25rem;

            @media (max-width: 576px) {
              font-size: 1rem;
            }
          }

          a {
            display: inline-block;
            font-weight: 500;
            color: inherit;

            &:hover {
              text-decoration: none;
            }

            @include mixins.focus-visible;
          }
        }
      }
    }
  }
}
</style>
