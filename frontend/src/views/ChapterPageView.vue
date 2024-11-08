<script setup lang="ts">
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import RichText from '@/components/RichText.vue'
import type { Chapter } from '@/types'
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const props = defineProps<{ chapter: Chapter }>()

const route = useRoute()
const pageIndex = computed(() => {
  const pageIndexParam = route.params.pageIndex as string
  return parseInt(pageIndexParam, 10)
})

const page = computed(() => {
  const p = props.chapter.pages?.[pageIndex.value]
  if (!p) {
    throw new Error('Page not found')
  }
  return p
})

const hasNextPage = computed(() => {
  return !!props.chapter.pages?.[pageIndex.value + 1]
})

// const answered = computed(() => {
//   if (page.value && page.value.id in store.userAnswers) {
//     return true
//   }
//   return false
// })

// function saveAnswer(correct: boolean, index: number) {
//   if (page.value) {
//     store.userAnswers[page.value.id] = index

//     if (correct) {
//       // store.chapterScore = store.chapterScore + page.value.points
//     }
//   }
// }
</script>

<template>
  <main>
    <div v-if="page.type === 'text'" class="page-content">
      <RichText :title="page.title" :content="page.text" />
      <ButtonPrimary
        class="button"
        :buttonText="page.button_text"
        :link="
          hasNextPage
            ? { name: 'chapter-page', params: { pageIndex: pageIndex + 1 } }
            : { name: 'chapter-result' }
        "
        icon="arrow"
      />
    </div>
    <!--
    <div>
       <div v-if="page.type=='quiz'">
        <img v-if="!answered" :src="`${store.apiUrl}${page.image}`" />
        <img v-if="answered" :src="`${store.apiUrl}${page.image_answer}`" />
        <div>
          <button v-for="(answer, index) in page.answers" @click="saveAnswer(answer.correct, index)" :disabled="answered"
            class="button">{{ answer.text
            }} {{ index }}</button>
        </div>
        <div v-if="answered" v-html="page.answer_description"></div>
      </div>
    </div>
    -->
  </main>
</template>

<style scoped lang="scss">
main {
  padding-bottom: 3.5rem;
}
</style>
