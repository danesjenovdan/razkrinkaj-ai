import { defineStore } from 'pinia'
import { ref, computed, reactive } from 'vue'

export const useIntroductionStore = defineStore('introduction', () => {
  const title = ref('Razkrinkaj.AI')
  const introduction = ref('Uvodno besedilo')

  return { title, introduction }
})
