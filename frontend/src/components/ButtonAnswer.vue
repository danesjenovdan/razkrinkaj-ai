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
console.log(store.currentChapterId)
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
        <svg
          v-if="correct"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 30 25"
        >
          <path
            fill="#BDFB7B"
            stroke="#000"
            stroke-width="3"
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M22.2842 2.254c1.1172-1.005 2.8212-1.005 3.9385 0l.1103.1034v.001l1.3027 1.2978.1963.2159a2.9266 2.9266 0 0 1 .668 1.8642c-.0001.7862-.3116 1.5269-.8613 2.0772l-.003.003-14.8955 14.8261c-1.1484 1.1433-3.0096 1.1432-4.1582 0l-6.2177-6.1905c-1.1521-1.1471-1.1521-3.011 0-4.1582l1.1835-1.1787.1192-.1181.2168-.1953a2.9405 2.9405 0 0 1 1.8633-.6631l.291.0146a2.9397 2.9397 0 0 1 1.5703.6465l.2158.1943.003.003 2.8339 2.8222L22.1738 2.3574l.1104-.1035Z"
          />
        </svg>
        <svg
          v-else
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 26 27"
        >
          <path
            fill="#FF6224"
            stroke="#000"
            stroke-width="3"
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M6.9775 2.542c.8142.1208 1.5947.5124 2.211 1.1299l3.8105 3.8105 3.8106-3.8105.1269-.1211c1.3358-1.2211 3.5282-1.5394 4.9727-.0938l.001-.001 1.6337 1.6338.1338.1416c1.3304 1.4894.9316 3.6765-.3506 4.9571l.001.001L19.5166 14l3.8105 3.8105.1211.126c1.2255 1.3377 1.5376 3.5311.0967 4.9746l-.0019.002-1.6338 1.6318c-1.4892 1.4879-3.7766 1.1056-5.0987-.2138l-.0009-.001-3.8106-3.8125-3.8105 3.8125c-1.3226 1.3213-3.6096 1.7015-5.0996.2148l-.001-.001-1.6309-1.6318c-1.4916-1.4913-1.1063-3.7803.2139-5.1006L6.4814 14 2.671 10.1885C1.3516 8.8687.9652 6.5803 2.457 5.0898l1.63-1.6328.0019-.002c.6355-.634 1.457-.935 2.2695-.954l.5547-.0127.0644.0537Z"
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
@use '@sass-fairy/string';
@use '@sass-fairy/url';
@use '@/assets/variables' as vars;

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
  gap: 0.68rem;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 1.125rem 1.125rem 1.125rem 2.375rem;
  background: transparent;
  background-image: url.svg(vars.$button-answer-bg-svg-string);
  background-repeat: no-repeat;
  background-size: 100% 100%;
  border: none;
  font-size: 1.5rem;
  line-height: 1;
  font-weight: 500;
  color: var(--color-text);
  text-align: left;
  text-decoration: none;
  cursor: pointer;
  transition:
    scale 0.15s ease-in-out,
    filter 0.15s ease-in-out;
  will-change: scale, filter;

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
    }

    .circle {
      background-color: #fff;
      border: 3px solid var(--color-text);
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
    border-radius: 3px;
    font-family: var(--font-family-alt);
    font-size: 1rem;
    line-height: 1.3;
    font-weight: 500;
    animation: bounceIn 0.66s;

    strong {
      font-weight: 700;
    }
  }

  &.revealed {
    pointer-events: none;

    &.correct,
    &.is-feedback {
      $button-answer-bg-svg-string-correct: string.replace(
        vars.$button-answer-bg-svg-string,
        '#FFF',
        '#E5FDCA'
      );
      background-image: url.svg($button-answer-bg-svg-string-correct);
      filter: drop-shadow(1.5px 1.5px 0 #bdfb7b)
        drop-shadow(-1.5px -1.5px 0 #bdfb7b) drop-shadow(0px 1.5px 0 #bdfb7b)
        drop-shadow(1.5px 0px 0 #bdfb7b) drop-shadow(0px -1.5px 0 #bdfb7b)
        drop-shadow(-1.5px 0px 0 #bdfb7b) drop-shadow(1.5px -1.5px 0 #bdfb7b)
        drop-shadow(-1.5px 1.5px 0 #bdfb7b);
    }

    &.selected.incorrect {
      $button-answer-bg-svg-string-incorrect: string.replace(
        vars.$button-answer-bg-svg-string,
        '#FFF',
        '#FEE2D6'
      );
      $button-answer-bg-svg-string-incorrect: string.replace(
        $button-answer-bg-svg-string-incorrect,
        '<path ',
        '<defs><filter id="shadow"><feFlood flood-color="#FF4B04" /><feComposite operator="out" in2="SourceGraphic" /><feMorphology operator="dilate" radius="2" /><feGaussianBlur stdDeviation="6" /><feComposite operator="atop" in2="SourceGraphic" /></filter></defs><path filter="url(#shadow)" '
      );
      $button-answer-bg-svg-string-incorrect-border: string.replace(
        vars.$button-answer-bg-svg-string,
        '#FFF',
        'none'
      );
      background-image: url.svg($button-answer-bg-svg-string-incorrect-border),
        url.svg($button-answer-bg-svg-string-incorrect);
      font-weight: 600;
    }
  }
}
</style>
