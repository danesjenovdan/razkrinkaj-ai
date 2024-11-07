<script setup lang="ts">
import { computed, ref, watch } from 'vue'
import { useStore } from '@/stores/store'
import { useRoute } from 'vue-router'

const store = useStore()
const route = useRoute()

const chapterId = <string>route.params.id
const chapter = store.chapters.filter((c) => c.id.toString() == chapterId)[0]

const pageId = ref(<string>route.params.pageId)

watch(
  () => route.params.pageId,
  async newPageId => {
    console.log("new page id!", newPageId)
    pageId.value = <string>newPageId
  }
)

const currentPageIndex = computed((): number => {
  return parseInt(pageId.value) - 1
})

const page = computed(() => {
  const chapter = store.chapters.filter(c => c.id.toString() == chapterId)[0]
  try {
    return chapter.pages[currentPageIndex.value]
  } catch {
    return null
  }
})

const answered = computed(() => {
  if (page.value && page.value.id in store.userAnswers) {
    return true
  }
  return false
})

function saveAnswer(correct: boolean, index: number) {
  if (page.value) {
    store.userAnswers[page.value.id] = index

    if (correct) {
      // store.chapterScore = store.chapterScore + page.value.points
    }
  }
}

</script>

<template>
  <main>
    <div v-if="page">
      <h1>{{ page.title }}</h1>
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
      <div v-else>
        <div v-html="page.text"></div>
      </div>
      <div v-if="answered || page.type === 'text'" class="button-wrapper">
        <!-- go to next page -->
        <RouterLink v-if="currentPageIndex + 1 < chapter.pages.length"
          :to="{ name: 'chapter-page', params: { id: chapterId, pageId: currentPageIndex + 2 } }">Nadaljuj</RouterLink>
        <!-- go to results -->
        <RouterLink v-else :to="{ name: 'chapter-result', params: { id: chapterId } }">Nadaljuj</RouterLink>
      </div>
    </div>
    <div v-else>
      loading...
    </div>
  </main>
</template>

<style lang="scss">
img {
  width: 100%;
  height: auto;
}
</style>
