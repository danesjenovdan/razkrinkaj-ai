import { defineStore } from 'pinia'
import { ref, computed, reactive, onMounted } from 'vue'
import type { Chapter } from '@/types'

import axios from 'axios'

export const useStore = defineStore('store', () => {
  // app info
  const apiUrl = import.meta.env.VITE_API_URL_BASE || 'http://localhost:8000'
  const storeInitialized = ref(false)
  // texts
  const introductionTitle = ref('')
  const introductionDescription = ref('')
  const introductionButtonText = ref('')
  // chapters
  const chapters: Chapter[] = reactive([])
  // user answers
  const finishedChapters: Record<number, number> = reactive({}) // finished chapters with number of points
  const userAnswers: Record<number, number> = reactive({}) // userAnswers[pageId] = chosenAnswerIndex
  const chapterScore = ref(0)
  const score = computed(() => {
    return Object.values(finishedChapters).reduce((a, b) => a + b, 0)
  })

  // če poglavja nisi zaključil - ga na novo fetchamo
  // če poglavje si zaključil, se shranijo tvoji odgovori in score

  async function getData() {
    const response = await axios.get(`${apiUrl}/api/home`)
    // console.log(response)

    if (response.status == 200) {
      const data = response.data
      introductionTitle.value = data.title
      introductionDescription.value = data.description
      introductionButtonText.value = data.button_text

      for (const c of data.chapters) {
        if (c.image && !c.image.startsWith('http')) {
          c.image = `${apiUrl}${c.image}`
        }
        chapters.push(c)
      }

      storeInitialized.value = true
    }
  }

  async function getChapterData(id: string) {
    const response = await axios.get(`${apiUrl}/api/chapter/${id}`)
    console.log(response)

    if (response.status == 200) {
      const data = response.data

      const chapter = chapters.filter(c => c.id.toString() == id)[0]
      chapter.pages = data.pages

      // storeInitialized.value = true
    }
  }

  async function initializeStore() {
    if (!storeInitialized.value) {
      getData()
    }
  }

  onMounted(() => {
    initializeStore()
  })

  return {
    initializeStore,
    getChapterData,
    introductionTitle,
    introductionDescription,
    introductionButtonText,
    chapters,
    score,
    chapterScore,
    userAnswers,
    finishedChapters,
    apiUrl,
  }
})
