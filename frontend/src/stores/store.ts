import { defineStore } from 'pinia'
import { ref, computed, reactive } from 'vue'
import type { Chapter } from '@/types'

import axios from 'axios'

export const useStore = defineStore('store', () => {
  // app info
  const apiUrl =
    import.meta.env.VITE_API_URL_BASE || 'http://localhost:8000'
  const storeInitialized = ref(false)
  // texts
  const introduction_title = ref('Naslov')
  const introduction_description = ref('Opis')
  const introduction_button_text = ref('Gumb')
  // chapters
  const chapters: Chapter[] = reactive([])
  // user answers
  const score = ref(10)
  const chapterScore = ref(0)

  // če poglavja nisi zaključil - ga na novo fetchamo
  // če poglavje si zaključil, se shranijo tvoji odgovori in score

  async function getData() {
    const response = await axios.get(`${apiUrl}/api/home`)
    console.log(response)

    if (response.status == 200) {
      const data = response.data
      introduction_title.value = data.title
      introduction_description.value = data.description
      introduction_button_text.value = data.button_text

      for (let c of data.chapters) {
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

  return {
    initializeStore,
    getChapterData,
    introduction_title,
    introduction_description,
    introduction_button_text,
    score,
    chapterScore,
    chapters,
    apiUrl
  }
})
