<script setup lang="ts">
import type { Chapter } from '@/types'
import { computed, onMounted } from 'vue'
import { useStore } from '@/stores/store'
import ButtonPrimary from '@/components/ButtonPrimary.vue'

const props = defineProps<{ chapter: Chapter }>()

const store = useStore()

function onShareResult() {
  const message = 'TODO: message, skopiraj v odložišče...'
  window.alert(message)
}

const totalChapterScore = computed(() => {
  if (props.chapter.pages) {
    return props.chapter.pages.reduce((prev, curr) => {
      if (curr.type === 'quiz') {
        return prev + curr.points
      }
      return prev
    }, 0)
  }
  return 0
})

onMounted(() => {
  // save score and answers
  store.finishedChapters.set(props.chapter.id, {
    score: store.currentChapterScore,
    answers: new Map(store.currentChapterAnswers),
  })
  // unlock next chapter
  const chapterIds = [...store.chapters.keys()]
  const currentChapterIndex = chapterIds.findIndex(
    cid => cid === props.chapter.id,
  )
  const nextChapterId = chapterIds[currentChapterIndex + 1]
  if (nextChapterId) {
    store.justUnlockedChapters.push(nextChapterId)
    store.unlockedChapters.push(nextChapterId)
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
      <img
        v-if="chapter.image"
        :src="chapter.image.url"
        :alt="chapter.image.alt"
        :width="chapter.image.width"
        :height="chapter.image.height"
      />
      <h1>{{ chapter.title }}</h1>
    </div>
    <div>
      <p>
        Zbranih točk: {{ store.currentChapterScore }}/{{ totalChapterScore }}
      </p>
      <p>Pravilni odgovori: 0/0</p>
      <p>Skupaj točk: {{ store.score }}</p>
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
      max-width: 13rem;
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
    padding-bottom: 1rem;
    text-align: center;

    img {
      width: 5rem;
      height: 5rem;
      margin-inline: auto;
      object-fit: cover;
      object-position: center;
      border-radius: 3px;

      @media (min-width: 768px) {
        width: 6.8125rem;
        height: 6.8125rem;
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

  .buttons {
    display: grid;
    gap: 0.68rem;

    @media (min-width: 768px) {
      gap: 0.88rem;
    }
  }
}
</style>
