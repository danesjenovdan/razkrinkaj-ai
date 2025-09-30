<script setup lang="ts">
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStore } from '@/stores/store'
import ScoreHeader from '@/components/ScoreHeader.vue'
import CalendarDay from '@/components/CalendarDay.vue'
import PageFooter from '@/components/PageFooter.vue'
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import ExplanationsSection from '@/components/ExplanationsSection.vue'

const router = useRouter()
const route = useRoute()
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
  <div class="bg-manipulacija-color-3">
    <ScoreHeader
      :title="store.introductionTitle"
      :description="store.introductionDescription"
      :score="store.score"
    />
    <main>
      <div class="page-gutter">
        <div class="intro">
          <!-- <div
            class="introduction"
            v-html="store.introductionDescription"
          ></div> -->
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
            v-if="route.query.showReset === '1'"
            class="button"
            buttonText="Začni znova"
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
          <ExplanationsSection :update-hash="false" />
        </div>
      </div>
    </main>
  </div>
  <PageFooter />
</template>

<style scoped lang="scss">
main {
  .intro {
    padding-block: 3rem;
    max-width: 550px;
    margin-inline: auto;

    @media (max-width: 576px) {
      padding-block: 2rem;
    }

    .introduction {
      font-size: 1.5rem;
      font-weight: 500;
      text-align: center;
    }

    .title {
      margin-bottom: 1rem;
      font-size: 2.25rem;
      text-align: center;
      text-transform: uppercase;

      @media (max-width: 576px) {
        font-size: 1.75rem;
      }
    }

    .description {
      font-size: 1.5rem;
      font-weight: 500;
      text-align: center;

      @media (max-width: 576px) {
        font-size: 1.125rem;
      }
    }
  }

  .calendar {
    display: grid;
    align-content: start;
    justify-content: center;
    grid-template-columns: repeat(auto-fit, 8.5625rem);
    gap: 1.25rem;
    width: 100%;
    max-width: min(1080px, 100%);
    margin-inline: auto;

    @media (max-width: 576px) {
      grid-template-columns: repeat(auto-fit, minmax(6rem, 1fr));
      gap: 0.75rem;
    }
  }

  .buttons {
    margin-inline: auto;
    padding-block: 4.625rem 7.75rem;
    max-width: 550px;

    @media (max-width: 576px) {
      padding-block: 2rem 3rem;
    }

    .button {
      margin-top: 2.875rem;
      margin-inline: auto;
      max-width: 404px;

      @media (max-width: 576px) {
        margin-top: 1.5rem;
      }
    }
  }

  .explanations {
    padding-top: 7.4375rem;
    padding-bottom: 8.8125rem;

    @media (max-width: 576px) {
      padding-block: 2rem 2rem;
    }
  }
}
</style>
