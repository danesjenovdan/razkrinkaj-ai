<script setup lang="ts">
import type { Chapter } from '@/types'
import { computed } from 'vue'
import { useStore } from '@/stores/store'

const props = defineProps<{ chapter: Chapter; pageIndex: number }>()

const store = useStore()

const quizPageIndices = computed(() => {
  if (props.chapter.pages) {
    return props.chapter.pages.reduce((prev, curr, i) => {
      if (curr.type === 'quiz') {
        prev.push(i)
      }
      return prev
    }, [] as number[])
  }
  return []
})

const quizPageIds = computed(() => {
  if (props.chapter.pages) {
    const pages = props.chapter.pages
    return quizPageIndices.value.map(i => pages[i].id)
  }
  return []
})

const numQuizPages = computed(() => {
  return quizPageIndices.value.length
})

const quizPageAnswers = computed(() => {
  console.log('quizPageAnswers', store.currentChapterAnswers, quizPageIds)
  return quizPageIds.value.map(
    id => store.currentChapterAnswers.get(id)?.correct,
  )
})
</script>

<template>
  <div v-if="numQuizPages > 1" class="progress-indicator">
    <div
      v-for="(pageIdx, i) in quizPageIndices"
      :key="pageIdx"
      class="progress-item"
      :class="{
        active: pageIdx === props.pageIndex,
        correct: pageIdx < props.pageIndex && quizPageAnswers[i] === true,
        incorrect: pageIdx < props.pageIndex && quizPageAnswers[i] === false,
      }"
    ></div>
  </div>
</template>

<style lang="scss" scoped>
.progress-indicator {
  display: flex;
  gap: 3px;
  margin-top: -3px;

  .progress-item {
    flex: 1 0 0%;
    height: 5px;
    border: 0.5px solid #000;
    background: #e1e6de;

    &.active {
      background: #4063f6;
    }

    &.correct {
      background: #99f37d;
    }

    &.incorrect {
      background: #e49a85;
    }
  }
}
</style>
