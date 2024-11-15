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

    ul {
      list-style-type: none;
      padding-left: 0;

      li {
        position: relative;
        padding-inline-start: 0.95rem;

        &::before {
          content: '';
          position: absolute;
          left: 0;
          top: 0;
          width: 0.64rem;
          height: 1.3em;
          height: 1lh;
          background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 8"><path fill="%23000" d="M.549 3.366a.562.562 0 0 0-.392.157A.51.51 0 0 0 0 3.9c.006.14.07.271.176.367a.578.578 0 0 0 .395.147h6.816c.081 0 .16.03.217.086a.29.29 0 0 1 .09.207.286.286 0 0 1-.09.207L5.53 6.891a.511.511 0 0 0-.16.376c.001.14.062.274.168.372a.58.58 0 0 0 .785-.022l3.519-3.355a.513.513 0 0 0 .16-.371.513.513 0 0 0-.16-.371L6.322.163A.58.58 0 0 0 5.538.14a.512.512 0 0 0-.167.372.51.51 0 0 0 .16.376l2.074 1.977a.29.29 0 0 1 .09.207.287.287 0 0 1-.09.207.316.316 0 0 1-.217.086H.549Z"/></svg>');
          background-repeat: no-repeat;
          background-position: center;
        }
      }
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
      background: var(--color-bg-white);
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
