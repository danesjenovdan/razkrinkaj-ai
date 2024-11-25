<script setup lang="ts">
import { useStore } from '@/stores/store'
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import PageFooter from '@/components/PageFooter.vue'

const store = useStore()
</script>

<template>
  <main>
    <div class="intro">
      <img
        src="/razkrinkaj-ai-logo.png"
        alt="Razkrinkaj.ai"
        class="title-logo"
      />
      <div class="description" v-html="store.introductionDescription"></div>
      <ButtonPrimary
        class="button"
        :buttonText="store.introductionButtonText"
        :link="{ name: 'chapter-list' }"
        emoji="🚀🚀🚀"
      />
    </div>
  </main>
  <PageFooter />
</template>

<style scoped lang="scss">
main {
  padding-bottom: 2rem;

  @media (min-width: 768px) {
    padding-bottom: 3.38rem;
  }

  @media (min-width: 768px) {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .intro {
    .title-logo {
      width: 100%;
      max-width: 480px;
      padding-top: 2.31rem;
      padding-bottom: 1.88rem;
      margin-inline: auto;

      @media (min-width: 768px) {
        padding-top: 3.38rem;
        padding-bottom: 2.31rem;
      }
    }

    .description {
      font-size: 1rem;

      @media (min-width: 768px) {
        font-size: 1.3125rem;
      }

      :deep(a) {
        font-weight: 600;
        color: #092bba;
      }
    }

    .button {
      margin-top: 1.5rem;

      @media (min-width: 768px) {
        margin-top: 2.45rem;
      }
    }
  }
}
</style>
