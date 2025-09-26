<script setup lang="ts">
import { useStore } from '@/stores/store'
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import PageFooter from '@/components/PageFooter.vue'
import ExplanationsSection from '@/components/ExplanationsSection.vue'

const store = useStore()

const scrollToMore = () => {
  document
    .querySelector('a[name="more"]')
    ?.scrollIntoView({ behavior: 'smooth' })
}
</script>

<template>
  <main>
    <div class="page-gutter bg-manipulacija-color-3">
      <div class="intro">
        <h1>
          <img
            src="/manipulacija-logo.svg"
            alt="Manipulacija ni informacija"
            class="title-logo"
          />
        </h1>
        <div class="narrow">
          <div class="description" v-html="store.introductionDescription"></div>
          <ButtonPrimary
            class="button"
            :buttonText="store.introductionButtonText"
            :link="{ name: 'calendar' }"
            icon="hands"
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
    </div>
    <div class="page-gutter bg-manipulacija-color-7">
      <div class="explanations">
        <a name="more"></a>
        <ExplanationsSection :update-hash="false" />
      </div>
    </div>
  </main>
  <PageFooter />
</template>

<style scoped lang="scss">
main {
  .intro {
    padding-top: 5.75rem;
    padding-bottom: 8.69rem;

    h1 {
      margin-top: 0;
      margin-bottom: 2.875rem;

      .title-logo {
        width: 100%;
        max-width: 960px;
        margin-inline: auto;
      }
    }

    .narrow {
      margin-inline: auto;
      max-width: 550px;

      .description {
        font-size: 1.5rem;
        font-weight: 500;
      }

      .button {
        margin-top: 2.875rem;
        margin-inline: auto;
        max-width: 404px;
      }
    }
  }

  .explanations {
    padding-top: 7.4375rem;
    padding-bottom: 8.8125rem;
  }
}
</style>
