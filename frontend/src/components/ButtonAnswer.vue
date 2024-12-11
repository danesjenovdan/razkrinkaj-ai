<script setup lang="ts">
import { useStore } from '@/stores/store'

defineProps<{
  buttonText: string
  correct: boolean
  revealed: boolean
  selected: boolean
  points: number
}>()

const store = useStore()

const chapter = store.chapters.get(store.currentChapterId)
if (!chapter) throw new Error('Chapter not found')
</script>

<template>
  <button
    type="button"
    :class="{
      'button-answer': true,
      'is-feedback': chapter.is_feedback,
      revealed: revealed,
      correct: revealed && correct && !chapter.is_feedback,
      incorrect: revealed && !correct && !chapter.is_feedback,
      selected: revealed && selected,
    }"
  >
    <span class="answer-left">
      <span v-if="!selected || chapter.is_feedback" class="circle"></span>
      <span v-else class="icon">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32.046">
          <path
            v-if="correct"
            fill="#99f37d"
            stroke="#000"
            d="M25.937 4.2 10.574 19.653l-4.51-4.54a2.294 2.294 0 0 0-3.265 0l-1.232 1.24-.396.4a2.324 2.324 0 0 0 0 3.273l7.773 7.821a2.3 2.3 0 0 0 3.26 0L30.829 9.115a2.326 2.326 0 0 0 0-3.276L29.2 4.199a2.3 2.3 0 0 0-3.26 0z"
          />
          <path
            v-else
            fill="#e49a85"
            stroke="#000"
            d="M5.75.497c-.725.017-1.41.28-1.933.802l-2.53 2.536c-1.19 1.19-1.04 3.253.33 4.627l7.559 7.57-7.557 7.565C.246 24.97.096 27.035 1.287 28.225l2.53 2.535c1.19 1.188 3.25 1.04 4.623-.333l7.558-7.568 7.559 7.568c1.374 1.374 3.436 1.521 4.623.333l2.535-2.535c1.187-1.19 1.04-3.255-.334-4.628l-7.559-7.566 7.558-7.57c1.375-1.372 1.522-3.436.335-4.626L28.18 1.3c-1.186-1.19-3.249-1.04-4.623.335L16 9.199 8.441 1.634C7.669.859 6.679.474 5.749.498Z"
          />
        </svg>
      </span>
      <span>{{ buttonText }}</span>
    </span>
    <span v-if="selected && points > 0" class="score">
      <strong>{{ correct ? '+' : '-' }} {{ points }}</strong>
      točk
    </span>
  </button>
</template>

<style scoped lang="scss">
@keyframes bounceIn {
  from,
  20%,
  40%,
  60%,
  80%,
  to {
    animation-timing-function: cubic-bezier(0.215, 0.61, 0.355, 1);
  }

  0% {
    opacity: 0;
    transform: scale3d(0.3, 0.3, 0.3);
  }

  20% {
    transform: scale3d(1.1, 1.1, 1.1);
  }

  40% {
    transform: scale3d(0.9, 0.9, 0.9);
  }

  60% {
    opacity: 1;
    transform: scale3d(1.03, 1.03, 1.03);
  }

  80% {
    transform: scale3d(0.97, 0.97, 0.97);
  }

  to {
    opacity: 1;
    transform: scale3d(1, 1, 1);
  }
}

.button-answer {
  --_color-bg: var(--color-bg-white);
  --_color-border: #000;
  --_color-shadow: transparent;

  display: flex;
  gap: 0.68rem;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 1.125rem 1.125rem;
  border-radius: 3px;
  border: 0.5px solid var(--_color-border);
  background: var(--_color-bg);
  font-family: var(--font-family-heading);
  font-size: 1.3125rem;
  line-height: 1;
  font-weight: 700;
  color: var(--_color-border);
  text-align: left;
  text-decoration: none;
  cursor: pointer;

  @media (min-width: 768px) {
    font-size: 1.5rem;
    padding-inline: 1.31rem 1.31rem;
    padding-block: 1.2rem;
  }

  .answer-left {
    display: flex;
    gap: 1rem;
    align-items: center;

    .circle,
    .icon {
      flex-shrink: 0;
      width: 1.5rem;
      height: 1.5rem;
      margin-block: -0.2em;

      @media (min-width: 768px) {
        width: 1.625rem;
        height: 1.625rem;
      }
    }

    .circle {
      border: 0.5px solid var(--_color-border);
      border-radius: 9999rem;
    }

    .icon {
      display: flex;

      svg {
        width: 100%;
        height: 100%;
      }
    }
  }

  .score {
    flex-shrink: 0;
    display: inline-block;
    padding: 0.125rem 0.3rem;
    background: var(--_color-shadow);
    border-radius: 3px;
    font-family: var(--font-family-base);
    font-size: 0.875rem;
    line-height: 1.3;
    font-weight: 400;
    animation: bounceIn 0.66s;

    @media (min-width: 768px) {
      font-size: 1rem;
    }

    strong {
      font-weight: 900;
    }
  }

  &.revealed {
    pointer-events: none;
    box-shadow: 0 0 6px 0 var(--_color-shadow) inset;

    &.selected {
      &.correct,
      &.is-feedback {
        --_color-bg: #f0ffeb;
        --_color-shadow: #99f37d;

        box-shadow:
          0 0 6px 0 var(--_color-shadow) inset,
          0 0 0 3px var(--_color-shadow);
      }

      &.is-feedback {
        .circle {
          background: #99f37d;
        }
      }

      &.incorrect {
        --_color-bg: #ffefeb;
        --_color-shadow: #e49a85;
      }
    }

    &:not(.selected) {
      box-shadow: 0 0 0 3px var(--_color-shadow);

      &.correct {
        --_color-shadow: #99f37d;
      }
    }
  }

  @at-root body:not(.is-ios) &:not(.revealed):hover {
    background: #eef1fc;
    box-shadow:
      0px 0px 6px 0px #173ac9 inset,
      0px 0px 7px -1px #4063f6;

    .circle {
      background: #4063f6;
    }
  }
}
</style>
