<script setup lang="ts">
import type { Chapter } from '@/types'
import { computed, onMounted } from 'vue'
import { useStore } from '@/stores/store'
import ThumbnailImage from './ThumbnailImage.vue'
import { preloadPageImages } from '@/utils/image'

const props = defineProps<{
  chapter: Chapter
}>()

const store = useStore()

const isFinished = computed(() => store.finishedChapters.has(props.chapter.id))
const isJustUnlocked = computed(() =>
  store.justUnlockedChapters.includes(props.chapter.id),
)
const isLocked = computed(() => {
  return (
    props.chapter.locked_by_default &&
    !store.unlockedChapters.includes(props.chapter.id)
  )
})

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
  <RouterLink
    :class="{ chapter: true, disabled: isLocked, completed: isFinished }"
    :to="{ name: 'chapter-intro', params: { id: chapter.id } }"
  >
    <div class="text-col">
      <h2 class="title">{{ chapter.title }}</h2>
      <div class="description">{{ chapter.description }}</div>
      <div v-if="!isFinished && !isLocked" class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 38.614 31.987">
          <path
            d="M3.307 14.02v1.333zm-1.413.592-.95-.933Zm-.56 1.419-1.333.026v.027zm2.05 1.936v-1.334h-.018zm24.494 0v-1.334zm.779.325.944-.944zm.325.779h1.333zm-.325.78.944.945zm-7.448 7.452.944.944zm-.58 1.413-1.332.013 1.333-.01zm.606 1.405-.922.96.024.024zm1.432.53.038 1.334zm1.392-.612-.944-.944-.013.013zm12.648-12.643.942.941zm0-2.8.942-.939zM24.054 1.95l-.957.928.013.013zm-1.395-.614L22.7.004zm-1.426.534L20.33.884l-.021.024.923.96zm-.606 1.4 1.334.013zm.579 1.413.944-.941zm7.45 7.453.945-.941zm.326.782h1.333zm-.325.78.944.942zm-.78.324v1.333zM3.306 12.689a3.307 3.307 0 0 0-2.36.992l1.901 1.867a.64.64 0 0 1 .456-.192zm-2.363.992a3.307 3.307 0 0 0-.941 2.376l2.666-.053a.64.64 0 0 1 .182-.459ZM.001 16.09a3.353 3.353 0 0 0 1.048 2.299l1.832-1.939a.69.69 0 0 1-.216-.472Zm1.048 2.299a3.36 3.36 0 0 0 2.354.915l-.04-2.667a.688.688 0 0 1-.482-.187Zm2.336.915h24.493v-2.667H3.388Zm24.49 0a.227.227 0 0 1-.16-.067l1.886-1.885a2.44 2.44 0 0 0-1.723-.715zm-.16-.067a.227.227 0 0 1-.066-.16h2.666a2.44 2.44 0 0 0-.714-1.725zm-.066-.16a.22.22 0 0 1 .066-.163l1.886 1.886a2.437 2.437 0 0 0 .714-1.726zm.066-.163-7.448 7.446 1.886 1.888 7.448-7.451zm-7.448 7.446a3.307 3.307 0 0 0-.97 2.373l2.666-.027a.64.64 0 0 1 .187-.458Zm-.97 2.373c.01.888.373 1.733 1.016 2.35l1.848-1.92a.64.64 0 0 1-.198-.457zm1.04 2.373a3.365 3.365 0 0 0 2.365.88l-.08-2.666a.693.693 0 0 1-.485-.182zm2.365.88a3.364 3.364 0 0 0 2.312-1.018l-1.915-1.86a.693.693 0 0 1-.474.212zM25 30.98l12.645-12.64-1.885-1.888-12.646 12.643Zm12.645-12.643a3.31 3.31 0 0 0 .968-2.341h-2.667a.648.648 0 0 1-.186.459zm.968-2.341c0-.877-.347-1.717-.968-2.339L35.76 15.54a.648.648 0 0 1 .186.456zm-.968-2.341L25 1.004l-1.888 1.885L35.76 15.54ZM25.014 1.02A3.36 3.36 0 0 0 22.702.001l-.077 2.667a.69.69 0 0 1 .474.208zM22.702.001a3.36 3.36 0 0 0-2.365.883l1.8 1.965a.693.693 0 0 1 .488-.181zm-2.39.904a3.307 3.307 0 0 0-1.013 2.35l2.667.026a.64.64 0 0 1 .195-.453zM19.3 3.255a3.307 3.307 0 0 0 .968 2.373L22.15 3.74a.64.64 0 0 1-.187-.459l-2.666-.026zm.968 2.373 7.45 7.445 1.886-1.885-7.45-7.45zm7.45 7.445a.227.227 0 0 1-.066-.16h2.667a2.44 2.44 0 0 0-.715-1.722zm-.066-.16a.22.22 0 0 1 .064-.16l1.888 1.883a2.44 2.44 0 0 0 .715-1.723zm.067-.162a.227.227 0 0 1 .16-.067l.003 2.667a2.44 2.44 0 0 0 1.722-.715zm.16-.067H3.308v2.667h24.575Z"
          />
          <path
            d="M3.307 14.02a1.973 1.973 0 0 0-1.973 2.013 2.024 2.024 0 0 0 2.053 1.936h24.494a1.107 1.107 0 0 1 .778 1.886l-7.45 7.448a1.973 1.973 0 0 0 .026 2.818 2.027 2.027 0 0 0 2.822-.082l12.648-12.643a1.981 1.981 0 0 0 0-2.8L24.054 1.95a2.024 2.024 0 0 0-2.821-.08 1.973 1.973 0 0 0-.027 2.816l7.45 7.45a1.107 1.107 0 0 1-.778 1.886z"
            fill="#ebf374"
          />
        </svg>
      </div>
    </div>
    <div class="image-col">
      <ThumbnailImage v-if="chapter.image" :image="chapter.image" />
    </div>
    <div class="lock-icons">
      <div v-if="isFinished" class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 21 21">
          <circle
            cx="10.5"
            cy="10.5"
            r="10.25"
            fill="#4063F6"
            stroke="#000"
            stroke-width=".5"
          />
          <path
            fill="#fff"
            stroke="#000"
            stroke-width=".5"
            d="m4.25 10.084-.195.187a.99.99 0 0 0 0 1.43l3.368 3.257a1.051 1.051 0 0 0 1.453 0l8.069-7.803a.992.992 0 0 0 0-1.43l-.706-.683a1.051 1.051 0 0 0-1.454 0L8.15 11.46 6.215 9.59a1.044 1.044 0 0 0-.727-.292c-.273 0-.532.103-.727.292l-.512.495Z"
          />
        </svg>
      </div>
      <div v-if="isJustUnlocked" class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 21 21">
          <circle
            cx="10.5"
            cy="10.5"
            r="10.25"
            fill="#EBF374"
            stroke="#000"
            stroke-width=".5"
          />
          <path
            fill="#000"
            d="M14.485 17H6.703A.704.704 0 0 1 6 16.297V9.318c0-.387.316-.703.704-.703h7.781c.388 0 .703.316.703.703v6.98a.704.704 0 0 1-.703.702ZM6.703 9.096c-.123 0-.222.1-.222.222v6.98c0 .122.1.222.222.222h7.781c.123 0 .223-.1.223-.222v-6.98c0-.122-.1-.222-.223-.222H6.703Z"
          />
          <path
            fill="#fff"
            d="M6.703 9.096c-.123 0-.222.1-.222.222v6.98c0 .122.1.222.222.222h7.781c.123 0 .223-.1.223-.222v-6.98c0-.122-.1-.222-.223-.222H6.703Z"
          />
          <path
            fill="#000"
            d="M8.304 9.096a.24.24 0 0 1-.24-.24V6.687a2.515 2.515 0 0 1 .74-1.79 2.528 2.528 0 0 1 3.58 0 2.527 2.527 0 0 1 .742 1.79v.048h.77a3.305 3.305 0 0 0-3.3-3.254 3.305 3.305 0 0 0-3.302 3.301v2.073a.24.24 0 1 1-.48 0V6.783a3.767 3.767 0 0 1 1.108-2.674A3.767 3.767 0 0 1 10.595 3a3.766 3.766 0 0 1 2.674 1.108 3.767 3.767 0 0 1 1.108 2.674v.193a.24.24 0 0 1-.24.24h-1.251a.24.24 0 0 1-.24-.24v-.288c0-1.13-.92-2.05-2.05-2.05s-2.05.92-2.05 2.05v2.169a.244.244 0 0 1-.243.24Z"
          />
          <path
            fill="#fff"
            d="M7.294 8.615h.77V6.687a2.515 2.515 0 0 1 .74-1.79 2.528 2.528 0 0 1 3.58 0 2.527 2.527 0 0 1 .742 1.79v.048h.77a3.305 3.305 0 0 0-3.3-3.254 3.305 3.305 0 0 0-3.302 3.301v1.833Z"
          />
          <path
            fill="#000"
            d="M11.222 14.548H9.966a.24.24 0 0 1-.24-.24v-1.31a1.161 1.161 0 1 1 2.028-.77c0 .283-.105.558-.292.77v1.31a.24.24 0 0 1-.24.24Zm-1.015-.48h.774V12.9a.24.24 0 0 1 .077-.176.68.68 0 1 0-.928 0 .24.24 0 0 1 .076.176v1.167Z"
          />
          <path
            fill="#F5FE94"
            d="M10.207 14.067h.774V12.9a.24.24 0 0 1 .077-.176.68.68 0 1 0-.928 0 .24.24 0 0 1 .076.176v1.167Z"
          />
          <path
            fill="#000"
            d="m15.646 6.558.7-.743a.204.204 0 0 0-.297-.28l-.7.743a.204.204 0 0 0 .297.28Zm1.306.191-1.155.034a.204.204 0 1 0 .012.408l1.155-.034a.204.204 0 0 0-.012-.408Zm-1.422.824a.204.204 0 0 0 .01.289l.594.56a.204.204 0 0 0 .28-.297l-.594-.56a.204.204 0 0 0-.29.008Z"
          />
        </svg>
      </div>
      <div v-if="isLocked" class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 21 21">
          <circle
            cx="10.5"
            cy="10.5"
            r="10.25"
            fill="#F8F8F4"
            stroke="#8F94A3"
            stroke-width=".5"
          />
          <path
            fill="#8F94A3"
            d="M14.311 17H6.69a.697.697 0 0 1-.69-.703V9.318c0-.387.31-.703.69-.703h7.621c.38 0 .689.316.689.703v6.98a.697.697 0 0 1-.689.702ZM6.69 9.096a.22.22 0 0 0-.218.222v6.98a.22.22 0 0 0 .218.222h7.622c.12 0 .218-.1.218-.222v-6.98a.22.22 0 0 0-.218-.222H6.689Z"
          />
          <path
            fill="#8F94A3"
            d="M13.969 9.096a.238.238 0 0 1-.236-.24V6.782c0-1.82-1.45-3.3-3.233-3.3-1.783 0-3.234 1.48-3.234 3.3v2.073a.238.238 0 0 1-.235.241.238.238 0 0 1-.235-.24V6.782A3.817 3.817 0 0 1 7.88 4.108c.34-.347.736-.62 1.178-.81A3.62 3.62 0 0 1 10.5 3c.5 0 .985.1 1.441.297.442.19.838.464 1.178.81a3.83 3.83 0 0 1 1.085 2.674v2.075a.24.24 0 0 1-.236.24Z"
          />
          <path
            fill="#8F94A3"
            d="M12.744 9.096a.238.238 0 0 1-.236-.24V6.687c0-1.13-.9-2.05-2.008-2.05-1.107 0-2.008.92-2.008 2.05v2.169c0 .132-.105.24-.235.24a.238.238 0 0 1-.236-.24V6.687a2.56 2.56 0 0 1 .726-1.79c.228-.232.493-.414.788-.542.307-.132.63-.2.966-.2a2.464 2.464 0 0 1 1.753.741 2.558 2.558 0 0 1 .726 1.79v2.17a.24.24 0 0 1-.236.24Z"
          />
          <path
            fill="#F6F7F4"
            d="M7.266 8.615h.755V6.687a2.56 2.56 0 0 1 .726-1.79c.228-.232.493-.414.788-.542.307-.132.63-.2.966-.2a2.464 2.464 0 0 1 1.753.741 2.558 2.558 0 0 1 .726 1.79v1.93h.753V6.781c0-1.82-1.45-3.3-3.233-3.3-1.783 0-3.234 1.48-3.234 3.3v1.833Zm-.577.481a.22.22 0 0 0-.218.222v6.98a.22.22 0 0 0 .218.222h7.622c.12 0 .218-.1.218-.222v-6.98a.22.22 0 0 0-.218-.222H6.689Z"
          />
          <path
            fill="#8F94A3"
            d="M11.038 14.555H9.962a.238.238 0 0 1-.235-.24v-1.328a1.131 1.131 0 0 1-.33-.802c0-.62.495-1.125 1.103-1.125s1.102.505 1.102 1.125c0 .306-.118.592-.329.802v1.328c0 .133-.105.24-.235.24Zm-.84-.48h.604v-1.196c0-.073.033-.143.09-.189a.646.646 0 0 0 .24-.505.64.64 0 0 0-.632-.645.639.639 0 0 0-.632.645c0 .198.088.382.24.505.056.046.09.115.09.189v1.196Z"
          />
          <path
            fill="#ECEEE8"
            d="M10.197 14.075h.606v-1.196c0-.073.032-.143.089-.189a.646.646 0 0 0 .24-.505.64.64 0 0 0-.632-.645.639.639 0 0 0-.632.645c0 .198.088.382.24.505.056.046.09.115.09.189v1.196Z"
          />
        </svg>
      </div>
    </div>
  </RouterLink>
