<script setup lang="ts">
import type { Chapter } from '@/types'

const props = defineProps<{
    chapter: Chapter
}>()

</script>

<template>
    <RouterLink :to="{ name: 'chapter-intro', params: { id: chapter.id } }" class="chapter"
        :class="{ 'disabled': chapter.locked_by_default }">
        <span>
            {{ chapter.title }}
        </span>
        <!-- <span class="icon">finished</span>
        <span class="icon">locked</span> -->
    </RouterLink>
</template>

<style lang="scss">
.chapter {
    display: flex;
    padding: 10px;
    margin: 10px 0;
    background-color: white;
    color: black;
    text-decoration: none;

    &.disabled {
        pointer-events: none;
    }
}
</style>