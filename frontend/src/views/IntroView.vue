<script setup lang="ts">
import { useStore } from '@/stores/store'
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import PageFooter from '@/components/PageFooter.vue'

const store = useStore()
</script>

<template>
  <main>
    <div class="intro">
      <h1>{{ store.introductionTitle }}</h1>
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
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .intro {
    h1 {
      margin: 0;
      padding-block: 2rem;
    }

    .description {
      font-size: 1rem;

      @media (min-width: 768px) {
        font-size: 1.125rem;
      }
    }

    .button {
      margin-top: 1.5rem;

      // @media (min-width: 768px) {
      //   font-size: 1.5rem;
      //   padding: 1.2rem 2rem;
      // }
    }
  }
}
</style>
