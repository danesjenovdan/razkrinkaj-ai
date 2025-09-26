<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useStore } from '@/stores/store'
import { slugify } from '@/utils/stringify'

const props = defineProps<{
  updateHash: boolean
}>()

const store = useStore()

const selectedId = ref(store.explanations.keys().next().value ?? -1)
const selectedIdMobile = ref(-1)

function selectAnswer(i: number) {
  if (selectedIdMobile.value === i) {
    selectedIdMobile.value = -1
    return
  }
  selectedId.value = i
  selectedIdMobile.value = i

  if (props.updateHash) {
    window.history.pushState(
      window.history.state,
      '',
      `#${slugify(store.explanations.get(i)?.name ?? '')}`,
    )
  }
}

function getAnswerBySlug(slug: string) {
  for (const [id, explanation] of store.explanations) {
    if (slugify(explanation.name) === slug) {
      return id
    }
  }
  return -1
}

function onHashChange() {
  const hash = window.location.hash.slice(1)
  if (!hash) return

  const id = getAnswerBySlug(hash)
  if (id === -1) return

  selectedId.value = id
  selectedIdMobile.value = id
}

window.addEventListener('hashchange', onHashChange)

onMounted(() => {
  onHashChange()
})
</script>

<template>
  <section class="explanations-section">
    <h2>SPOZNAJ MANIPULACIJSKE TAKTIKE</h2>
    <div class="questions-and-answers">
      <div class="questions">
        <template v-for="[id, explanation] in store.explanations" :key="id">
          <div
            :class="{
              question: true,
              selected: id === selectedId,
              selectedMobile: id === selectedIdMobile,
            }"
          >
            <button @click="selectAnswer(id)">
              <div class="icon">
                <div v-if="explanation.image" class="image">
                  <img
                    :src="explanation.image.url"
                    :alt="explanation.image.alt"
                  />
                </div>
                <svg
                  v-else
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 54 56"
                >
                  <path
                    stroke="#000"
                    stroke-linecap="round"
                    stroke-width="3"
                    d="M32.2403 1.8834c-3.9584.1638-11.8909 1.8037-16.6362 3.8285-4.4638 1.9047-9.1643 7.4747-11.8237 12.2406-2.207 3.955-2.287 13.287-.0267 19.8766 1.5512 4.5227 6.3006 7.6846 10.4175 10.5055 3.9553 2.7103 8.1633 4.3033 13.1917 5.258 8.8376 1.6779 12.8788-2.6694 17.5425-6.6685 5.0245-4.3084 7.0797-10.0617 6.986-24.7607-.04-6.2785-3.5646-9.994-6.5489-13.6867-3.9404-2.6593-7.0002-4.1923-9.0166-4.7698-1.0158-.2909-2.0165-.5774-6.0387-.749"
                  />
                </svg>
              </div>
              <div class="text">
                <div class="name">{{ explanation.name }}</div>
                <div class="desc">{{ explanation.description }}</div>
              </div>
              <div class="arrow">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 28.4648 20.4952"
                >
                  <path
                    stroke="#000"
                    stroke-linecap="round"
                    stroke-width="3"
                    d="m1.5 9.9579 23.1413.0114m-9.3419 9.0259c1.6882-.9361 5.431-4.2982 8.4604-6.2947 1.0873-.7168 2.4477-1.7823 3.205-3.2832-2.0589-2.6424-4.3102-4.1449-6.5694-5.746-.5676-.4716-1.1264-1.0306-2.265-2.1713"
                  />
                </svg>
              </div>
            </button>
          </div>
          <div
            :class="{
              'inline-answer': true,
              selected: id === selectedIdMobile,
            }"
          >
            <div class="answer-text" v-html="explanation.content"></div>
          </div>
        </template>
      </div>
      <div class="answer">
        <div
          ref="answer-element"
          class="answer-text"
          v-html="store.explanations.get(selectedId)?.content"
        ></div>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
section.explanations-section {
  width: var(--page-width);
  margin-inline: auto;

  h2 {
    margin-top: 0;
    margin-bottom: 2.875rem;
    font-size: 2.25rem;
    font-weight: 700;
    text-align: center;
  }

  .questions-and-answers {
    display: grid;
    grid-template-columns: 1.85fr 3fr;
    gap: 3rem;

    .questions {
      margin-top: 2rem;

      .question {
        button {
          position: relative;
          z-index: 0;
          display: flex;
          align-items: center;
          gap: 0.75rem;
          width: 100%;
          padding: 0.625rem 0.875rem;
          background: var(--manipulacija-color-10);
          border: 3px solid #000;
          border-radius: 20px;
          text-align: left;
          // transform-origin: left center;
          transition:
            scale 0.15s ease-in-out,
            box-shadow 0.15s ease-in-out,
            width 0.15s ease-in-out;
          will-change: scale, box-shadow, width;

          .icon {
            flex-shrink: 0;
            width: 3.5rem;
            height: 3.5rem;

            svg,
            img {
              width: 100%;
              height: 100%;
            }
          }

          .text {
            flex: 1;
            font-weight: 500;

            .name {
              margin-bottom: 0.25rem;
              font-family: var(--font-family-alt);
              font-size: 1.3125rem;
              text-transform: uppercase;
            }

            .desc {
              font-size: 1rem;
            }
          }

          .arrow {
            display: none;
            margin-right: 0.5rem;

            svg {
              width: 1.8rem;
              height: 1.3125rem;
            }
          }
        }

        &:nth-child(4n - 3) {
          button {
            rotate: -1deg;
            margin-top: 0.25rem;
          }
        }

        &:nth-child(4n - 1) {
          button {
            rotate: 1deg;
          }
        }

        &:nth-child(6n - 1) {
          button {
            translate: 0.625rem;
          }
        }

        &.selected {
          button {
            width: 120%;
            background: var(--manipulacija-color-11);
            z-index: 1;
            cursor: default;

            .text {
              // font-weight: 600;
              // text-decoration: underline;
              // text-decoration-thickness: 1px;
            }

            .arrow {
              display: block;
            }
          }
        }

        &:not(.selected) {
          button:hover {
            scale: 1.02;
            box-shadow: 0 0 8px var(--manipulacija-color-4);
          }
        }
      }

      .inline-answer {
        display: none;
      }
    }

    .answer {
      display: grid;
      grid-template-areas: 'stack';
      background-image: url('/jagged-border.svg');
      background-repeat: no-repeat;
      background-size: 100% 100%;

      .answer-text {
        grid-area: stack;
        margin: 0.25rem;
        padding: 2.1875rem 2.9375rem 2.5625rem 3.8125rem;

        :deep(h3) {
          margin-top: 0;
          margin-bottom: 1.125rem;
          font-size: 1.3125rem;
          font-weight: 600;
        }

        :deep(p) {
          margin-top: 0;
          margin-bottom: 1.125rem;
          font-size: 1.125rem;
          line-height: 1.3;

          &:last-child {
            margin-bottom: 0;
          }
        }
      }
    }
  }
}
</style>
