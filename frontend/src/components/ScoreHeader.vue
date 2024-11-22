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
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 626.4 86.2"
            fill="currentColor"
            role="img"
          >
            <title>Razkrinkaj.ai</title>
            <path
              d="M195.4 72.2h-16.8v-70h16.8v33.9h9.6l9.8-19.9h18.8l-14.8 25.9 15.8 30.1h-19l-10.1-22.1h-10.1v22.1Zm196.6 0h-16.8v-70H392v33.9h9.6l9.8-19.9h18.8l-14.8 25.9 15.8 30.1h-19l-10.1-22.1H392v22.1Zm-62 0h-16.8v-56h40.4l12 12v44h-16.8V30.8H330v41.4ZM44.4 2.2l12.2 12.2v25.3l-8.1 8.1 12.1 24.4H41.8l-8.9-19.8H16.8v19.8H0v-70h44.4Zm127 70h-48.2v-12l27.3-30h-27v-14h47.7v12l-27.3 30h27.5v14Zm-94.8 0-12-12v-20l34.6-1v-9H66.6v-14H104l12 12v44H76.6Zm370.8 0-12-12v-20l34.6-1v-9h-32.6v-14h37.4l12 12v44h-39.4Zm113.2 0-12-12v-20l34.6-1v-9h-32.6v-14H588l12 12v44h-39.4Zm-304 0h-16.8v-44l12-12H280v15.2h-23.4v40.8Zm256.6 14h-16.8v-70h16.8v70Zm-209.6-14h-16.8v-56h16.8v56Zm322.8 0h-16.8v-56h16.8v56ZM16.8 15.6V39h23V15.6h-23Zm522.4 56.6h-15.6v-16h15.6v16Zm-440-24.8-17.8 2v9.4h17.8V47.4Zm370.8 0-17.8 2v9.4H470V47.4Zm113.2 0-17.8 2v9.4h17.8V47.4ZM303.6 11h-16.8V0h16.8v11Zm209.6 0h-16.8V0h16.8v11Zm113.2 0h-16.8V0h16.8v11Z"
            />
          </svg>
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
      font-size: 1rem;

      @media (min-width: 768px) {
        font-size: 1.25rem;
      }

      svg {
        width: auto;
        height: 1em;
        margin-top: 0.125em;
      }
    }

    .score {
      margin-block: 0.75rem;
      font-size: 0.875rem;

      strong {
        font-weight: 700;
      }
    }
  }
}
</style>
