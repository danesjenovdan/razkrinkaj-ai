<script setup lang="ts">
import { useStore } from '@/stores/store'
import ButtonPrimary from '@/components/ButtonPrimary.vue'

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
        :link="{ name: 'chapters-list' }"
        emoji="🚀🚀🚀"
      />
    </div>
  </main>
</template>

<style scoped lang="scss">
.intro {
  padding-bottom: 3.5rem;

  h1 {
    margin: 0;
    padding-block: 2rem;
  }

  .description {
    font-size: 0.875rem;
  }

  .button {
    margin-top: 2rem;
  }
}
</style>
