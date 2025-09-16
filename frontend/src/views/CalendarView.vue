<script setup lang="ts">
import { onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from '@/stores/store'
import ScoreHeader from '@/components/ScoreHeader.vue'
import CalendarDay from '@/components/CalendarDay.vue'
import PageFooter from '@/components/PageFooter.vue'
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import ExplanationsSection from '@/components/ExplanationsSection.vue'

const router = useRouter()
const store = useStore()

function onResetClick() {
  if (
    window.confirm(
      'Ali ste prepričani, da želite začeti znova? To bo izbrisalo vse odgovore.',
    )
  ) {
    store.clearAllProgress()
    router.push({ name: 'intro' })
  }
}

const scrollToMore = () => {
  document
    .querySelector('a[name="more"]')
    ?.scrollIntoView({ behavior: 'smooth' })
}

onMounted(() => {
  store.clearCurrentChapter()
})
</script>

<template>
  <ScoreHeader :title="store.introductionTitle" :score="store.score" />
  <main>
    <div class="page-gutter">
      <div class="intro">
        <h1 class="title">Preizkusi svoje spretnosti</h1>
        <div class="description">
          Vsak dan v mesecu objavimo manipulativen citat.<br />
          Ugotovi za katero vrsto manipulacije gre.
        </div>
      </div>
      <div class="calendar">
        <CalendarDay
          v-for="[id, chapter] in store.chapters"
          :key="id"
          :chapter="chapter"
        />
      </div>
      <div class="buttons">
        <ButtonPrimary
          class="button"
          buttonText="Začni znova"
          icon="refresh"
          color="white"
          @click="onResetClick"
        />
        <ButtonPrimary
          class="button"
          :buttonText="store.introductionButtonTextSecondary"
          href="#more"
          color="secondary"
          side-icon="hand-down"
          @click.prevent="scrollToMore"
        />
      </div>
    </div>
    <div class="page-gutter bg-manipulacija-color-7">
      <div class="explanations">
        <a name="more"></a>
        <ExplanationsSection />
      </div>
    </div>
  </main>
  <PageFooter />
</template>

<style scoped lang="scss">
main {
  .intro {
    padding-block: 4.4375rem 3rem;

    h1 {
      margin-bottom: 1rem;
      font-size: 2.25rem;
      text-align: center;
      text-transform: uppercase;
    }

    .description {
      font-size: 1.5rem;
      text-align: center;
    }
  }

  .calendar {
    display: grid;
    align-content: start;
    justify-content: center;
    grid-template-columns: repeat(auto-fit, 8.5625rem);
    gap: 1.25rem;
    width: 100%;
    max-width: 1080px;
    margin-inline: auto;
  }

  .buttons {
    margin-inline: auto;
    padding-block: 4.625rem 7.75rem;
    max-width: 550px;

    .button {
      margin-top: 2.875rem;
      margin-inline: auto;
      max-width: 404px;
    }
  }

  .explanations {
    padding-top: 7.4375rem;
    padding-bottom: 8.8125rem;
  }
}
</style>
