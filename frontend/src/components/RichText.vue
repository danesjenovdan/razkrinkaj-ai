<script setup lang="ts">
defineProps<{
  title?: string
  content: string
}>()
</script>

<template>
  <div class="rich-text">
    <h1 v-if="title">{{ title }}</h1>
    <div class="rich-content" v-html="content"></div>
  </div>
</template>

<style scoped lang="scss">
.rich-text {
  padding-block: 1.5rem;

  h1 {
    font-family: var(--font-family-heading);
    font-size: 1.3125rem;
  }

  :deep(.rich-content) {
    h2,
    h3,
    h4 {
      font-family: var(--font-family-heading);
      font-weight: 600;
    }

    h2 {
      font-size: 1.125rem;
    }

    h3 {
      font-size: 1rem;
    }

    h4 {
      font-size: 0.875rem;
    }

    p,
    ul,
    ol {
      font-size: 0.75rem;
    }

    p:empty {
      display: none;
    }

    b,
    strong {
      font-weight: 700;
    }

    i,
    em {
      font-style: italic;
    }

    div:has(> iframe),
    img {
      font-size: 0.75rem;
      margin-block: 1em;
    }

    iframe {
      display: block;
      width: 100%;
      height: auto;
      aspect-ratio: 16 / 9;
    }

    img {
      display: block;
      width: 100%;
      height: auto;
      padding: 0.25rem;
      border-radius: 3px;
      border: 0.5px solid #000;
      background: var(--color-bg);
    }

    hr {
      height: 0;
      border: 0;
      border-top: 0.5px solid #000;
      margin-block: 1em;
    }
  }
}
</style>
