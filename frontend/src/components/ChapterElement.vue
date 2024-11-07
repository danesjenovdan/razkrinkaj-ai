<script setup lang="ts">
import type { Chapter } from '@/types'

defineProps<{
  chapter: Chapter
}>()
</script>

<template>
  <RouterLink
    class="chapter"
    :to="{ name: 'chapter-intro', params: { id: chapter.id } }"
  >
    <div class="text-col">
      <h2 class="title">{{ chapter.title }}</h2>
      <div class="description">{{ chapter.description }}</div>
    </div>
    <div class="image-col">
      <img :src="chapter.image" alt="chapter image" />
    </div>
    <!-- <span v-if="chapter.id in store.finishedChapters" class="icon"
      >finished</span
    > -->
    <!-- <span class="icon">locked</span> -->
  </RouterLink>
</template>

<style lang="scss">
.chapter {
  display: flex;
  padding: 0.5rem 0.625rem;
  border-radius: 3px;
  border: 0.5px solid #000;
  text-decoration: none;

  .text-col {
    flex-grow: 1;

    .title {
      margin: 0;
      font-family: var(--font-family-heading);
      font-size: 1rem;
      font-weight: 700;
    }

    .description {
      margin-top: 0.25rem;
      font-size: 0.625rem;
      line-height: 1.1;

      // limit to 3 rows
      display: -webkit-box;
      line-clamp: 3;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
  }

  .image-col {
    flex-shrink: 0;

    img {
      width: 5rem;
      height: 5rem;
      object-fit: cover;
      object-position: center;
      border-radius: 3px;
    }
  }

  &.disabled {
    pointer-events: none;
  }
}
</style>
