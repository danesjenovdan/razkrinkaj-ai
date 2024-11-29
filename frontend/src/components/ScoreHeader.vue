<script setup lang="ts">
defineProps<{
  title: string
  score: number
}>()
</script>

<template>
  <header class="score-header">
    <div class="header-content">
      <RouterLink :to="{ name: 'intro' }">
        <div class="title">
          <img
            src="/razkrinkaj-ai-logo.png"
            alt="Razkrinkaj.ai"
            class="title-logo"
          />
        </div>
      </RouterLink>
      <div class="score">
        <strong>{{ score }}</strong> točk
      </div>
    </div>
  </header>
</template>

<style scoped lang="scss">
.score-header {
  margin-inline: calc(var(--page-gutter) * -1);
  padding-inline: var(--page-gutter);
  background: var(--color-bg-white);
  border-bottom: 0.5px solid #000;

  .header-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: var(--page-width);
    margin-inline: auto;

    .title {
      display: flex;
      font-size: 1.375rem;

      @media (min-width: 768px) {
        font-size: 1.75rem;
      }

      img {
        width: auto;
        height: 1em;
        margin-top: 0.125em;
      }
    }

    .score {
      margin-block: 1rem;
      font-size: 1.125rem;
      line-height: 1;

      strong {
        font-weight: 700;
      }
    }
  }
}
</style>
