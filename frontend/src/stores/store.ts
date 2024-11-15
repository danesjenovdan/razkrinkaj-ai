import type { Chapter } from '@/types'
import axios from 'axios'
import { defineStore } from 'pinia'
import { computed, reactive, ref } from 'vue'

const apiUrl = import.meta.env.VITE_API_URL_BASE || 'http://localhost:8000'

export const useStore = defineStore('store', () => {
  const homeDataLoaded = ref(false)
  const chapterDataLoaded = reactive(new Map<number, boolean>())

  // intro texts
  const introductionTitle = ref('')
  const introductionDescription = ref('')
  const introductionButtonText = ref('')

  // chapters
  const chapters = reactive(new Map<number, Chapter>())

  // ids of just unlocked chapters
  const justUnlockedChapters = ref<number[]>([])
  // ids of all unlocked chapters
  const unlockedChapters = ref<number[]>([])
  // ids of finished chapters to number of points
  const finishedChapters = reactive(new Map<number, number>())

  // user answers
  const userAnswers: Record<number, number> = reactive({}) // userAnswers[pageId] = chosenAnswerIndex
  const score = computed(() => {
    return Object.values(finishedChapters).reduce((a, b) => a + b, 0)
  })

  // če poglavja nisi zaključil - ga na novo fetchamo
  // če poglavje si zaključil, se shranijo tvoji odgovori in score

  async function fetchHomeData() {
    const response = await axios.get(`${apiUrl}/api/home`)

    if (response.status == 200) {
      const data = response.data
      introductionTitle.value = data.title
      introductionDescription.value = data.description
      introductionButtonText.value = data.button_text

      chapters.clear()
      for (const c of data.chapters) {
        chapters.set(c.id, c)
      }

      homeDataLoaded.value = true
    }
  }

  async function initHomeData() {
    if (!homeDataLoaded.value) {
      await fetchHomeData()
    }
  }

  async function fetchChapterData(id: number) {
    const response = await axios.get(`${apiUrl}/api/chapter/${id}`)

    if (response.status == 200) {
      const data = response.data
      const chapter = chapters.get(id)
      if (chapter) {
        chapter.pages = data.pages

        chapterDataLoaded.set(chapter.id, true)
      }
    }
  }

  async function initChapterData(id: number) {
    if (!chapterDataLoaded.get(id)) {
      await fetchChapterData(id)
    }
  }

  return {
    initHomeData,
    homeDataLoaded,
    initChapterData,
    chapterDataLoaded,
    //
    introductionTitle,
    introductionDescription,
    introductionButtonText,
    chapters,
    score,
    userAnswers,
    finishedChapters,
    apiUrl,
    justUnlockedChapters,
    unlockedChapters,
  }
})
