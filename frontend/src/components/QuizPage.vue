<script setup lang="ts">
import type { QuizPage } from '@/types'
import { computed, onMounted, ref } from 'vue'
import { useStore } from '@/stores/store'
import ButtonAnswer from './ButtonAnswer.vue'
import RichText from './RichText.vue'
import ZoomableImage from './ZoomableImage.vue'
import { preloadPageImages } from '@/utils/image'

const props = defineProps<{ page: QuizPage }>()
const emit = defineEmits<{ done: [] }>()

const store = useStore()

const selectedAnswer = ref<number | null>(null)

const image = computed(() => {
  if (selectedAnswer.value !== null && props.page.image_answer) {
    return props.page.image_answer
  }
  return props.page.image
})

function onAnswerClick(index: number) {
  selectedAnswer.value = index
  const correct = props.page.answers[index].correct
  const points = correct ? props.page.points : -props.page.points
  // add points
  store.currentChapterScore += points
  // store answer
  store.currentChapterAnswers.set(props.page.id, {
    answerIndex: index,
    correct,
    answerText: props.page.answers[index].text,
  })
  // update in progress chapters
  store.inProgressChapters.set(store.currentChapterId, {
    score: store.currentChapterScore,
    answers: new Map(store.currentChapterAnswers),
  })
  store.sendProgressChapterDataToApi(store.currentChapterId)
  // persist data to local storage
  store.saveLocalStorage()
  emit('done')
}

onMounted(() => {
  preloadPageImages(props.page)

  if (
    store.finishedChapters.has(store.currentChapterId) ||
    store.inProgressChapters.has(store.currentChapterId)
  ) {
    const index = store.currentChapterAnswers.get(props.page.id)?.answerIndex
    if (index != null) {
      selectedAnswer.value = index
      emit('done')
    }
  }
})
</script>

<template>
  <div class="quiz-page">
    <ZoomableImage v-if="image" :image="image" class="main-image" />
    <div v-if="page.question" class="question">{{ page.question }}</div>
    <div class="answers">
      <ButtonAnswer
        v-for="(answer, index) in page.answers"
        :key="index"
        :buttonText="answer.text"
        :correct="answer.correct"
        :revealed="selectedAnswer !== null"
        :selected="selectedAnswer === index"
        :points="page.points"
        @click="onAnswerClick(index)"
      />
    </div>
    <div v-if="selectedAnswer !== null" class="answer-description">
      <RichText :content="page.answer_description" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.quiz-page {
  padding-block: 1.5rem 1.56rem;

  @media (min-width: 768px) {
    padding-bottom: 3.38rem;
  }

  .main-image {
    margin-bottom: 0.75rem;
  }

  .question {
    font-size: 1.25rem;
    font-weight: 600;
    line-height: 1.1;
    text-align: center;
  }

  .answers {
    display: grid;
    gap: 0.68rem;
    margin-top: 2rem;

    @media (min-width: 768px) {
      margin-top: 2.25rem;
      gap: 0.875rem;
    }
  }

  .answer-description {
    margin-top: 2.12rem;
    padding: 1rem 1.125rem;
    background: var(--color-bg-accent);
    border-radius: 3px;

    @media (min-width: 768px) {
      margin-top: 3.38rem;
      padding: 1.68rem 1.5rem;
    }

    .rich-text {
      padding-block: 0;
    }
  }
}
</style>
