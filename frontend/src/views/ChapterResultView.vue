<script setup lang="ts">
import type { Chapter } from '@/types'
import { useStore } from '@/stores/store'
import ButtonPrimary from '@/components/ButtonPrimary.vue'

defineProps<{ chapter: Chapter }>()

const store = useStore()

function onShareResult() {
  const message = 'TODO: message, skopiraj v odložišče...'
  window.alert(message)
}
</script>

<template>
  <main>
    <div class="results-header">
      <h1>Poglavje zaključeno!</h1>
    </div>
    <div class="chapter-info">
      <img :src="chapter.image" alt="chapter image" />
      <h1>{{ chapter.title }}</h1>
    </div>
    <div>
      <p>Zbranih točk: 0/0</p>
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
  padding-bottom: 3.5rem;

  .results-header {
    margin-inline: calc(var(--page-gutter) * -1);
    padding-inline: var(--page-gutter);
    margin-bottom: -1.5rem;
    padding-block: 2.4rem;
    background: #4063f6;
    border-bottom: 0.5px solid #000;
    text-align: center;

    h1 {
      max-width: 13rem;
      margin-inline: auto;
      margin-bottom: 0.3rem;
      font-family: var(--font-family-heading);
      font-size: 1.3125rem;
      font-weight: 700;
      line-height: 1;
      color: #fff;
      text-transform: uppercase;
    }
  }

  .chapter-info {
    padding-bottom: 2.4rem;
    text-align: center;

    img {
      width: 5rem;
      height: 5rem;
      margin-inline: auto;
      object-fit: cover;
      object-position: center;
      border-radius: 3px;
    }

    h1 {
      margin-top: 1.1rem;
      margin-bottom: 0.25rem;
      font-family: var(--font-family-heading);
      font-size: 1.3125rem;
      font-weight: 700;
    }
  }

  .buttons {
    display: grid;
    gap: 0.68rem;
  }
}
</style>
