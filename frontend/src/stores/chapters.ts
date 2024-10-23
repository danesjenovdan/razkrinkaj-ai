import { defineStore } from 'pinia'
import { ref, computed, reactive } from 'vue'
import type { Chapter } from '@/types'


export const useChaptersStore = defineStore('chapters', () => {
  const chapters: Chapter[] = reactive([
    {
      title: 'Spoznaj AI',
      shortDescription:
        'Kako delujejo orodja za generativno ustvarjanje vsebin?',
      description: '<p>Dolg opis</p>',
    },
    {
      title: 'Prepoznaj obraze',
      shortDescription: '',
      description: '<p>Dolg opis</p>',
    },
  ])

  return { chapters }
})
