<script setup lang="ts">
import type { Chapter } from '@/types'

const props = defineProps<{
    chapter: Chapter
}>()

</script>

<template>
    <RouterLink :to="{ name: 'chapter-intro', params: { id: 1 } }">
        {{ chapter.title }}
    </RouterLink>
</template>

<style lang="scss">

</style>