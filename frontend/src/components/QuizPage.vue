<script setup lang="ts">
import type { QuizPage } from '@/types'
import { computed, ref } from 'vue'
import { useStore } from '@/stores/store'
import ButtonAnswer from './ButtonAnswer.vue'
import RichText from './RichText.vue'

const props = defineProps<{ page: QuizPage }>()
const emit = defineEmits<{ done: [] }>()

const store = useStore()

// TODO:
// const answered = computed(() => {
//   if (page.value && page.value.id in store.userAnswers) {
//     return true
//   }
//   return false
// })

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
  store.currentChapterScore += points
  emit('done')
}
</script>

<template>
  <div class="quiz-page">
    <img
      v-if="image"
      :src="image.url"
      :alt="image.alt"
      :width="image.width"
      :height="image.height"
    />
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
  padding-block: 1.5rem;

  img {
    display: block;
    width: 100%;
    height: auto;
    padding: 0.25rem;
    border-radius: 3px;
    border: 0.5px solid #000;
    background: var(--color-bg-white);
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
  }

  .answer-description {
    margin-top: 2.25rem;
    margin-bottom: 0.75rem;
    padding: 1rem 1.125rem;
    background: var(--color-bg-accent);
    border-radius: 3px;

    .rich-text {
      padding-block: 0;
    }
  }
}
</style>
