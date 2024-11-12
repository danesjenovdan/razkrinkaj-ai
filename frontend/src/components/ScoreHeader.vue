<script setup lang="ts">
defineProps<{
  title: string
  score: number
}>()
</script>

<template>
  <header class="score-header">
    <div class="header-content">
      <span class="title">{{ title }}</span>
      <span class="score">
        <strong>{{ score }}</strong> točk
      </span>
    </div>
  </header>
</template>

<style scoped lang="scss">
.score-header {
  margin-inline: calc(var(--page-gutter) * -1);
  padding-inline: var(--page-gutter);
  border-bottom: 0.5px solid #000;

  .header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;

    .score {
      display: block;
      margin-block: 0.75rem;
      font-size: 0.875rem;

      strong {
        font-weight: 700;
      }
    }
  }
}
</style>
