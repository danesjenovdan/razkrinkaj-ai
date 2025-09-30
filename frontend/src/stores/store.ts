import type { Chapter, Explanation, LeaderboardData } from '@/types'
import axios from 'axios'
import { defineStore } from 'pinia'
import { computed, reactive, ref } from 'vue'
import { smartParse, smartToString, slugifyDot } from '@/utils/stringify'
import { preloadImage, preloadImages } from '@/utils/image'
import { apiUrl } from '@/utils/api'

type AnswerData = {
  answerIndex: number
  correct: boolean
  answerText?: string
}

type FinishedChapterData = {
  score: number
  answers: Map<number, AnswerData>
}

export const useStore = defineStore('store', () => {
  const homeDataLoaded = ref(false)
  const chapterDataLoaded = reactive(new Map<number, boolean>())

  // user guid (does not change after reset)
  const userGUID = ref('')
  // attempt guid (does change after reset)
  const attemptGUID = ref('')
  const attemptStreak = ref(0)

  // intro texts
  const introductionTitle = ref('')
  const introductionDescription = ref('')
  const introductionButtonText = ref('')
  const introductionButtonTextSecondary = ref('')

  // chapters
  const chapters = reactive(new Map<number, Chapter>())
  const explanations = reactive(new Map<number, Explanation>())

  // ids of just unlocked chapters
  const justUnlockedChapters = ref<number[]>([])
  // ids of all unlocked chapters
  const unlockedChapters = ref<number[]>([])
  // ids of finished chapters to score and answers
  const finishedChapters = reactive(new Map<number, FinishedChapterData>())
  // ids of in progress chapters to score and answers
  const inProgressChapters = reactive(new Map<number, FinishedChapterData>())

  // user answers
  const currentChapterId = ref(-1)
  const currentChapterScore = ref(0)
  // ids of pages to answers
  const currentChapterAnswers = reactive(new Map<number, AnswerData>())

  function setCurrentChapter(id: number) {
    currentChapterId.value = id
    if (finishedChapters.has(id)) {
      const data = finishedChapters.get(id)
      if (data) {
        currentChapterScore.value = data.score
        currentChapterAnswers.clear()
        for (const [k, v] of data.answers.entries()) {
          currentChapterAnswers.set(k, v)
        }
      } else {
        currentChapterScore.value = 0
        currentChapterAnswers.clear()
      }
    } else if (inProgressChapters.has(id)) {
      const data = inProgressChapters.get(id)
      if (data) {
        currentChapterScore.value = data.score
        currentChapterAnswers.clear()
        for (const [k, v] of data.answers.entries()) {
          currentChapterAnswers.set(k, v)
        }
      } else {
        currentChapterScore.value = 0
        currentChapterAnswers.clear()
      }
    } else {
      currentChapterScore.value = 0
      currentChapterAnswers.clear()
    }
  }

  function clearCurrentChapter() {
    setCurrentChapter(-1)
  }

  function generateGUID() {
    const one = Math.random().toString(36).substring(2)
    const two = Math.random().toString(36).substring(2)
    return one + two
  }

  function clearAllProgress() {
    attemptGUID.value = generateGUID()
    attemptStreak.value = 0
    justUnlockedChapters.value = []
    unlockedChapters.value = []
    finishedChapters.clear()
    inProgressChapters.clear()
    clearCurrentChapter()
    clearLocalStorage()
  }

  function clearLocalStorage() {
    const s = window.localStorage
    s.setItem('attemptGUID', attemptGUID.value)
    s.removeItem('justUnlockedChapters')
    s.removeItem('unlockedChapters')
    s.removeItem('finishedChapters')
    s.removeItem('inProgressChapters')
  }

  function saveLocalStorage() {
    const s = window.localStorage
    s.setItem('userGUID', userGUID.value)
    s.setItem('attemptGUID', attemptGUID.value)
    s.setItem('justUnlockedChapters', smartToString(justUnlockedChapters))
    s.setItem('unlockedChapters', smartToString(unlockedChapters))
    s.setItem('finishedChapters', smartToString(finishedChapters))
    s.setItem('inProgressChapters', smartToString(inProgressChapters))
  }

  function loadLocalStorage() {
    const s = window.localStorage
    let item: string | null = null

    // load user guid
    if ((item = s.getItem('userGUID'))) {
      userGUID.value = item
    } else {
      userGUID.value = generateGUID()
      s.setItem('userGUID', userGUID.value)
    }

    // load attempt guid
    if ((item = s.getItem('attemptGUID'))) {
      attemptGUID.value = item
    } else {
      attemptGUID.value = generateGUID()
      s.setItem('attemptGUID', attemptGUID.value)
    }

    // load saved data
    if ((item = s.getItem('justUnlockedChapters'))) {
      const value = smartParse(item) as number[]
      justUnlockedChapters.value = value
    }
    if ((item = s.getItem('unlockedChapters'))) {
      const value = smartParse(item) as number[]
      unlockedChapters.value = value
    }
    if ((item = s.getItem('finishedChapters'))) {
      const value = smartParse(item) as Map<number, FinishedChapterData>
      finishedChapters.clear()
      for (const [k, v] of value.entries()) {
        finishedChapters.set(k, v)
      }
    }
    if ((item = s.getItem('inProgressChapters'))) {
      const value = smartParse(item) as Map<number, FinishedChapterData>
      inProgressChapters.clear()
      for (const [k, v] of value.entries()) {
        inProgressChapters.set(k, v)
      }
    }
  }

  // total score
  const score = computed(() => {
    return [...finishedChapters.values()].reduce(
      (prev, curr) => prev + curr.score,
      0,
    )
  })

  async function fetchHomeData() {
    const response = await axios.get(`${apiUrl}/api/home/`)

    if (response.status == 200) {
      const data = response.data
      introductionTitle.value = data.title
      introductionDescription.value = data.description
      preloadImages(data.description_images)
      introductionButtonText.value = data.button_text
      introductionButtonTextSecondary.value = data.button_text_secondary

      chapters.clear()
      for (const c of data.chapters) {
        chapters.set(c.id, c)
        if (c.image) {
          preloadImage(c.image)
        }
      }

      explanations.clear()
      for (const e of data.explanations) {
        explanations.set(e.id, e)
      }

      homeDataLoaded.value = true
    }
  }

  async function initHomeData() {
    if (!homeDataLoaded.value) {
      await fetchHomeData()
    }
  }

  function getChapterIdBySlug(slug: string) {
    for (const chapter of chapters.values()) {
      if (slugifyDot(chapter.title) === slug) {
        return chapter.id
      }
    }
    return -1
  }

  async function fetchChapterData(id: number) {
    const response = await axios.get(`${apiUrl}/api/chapter/${id}/`)

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

  async function sendChapterDataToApi(
    data: FinishedChapterData | undefined,
    url: string,
  ) {
    if (data) {
      try {
        const response = await axios.post(url, {
          userGUID: userGUID.value,
          attemptGUID: attemptGUID.value,
          data: smartToString(data),
        })
        if (response.status == 200) {
          console.log('sendChapterDataToApi', response.data)
        }
      } catch (error) {
        console.error('sendChapterDataToApi', error)
      }
    } else {
      console.error('sendChapterDataToApi', 'no data')
    }
  }

  async function sendFinishedChapterDataToApi(chapterId: number) {
    const data = finishedChapters.get(chapterId)
    return sendChapterDataToApi(
      data,
      `${apiUrl}/api/chapter/${chapterId}/finished/`,
    )
  }

  async function sendProgressChapterDataToApi(chapterId: number) {
    const data = inProgressChapters.get(chapterId)
    return sendChapterDataToApi(
      data,
      `${apiUrl}/api/chapter/${chapterId}/progress/`,
    )
  }

  async function fetchPageCorrectPercent(chapterId: number, pageId: number) {
    try {
      const response = await axios.get(
        `${apiUrl}/api/chapter/${chapterId}/page/${pageId}/stats/`,
      )
      if (response.status == 200) {
        return response.data.percent_correct
      }
    } catch (error) {
      console.error('fetchPageCorrectPercent', error)
    }
    return null
  }

  async function fetchLeaderboard(): Promise<LeaderboardData | null> {
    try {
      const response = await axios.get(
        `${apiUrl}/api/leaderboard/?attempt_guid=${attemptGUID.value}`,
      )
      if (response.status == 200) {
        return response.data
      }
    } catch (error) {
      console.error('fetchLeaderboard', error)
    }
    return null
  }

  async function submitLeaderboardNickname(nickname: string): Promise<boolean> {
    try {
      const response = await axios.post(`${apiUrl}/api/leaderboard/nickname/`, {
        userGUID: userGUID.value,
        attemptGUID: attemptGUID.value,
        nickname,
      })
      if (response.status == 200) {
        return true
      }
    } catch (error) {
      console.error('submitLeaderboardNickname', error)
    }
    return false
  }

  return {
    initHomeData,
    homeDataLoaded,
    getChapterIdBySlug,
    initChapterData,
    chapterDataLoaded,
    //
    userGUID,
    attemptGUID,
    introductionTitle,
    introductionDescription,
    introductionButtonText,
    introductionButtonTextSecondary,
    chapters,
    explanations,
    justUnlockedChapters,
    unlockedChapters,
    finishedChapters,
    inProgressChapters,
    currentChapterId,
    currentChapterScore,
    currentChapterAnswers,
    attemptStreak,
    setCurrentChapter,
    clearCurrentChapter,
    clearAllProgress,
    saveLocalStorage,
    loadLocalStorage,
    score,
    sendFinishedChapterDataToApi,
    sendProgressChapterDataToApi,
    fetchPageCorrectPercent,
    fetchLeaderboard,
    submitLeaderboardNickname,
  }
})
