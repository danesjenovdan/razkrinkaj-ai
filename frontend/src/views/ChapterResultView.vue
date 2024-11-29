<script setup lang="ts">
import type { Chapter } from '@/types'
import { computed, onMounted } from 'vue'
import { useStore } from '@/stores/store'
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import ThumbnailImage from '@/components/ThumbnailImage.vue'

const props = defineProps<{ chapter: Chapter }>()

const store = useStore()

// const totalChapterScore = computed(() => {
//   if (props.chapter.pages) {
//     return props.chapter.pages.reduce((prev, curr) => {
//       if (curr.type === 'quiz') {
//         return prev + curr.points
//       }
//       return prev
//     }, 0)
//   }
//   return 0
// })

const totalAnswers = computed(() => {
  const answers = [...store.currentChapterAnswers.values()]
  return answers.length
})

const correctAnswers = computed(() => {
  const answers = [...store.currentChapterAnswers.values()].filter(
    answer => answer.correct,
  )
  return answers.length
})

const shareResultMessage = computed(() => {
  return `

Razkrinkaj.ai

Poglavje: ${props.chapter.title}

💪 Zbranih točk: ${store.currentChapterScore}
🎓 Pravilni odgovori: ${correctAnswers.value}/${totalAnswers.value}
🚀 Skupaj točk: ${store.score}

  `.trim()
})

async function copyTextToClipboard(text: string) {
  try {
    await navigator.clipboard.writeText(text)
    return true
  } catch (error) {
    console.error(error)
    return false
  }
}

async function onShareResult() {
  if (await copyTextToClipboard(shareResultMessage.value)) {
    window.alert(
      `Tvoj rezultat smo skopirali v odložišče. Objavi ga na svojem najljubšem kanalu!\n\n${shareResultMessage.value}`,
    )
  } else {
    window.alert(
      'Ups, nekaj je šlo narobe pri kopiranju v odložišče. Rezultat imaš spodaj, skopiraj in deli ga!',
    )
  }
}

onMounted(() => {
  // save score and answers
  if (!store.finishedChapters.has(props.chapter.id)) {
    store.finishedChapters.set(props.chapter.id, {
      score: store.currentChapterScore,
      answers: new Map(store.currentChapterAnswers),
    })
    store.sendFinishedChapterDataToApi(props.chapter.id)
  }
  // unlock next chapter
  const chapterIds = [...store.chapters.keys()]
  const currentChapterIndex = chapterIds.findIndex(
    cid => cid === props.chapter.id,
  )
  const nextChapterId = chapterIds[currentChapterIndex + 1]
  if (nextChapterId) {
    if (!store.justUnlockedChapters.includes(nextChapterId)) {
      store.justUnlockedChapters.push(nextChapterId)
    }
    if (!store.unlockedChapters.includes(nextChapterId)) {
      store.unlockedChapters.push(nextChapterId)
    }
  }
  // persist data to local storage
  store.saveLocalStorage()
})
</script>

<template>
  <main>
    <div class="results-header">
      <h1>Poglavje zaključeno!</h1>
    </div>
    <div class="chapter-info">
      <ThumbnailImage v-if="chapter.image" :image="chapter.image" />
      <h1>{{ chapter.title }}</h1>
    </div>
    <div class="chapter-scores">
      <div class="score-box">
        <span class="emoji">💪</span>
        <div>
          Zbranih točk:
          <span class="score">{{ store.currentChapterScore }}</span>
        </div>
      </div>
      <div class="score-box">
        <span class="emoji">🎓</span>
        <div>
          Pravilni odgovori:
          <span class="score">{{ correctAnswers }}/{{ totalAnswers }}</span>
        </div>
      </div>
      <div class="score-box">
        <span class="emoji">🚀</span>
        <div>
          Skupaj točk: <span class="score">{{ store.score }}</span>
        </div>
      </div>
    </div>
    <div class="buttons">
      <ButtonPrimary
        class="button"
        buttonText="Deli rezultat"
        @click="onShareResult"
        icon="arrow"
      />
      <ButtonPrimary
        class="button"
        buttonText="Na izbirnik poglavij"
        :link="{ name: 'chapter-list' }"
        icon="arrow"
        color="white"
      />
    </div>
  </main>
</template>

<style scoped lang="scss">
main {
  padding-bottom: 2rem;

  @media (min-width: 768px) {
    padding-bottom: 3.38rem;
  }

  .results-header {
    margin-inline: calc(var(--page-gutter) * -1);
    padding-inline: var(--page-gutter);
    margin-bottom: -1.75rem;
    padding-block: 1.5rem 2.75rem;
    background: #4063f6;
    border-bottom: 0.5px solid #000;
    text-align: center;

    @media (min-width: 768px) {
      margin-inline: 0;
      padding-inline: 0;
      margin-bottom: -1.94rem;
      padding-block: 3.44rem 4.94rem;
      border-bottom: 0;
      border-radius: 0 0 3px 3px;
    }

    h1 {
      max-width: 16rem;
      margin-inline: auto;
      margin-bottom: 0;
      font-family: var(--font-family-heading);
      font-size: 1.5rem;
      font-weight: 700;
      line-height: 1;
      color: #fff;
      text-transform: uppercase;

      @media (min-width: 768px) {
        font-size: 2.25rem;
      }
    }
  }

  .chapter-info {
    padding-bottom: 1.25rem;
    text-align: center;

    @media (min-width: 768px) {
      padding-bottom: 2.5rem;
    }

    .thumbnail-image {
      width: 5rem;
      height: 5rem;
      margin-inline: auto;
      border-radius: 3px;

      @media (min-width: 768px) {
        width: 6.8125rem;
        height: 6.8125rem;
      }

      :deep(img) {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
      }
    }

    h1 {
      margin-top: 1rem;
      margin-bottom: 0;
      font-family: var(--font-family-heading);
      font-size: 1.5rem;
      font-weight: 700;

      @media (min-width: 768px) {
        font-size: 2.25rem;
        margin-top: 2.5rem;
      }
    }
  }

  .chapter-scores {
    display: grid;
    gap: 0.38rem;

    @media (min-width: 768px) {
      gap: 1rem;
    }

    .score-box {
      display: flex;
      gap: 0.68rem;
      align-items: center;
      width: min(25rem, 100%);
      margin-inline: auto;
      padding: 0.5875rem 0.81rem;
      background: #dbe2ff;
      border-radius: 3px;
      font-size: 1.125rem;
      font-weight: 500;

      @media (min-width: 768px) {
        gap: 1.31rem;
        padding: 0.4125rem 1.62rem;
        font-size: 1.25rem;
      }

      .emoji {
        flex-shrink: 0;
        font-size: 1.5rem;

        @media (min-width: 768px) {
          font-size: 2.25rem;
        }
      }

      .score {
        font-size: 1.5rem;
        font-weight: 900;

        @media (min-width: 768px) {
          font-size: 2rem;
        }
      }
    }
  }

  .buttons {
    margin-top: 1.44rem;
    display: grid;
    gap: 0.68rem;

    @media (min-width: 768px) {
      margin-top: 4.75rem;
      gap: 0.875rem;
    }
  }
}
</style>
