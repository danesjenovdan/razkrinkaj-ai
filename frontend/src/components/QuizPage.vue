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
const answeredCorrectly = computed(() => {
  if (selectedAnswer.value === null) {
    return null
  }
  return props.page.answers[selectedAnswer.value].correct
})

const image = computed(() => {
  return selectedAnswer.value === null
    ? props.page.image
    : props.page.image_answer
})

function onAnswerClick(index: number) {
  selectedAnswer.value = index
  const correct = props.page.answers[selectedAnswer.value].correct
  const points = correct ? props.page.points : -props.page.points
  // add points
  store.currentChapterScore += points
  // store answer
  store.currentChapterAnswers.set(props.page.id, {
    answerIndex: index,
    correct,
  })
  emit('done')
}

onMounted(() => {
  preloadPageImages(props.page)
})
</script>

<template>
  <div class="quiz-page">
    <ZoomableImage v-if="image" :image="image" />
    <div v-if="page.question" class="question">{{ page.question }}</div>
    <div
      :class="{
        score: true,
        correct: answeredCorrectly === true,
        incorrect: answeredCorrectly === false,
      }"
    >
      <span>
        <strong>{{ answeredCorrectly ? '+' : '-' }} {{ page.points }}</strong>
        točk
      </span>
    </div>
    <div class="answers">
      <ButtonAnswer
        v-for="(answer, index) in page.answers"
        :key="index"
        :buttonText="answer.text"
        :correct="answer.correct"
        :revealed="selectedAnswer !== null"
        :selected="selectedAnswer === index"
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

  .question {
    padding-block: 0.75rem 1.56rem;
    font-size: 1.25rem;
    font-weight: 600;
    line-height: 1.1;
    text-align: center;
  }

  .score {
    display: flex;
    justify-content: center;
    margin-block: 0.75rem;

    span {
      visibility: hidden;
      display: inline-block;
      padding: 0.125rem 0.3rem;
      background: #ccc;
      font-size: 0.75rem;
      line-height: 1;

      strong {
        font-weight: 900;
      }
    }

    &.correct {
      span {
        visibility: visible;
        background: #c5f6b6;
      }
    }

    &.incorrect {
      span {
        visibility: visible;
        background: #f9c7b9;
      }
    }
  }

  .answers {
    display: grid;
    gap: 0.68rem;

    @media (min-width: 768px) {
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