</template>

<style scoped lang="scss">
.chapter {
  position: relative;
  display: flex;
  gap: 0.56rem;
  padding: 0.56rem;
  background: var(--color-bg-white);
  border-radius: 3px;
  border: 0.5px solid #000;
  text-decoration: none;

  @media (min-width: 768px) {
    padding: 0.625rem;
  }

  .text-col {
    flex-grow: 1;
    display: flex;
    flex-direction: column;

    @media (min-width: 768px) {
      padding: 0.25rem;
      padding-right: 0;
    }

    .title {
      margin: 0;
      font-family: var(--font-family-heading);
      font-size: 1.25rem;
      font-weight: 700;

      @media (min-width: 768px) {
        font-size: 1.625rem;
      }
    }

    .description {
      margin-top: 0.25rem;
      margin-bottom: auto;
      font-size: 1rem;
      line-height: 1.1;
      white-space: pre-line;

      @media (min-width: 768px) {
        font-size: 1.25rem;
      }
    }

    .icon {
      display: flex;
      margin-top: 0.5rem;
      width: 0.875rem;
      height: 0.875rem;

      @media (min-width: 768px) {
        margin-top: 0.75rem;
        width: 1.125rem;
        height: 1.125rem;
      }

      svg {
        width: 100%;
        height: 100%;
      }
    }
  }

  .image-col {
    flex-shrink: 0;

    .thumbnail-image {
      width: 5rem;
      height: 5rem;
      border-radius: 3px;

      @media (min-width: 768px) {
        width: 6.8125rem;
        height: 6.8125rem;
      }

      :deep(img),
      :deep(svg) {
        width: 100%;
        height: 100%;
        object-fit: cover;
        object-position: center;
      }

      :deep(svg) {
        *[fill='#9BF37E' i],
        *[fill='#9BF47E' i] {
          fill: #ebf578;
        }

        *[stroke='#9BF37E' i],
        *[stroke='#9BF47E' i] {
          stroke: #ebf578;
        }
      }
    }
  }

  .lock-icons {
    position: absolute;
    top: 0.25rem;
    right: 0.25rem;

    .icon {
      width: 1.5rem;
      height: 1.5rem;

      @media (min-width: 768px) {
        width: 2rem;
        height: 2rem;
      }
    }
  }

  &.completed {
    .image-col {
      .thumbnail-image {
        :deep(svg) {
          *[fill='#9BF37E' i],
          *[fill='#9BF47E' i] {
            fill: #4063f6;
          }

          *[stroke='#9BF37E' i],
          *[stroke='#9BF47E' i] {
            stroke: #4063f6;
          }
        }
      }
    }
  }

  &.disabled {
    background: #fafafa;
    border-color: #8f94a3;
    color: #8f94a3;
    pointer-events: none;

    .image-col {
      .thumbnail-image {
        opacity: 0.75;

        :deep(svg) {
          *[fill='#9BF37E' i],
          *[fill='#9BF47E' i] {
            fill: #fafafa;
          }

          *[stroke='#9BF37E' i],
          *[stroke='#9BF47E' i] {
            stroke: #fafafa;
          }
        }
      }
    }
  }
}
</style>
