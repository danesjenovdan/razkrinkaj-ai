<script setup lang="ts">
import type { Chapter } from '@/types'
import { computed, onMounted } from 'vue'
import { useStore } from '@/stores/store'
import { preloadPageImages } from '@/utils/image'
import StarIcon from './StarIcon.vue'
import LockIcon from './LockIcon.vue'
import { slugifyDot } from '@/utils/stringify'

const props = defineProps<{
  chapter: Chapter
}>()

const store = useStore()

const chapterDate = computed(() => {
  const dateParts = props.chapter.title.split('.').map(Number)
  return new Date(dateParts[2], dateParts[1] - 1, dateParts[0])
})

const chapterSlug = computed(() => {
  return slugifyDot(props.chapter.title)
})

const isFinished = computed(() => store.finishedChapters.has(props.chapter.id))
const isLocked = computed(() => {
  const date = chapterDate.value
  const now = Date.now()
  return now < date.getTime()
})
const isToday = computed(() => {
  const date = chapterDate.value
  const today = new Date()
  return (
    date.getDate() === today.getDate() &&
    date.getMonth() === today.getMonth() &&
    date.getFullYear() === today.getFullYear()
  )
})

const didAnswerCorrectly = computed<boolean | null>(() => {
  if (store.finishedChapters.has(props.chapter.id)) {
    const chapterData = store.finishedChapters.get(props.chapter.id)!
    const answers = Array.from(chapterData.answers.values())
    return answers.every(answer => answer.correct)
  } else if (store.inProgressChapters.has(props.chapter.id)) {
    const chapterData = store.inProgressChapters.get(props.chapter.id)!
    const answers = Array.from(chapterData.answers.values())
    return answers.every(answer => answer.correct)
  }
  return null
})
const starVariant = computed(() => {
  if (didAnswerCorrectly.value === true) {
    return 'success'
  } else if (didAnswerCorrectly.value === false) {
    return 'fail'
  }
  return 'regular'
})

const isHidden = computed(() => {
  if (props.chapter.is_feedback && (isLocked.value || isFinished.value)) {
    return true
  }
  return false
})

const componentName = computed(() => (!isLocked.value ? 'RouterLink' : 'span'))

onMounted(() => {
  if (!isLocked.value) {
    store.initChapterData(props.chapter.id).then(() => {
      const firstPage = props.chapter.pages?.[0]
      if (firstPage) {
        preloadPageImages(firstPage)
      }
    })
  }
})
</script>

<template>
  <component
    v-if="!isHidden"
    :is="componentName"
    :class="{
      'calendar-day': true,
      today: isToday && didAnswerCorrectly === null,
      disabled: isLocked,
      completed: isFinished,
      success: didAnswerCorrectly === true,
      fail: didAnswerCorrectly === false,
    }"
    :to="
      !isLocked
        ? { name: 'chapter-intro', params: { slug: chapterSlug } }
        : undefined
    "
  >
    <h2 class="title">{{ chapter.title }}</h2>
    <div v-if="isToday && didAnswerCorrectly === null" class="text">
      REŠI!
    </div>
    <div v-else-if="!isLocked" class="icon icon--star">
      <StarIcon :variant="starVariant" />
    </div>
    <div v-else-if="isLocked" class="icon icon--lock">
      <LockIcon />
    </div>
  </component>
</template>

<style scoped lang="scss">
@use '@sass-fairy/string';
@use '@sass-fairy/url';
@use '@/assets/variables' as vars;

.calendar-day {
  $day-bg-svg-string: '<svg viewBox="0 0 137 137" preserveAspectRatio="none" fill="#FFF"><path vector-effect="non-scaling-stroke" stroke="#000" stroke-width="3" d="M68.5 1.5c17.1615 0 29.9054.0027 39.436 1.0615 9.541 1.0602 15.531 3.152 19.441 7.0615 3.909 3.9096 6.001 9.9002 7.061 19.4415 1.059 9.5301 1.062 22.274 1.062 39.4355 0 17.1615-.003 29.9054-1.062 39.436-1.06 9.541-3.152 15.531-7.061 19.441-3.91 3.909-9.9 6.001-19.441 7.061-9.5306 1.059-22.2745 1.062-39.436 1.062s-29.9054-.003-39.4355-1.062c-9.5413-1.06-15.5319-3.152-19.4414-7.061-3.9096-3.91-6.0014-9.9-7.0616-19.441C1.5026 98.4054 1.5 85.6615 1.5 68.5s.0027-29.9054 1.0615-39.4355c1.0602-9.5413 3.152-15.5319 7.0615-19.4414 3.9096-3.9096 9.9002-6.0014 19.4415-7.0616C38.5946 1.5026 51.3385 1.5 68.5 1.5Z"/></svg>';
  $day-bg-svg-string-normal: string.replace(
    $day-bg-svg-string,
    '#FFF',
    '#{vars.$manipulacija-color-9}'
  );
  aspect-ratio: 1;
  padding: 1.125rem;
  background-image: url.svg($day-bg-svg-string-normal);
  background-repeat: no-repeat;
  background-size: 100% 100%;
  overflow: hidden;
  text-decoration: none;
  transition:
    scale 0.15s ease-in-out,
    rotate 0.15s ease-in-out,
    filter 0.15s ease-in-out;
  will-change: scale, rotate, filter;

  .title {
    margin-bottom: 0.625rem;
    font-size: 1rem;
    font-weight: 600;
    text-align: center;
  }

  .icon {
    width: 5rem;
    height: 4.8125rem;
    margin-inline: auto;

    &.icon--lock {
      width: 2.875rem;
    }

    svg {
      width: 100%;
      height: 100%;
    }
  }

  .text {
    font-family: var(--font-family-alt);
    font-size: 2.25rem;
    font-weight: 600;
    line-height: 2;
    text-align: center;
  }

  &.success {
    $day-bg-svg-string-success: string.replace(
      $day-bg-svg-string,
      '#FFF',
      '#D8FFAF'
    );
    background-image: url.svg($day-bg-svg-string-success);
  }

  &.fail {
    $day-bg-svg-string-fail: string.replace(
      $day-bg-svg-string,
      '#FFF',
      '#FFBA9E'
    );
    background-image: url.svg($day-bg-svg-string-fail);
  }

  &.today {
    $day-bg-svg-string-today: string.replace(
      $day-bg-svg-string,
      '#FFF',
      '#{vars.$manipulacija-color-5}'
    );
    $day-bg-svg-string-today: string.replace(
      $day-bg-svg-string-today,
      '<path ',
      '<defs><filter id="shadow"><feFlood flood-color="#FF9E01" /><feComposite operator="out" in2="SourceGraphic" /><feMorphology operator="dilate" radius="2" /><feGaussianBlur stdDeviation="6" /><feComposite operator="atop" in2="SourceGraphic" /></filter></defs><path filter="url(#shadow)" '
    );
    $day-bg-svg-string-today-border: string.replace(
      $day-bg-svg-string,
      '#FFF',
      'none'
    );
    background-image: url.svg($day-bg-svg-string-today-border),
      url.svg($day-bg-svg-string-today);

    .title {
      font-weight: 700;
    }
  }

  &.disabled {
    $day-bg-svg-string-disabled: string.replace(
      $day-bg-svg-string,
      '#FFF',
      '#FFF'
    );
    background-image: url.svg($day-bg-svg-string-disabled);
  }

  &:not(.disabled):hover {
    rotate: 3deg;
    scale: 1.05;
    filter: drop-shadow(0 0 4px var(--manipulacija-color-4));
  }
}
</style>
