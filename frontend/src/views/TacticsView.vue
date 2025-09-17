<script setup lang="ts">
import PageFooter from '@/components/PageFooter.vue'
import ExplanationsSection from '@/components/ExplanationsSection.vue'
</script>

<template>
  <main>
    <div class="page-gutter bg-manipulacija-color-7">
      <div class="explanations">
        <ExplanationsSection :update-hash="true" />
      </div>
    </div>
  </main>
  <PageFooter />
</template>

<style scoped lang="scss">
main {
  .explanations {
    padding-block: 5rem;
  }
}
</style>
