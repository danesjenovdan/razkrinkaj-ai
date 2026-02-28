<script setup lang="ts">
import { useStore } from "@/stores/store.ts";

defineProps<{
  buttonText: string;
  correct: boolean;
  revealed: boolean;
  selected: boolean;
  points: number;
}>();

const store = useStore();

const chapter = store.chapters.get(store.currentChapterId);
if (!chapter) throw new Error("Chapter not found");
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
    <div class="answer-left">
      <div class="icon">
        <img v-if="revealed && correct" src="/check.svg" alt="" />
        <img v-else-if="revealed && selected" src="/cross.svg" alt="" />
        <div v-else class="dot"></div>
      </div>
    </div>
    <div class="answer-text">{{ buttonText }}</div>
    <div class="answer-right">
      <div v-if="selected && points > 0 && correct" class="score">
        <strong>{{ correct ? "+" : "-" }}{{ points }}</strong>
        točk
      </div>
    </div>
  </button>
</template>

<style scoped lang="scss">
@use "@/assets/mixins";

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
  position: relative;
  display: flex;
  gap: 0.5rem;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 0.375rem 0.5rem;
  background: var(--color-bg-white);
  border: 2px solid var(--kvizle-color-2);
  font-size: 1.25rem;
  line-height: 1.3;
  font-weight: 500;
  color: var(--color-text);
  text-align: left;
  text-decoration: none;
  cursor: pointer;
  will-change: scale, filter;
  --_box-shadow-size: 1rem;

  @media (max-width: 576px) {
    padding-block: 0.25rem;
    font-size: 1rem;
    --_box-shadow-size: 0.5rem;
  }

  .answer-left {
    .icon {
      flex-shrink: 0;
      display: grid;
      place-items: center;
      width: 2.5rem;
      height: 2.5rem;

      @media (max-width: 576px) {
        width: 2rem;
        height: 2rem;
      }

      img {
        width: 100%;
        height: 100%;
      }

      .dot {
        width: 1.5rem;
        height: 1.5rem;
        border: 2px solid var(--kvizle-color-2);
        border-radius: 50%;

        @media (max-width: 576px) {
          width: 1.25rem;
          height: 1.25rem;
        }
      }
    }
  }

  .answer-text {
    flex: 1;
  }

  .answer-right {
    align-self: center;

    .score {
      flex-shrink: 0;
      margin-block: -1rem;
      font-size: 1rem;
      line-height: 1.3;
      font-weight: 600;
      color: var(--kvizle-color-2);
      animation: bounceIn 0.66s;

      @media (max-width: 576px) {
        font-size: 0.875rem;
      }

      strong {
        font-family: var(--font-family-alt);
        font-size: 2.25rem;
        font-weight: 400;

        @media (max-width: 576px) {
          font-size: 1.5rem;
        }
      }
    }
  }

  &.revealed {
    pointer-events: none;

    &.correct,
    &.is-feedback {
      box-shadow:
        0 0 0.25rem 0 var(--kvizle-color-9),
        0 0 var(--_box-shadow-size) 0 var(--kvizle-color-10) inset;
    }

    &.selected.incorrect {
      box-shadow: 0 0 var(--_box-shadow-size) 0 var(--kvizle-color-11) inset;
    }
  }

  &:not(.revealed):hover {
    box-shadow:
      0 0 0.25rem 0 var(--kvizle-color-6),
      0 0 var(--_box-shadow-size) 0 var(--kvizle-color-7) inset;

    .answer-left .icon {
      .dot {
        background-color: var(--kvizle-color-2);
      }
    }
  }

  @include mixins.focus-visible;
}
</style>
