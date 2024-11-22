<script setup lang="ts">
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import QuizPage from '@/components/QuizPage.vue'
import RichText from '@/components/RichText.vue'
import type { Chapter } from '@/types'
import { computed, ref, watch } from 'vue'
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

const nextPageLink = computed(() => {
  return hasNextPage.value
    ? { name: 'chapter-page', params: { pageIndex: pageIndex.value + 1 } }
    : { name: 'chapter-result' }
})

const showNextButton = ref(false)

watch(pageIndex, () => {
  showNextButton.value = false
})

function onQuizDone() {
  showNextButton.value = true
}
</script>

<template>
  <main :key="pageIndex">
    <div v-if="page.type === 'text'" class="page-content">
      <RichText :title="page.title" :content="page.text" />
      <ButtonPrimary
        class="button"
        :buttonText="page.button_text"
        :link="nextPageLink"
        icon="arrow"
      />
    </div>
    <div v-else-if="page.type === 'quiz'" class="page-content">
      <QuizPage :page="page" @done="onQuizDone" />
      <ButtonPrimary
        v-if="showNextButton"
        class="button"
        :buttonText="page.button_text"
        :link="nextPageLink"
        icon="arrow"
        color="white"
      />
    </div>
    <div v-else>unknown page type</div>
  </main>
</template>

<style scoped lang="scss">
main {
  padding-bottom: 2rem;

  .page-content {
    padding-top: 0.75rem;
  }
}
</style>
