import { defineStore } from 'pinia'
import { ref, computed, reactive } from 'vue'

export const useResultsStore = defineStore('results', () => {
  const score = ref(10)
  const chapterScore = ref(0)
  // const doubleCount = computed(() => count.value * 2)
  // function increment() {
  //   count.value++
  // }

  return { score, chapterScore }
})
