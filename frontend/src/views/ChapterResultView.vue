<script setup lang="ts">
import type { Chapter } from "@/types";
import { onMounted, computed } from "vue";
import { useStore } from "@/stores/store.ts";

const props = defineProps<{ chapter: Chapter }>();

const store = useStore();

const chapterDate = computed(() => {
  const dateParts = props.chapter.title.split(".").map(Number);
  return new Date(dateParts[2], dateParts[1] - 1, dateParts[0]);
});

const isLocked = computed(() => {
  const date = chapterDate.value;
  const now = Date.now();
  return now < date.getTime();
});

if (isLocked.value) {
  throw new Error("ChapterResultView cannot be shown for locked chapters");
}

const totalAnswers = computed(() => {
  const answers = [...store.currentChapterAnswers.values()];
  return answers.length;
});

const correctAnswers = computed(() => {
  const answers = [...store.currentChapterAnswers.values()].filter(
    (answer) => answer.correct,
  );
  return answers.length;
});

const shareResultMessage = computed(() => {
  return `

Moj rezultat na Kvizle.si

${props.chapter.title}

💪 Zbranih točk: ${store.currentChapterScore}
🎓 Pravilni odgovori: ${correctAnswers.value}/${totalAnswers.value}
🚀 Skupaj točk: ${store.score}

  `.trim();
});

async function copyTextToClipboard(text: string) {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch (error) {
    // eslint-disable-next-line no-console
    console.error(error);
    return false;
  }
}

async function onShareResult() {
  if (await copyTextToClipboard(shareResultMessage.value)) {
    // eslint-disable-next-line no-alert
    window.alert(
      `Tvoj rezultat smo skopirali v odložišče. Objavi ga na svojem najljubšem kanalu!\n\n${shareResultMessage.value}`,
    );
  } else {
    // eslint-disable-next-line no-alert
    window.alert(
      "Ups, nekaj je šlo narobe pri kopiranju v odložišče. Rezultat imaš spodaj, skopiraj in deli ga!",
    );
  }
}

const websiteLinkValue = "kvizle.si";

async function onCopyLink() {
  if (await copyTextToClipboard(websiteLinkValue)) {
    // eslint-disable-next-line no-alert
    window.alert(
      `Povezavo smo skopirali v odložišče. Pošlji jo svojim prijateljem!\n\n${websiteLinkValue}`,
    );
  } else {
    // eslint-disable-next-line no-alert
    window.alert(
      "Ups, nekaj je šlo narobe pri kopiranju v odložišče. Povezava je spodaj, skopiraj in deli jo!",
    );
  }
}

onMounted(() => {
  // save score and answers
  if (!store.finishedChapters.has(props.chapter.id)) {
    store.finishedChapters.set(props.chapter.id, {
      score: store.currentChapterScore,
      answers: new Map(store.currentChapterAnswers),
    });
    store.inProgressChapters.delete(props.chapter.id);
    store.sendFinishedChapterDataToApi(props.chapter.id);
  }

  // persist data to local storage
  store.saveLocalStorage();
});
</script>

<template>
  <main>
    <div class="result-section bg-kvizle-color-0">
      <div class="page-gutter">
        <h2 class="section-title result-title">Tvoj rezultat</h2>
        <div class="chapter-scores">
          <div class="score-box">
            <img src="/star.svg" alt="" />
            <div>Zbranih točk:</div>
            <span class="score">{{ store.currentChapterScore }}</span>
          </div>
          <div class="score-box">
            <img src="/hat.svg" alt="" />
            <div>Pravilni odgovori:</div>
            <span class="score">{{ correctAnswers }}/{{ totalAnswers }}</span>
          </div>
          <div class="score-box">
            <img src="/stars.svg" alt="" />
            <div>Skupaj točk:</div>
            <span class="score">{{ store.score }}</span>
          </div>
          <button type="button" @click.prevent="onShareResult">
            <span>Deli rezultat</span>
            <img src="/share-arrow.svg" alt="" />
          </button>
        </div>
      </div>
    </div>
    <div class="link-section bg-kvizle-color-8">
      <div class="page-gutter">
        <div class="section-title">
          <img src="/calendar.svg" alt="" />
          <div>
            Nova vprašanja<br />
            te čakajo jutri!
          </div>
          <img src="/calendar.svg" alt="" />
        </div>
        <div class="subtitle">
          Do takrat pa k sodelovanju povabi še prijatelje!
        </div>
        <div class="link-group">
          <input
            id="website-link"
            type="text"
            :value="websiteLinkValue"
            maxlength="20"
            required
            onfocus="this.select()"
          />
          <button type="button" @click.prevent="onCopyLink">Kopiraj</button>
        </div>
      </div>
    </div>
  </main>
</template>

<style scoped lang="scss">
@use "@sass-fairy/string";
@use "@sass-fairy/url";
@use "@/assets/variables" as vars;
@use "@/assets/mixins";

main {
  .section-title {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    margin: 0;
    font-size: 1.75rem;
    font-weight: 700;
    text-align: center;
    text-wrap: balance;

    @media (max-width: 576px) {
      font-size: 1.375rem;
    }

    &.result-title {
      font-family: var(--font-family-alt);
      font-size: 2.25rem;

      @media (max-width: 576px) {
        font-size: 1.75rem;
      }
    }

    br {
      display: none;

      @media (max-width: 576px) {
        display: block;
      }
    }

    img {
      width: 2.125rem;
      height: 2.125rem;
    }
  }

  .result-section {
    padding-block: 2.5rem 4rem;

    @media (max-width: 576px) {
      padding-block: 1.75rem;
    }

    .chapter-scores {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      max-width: 21rem;
      margin-inline: auto;
      margin-top: 2rem;

      @media (max-width: 576px) {
        max-width: 18rem;
        margin-top: 1.25rem;
      }

      .score-box {
        display: flex;
        gap: 1rem;
        align-items: center;
        padding: 0.5rem 1rem;
        background: var(--kvizle-color-5);
        font-size: 1.125rem;
        font-weight: 500;

        @media (max-width: 576px) {
          gap: 0.75rem;
          padding: 0.375rem 0.75rem;
          font-size: 1rem;
        }

        img {
          width: 2rem;
          height: 2rem;
        }

        .score {
          margin-bottom: -0.25rem;
          font-family: var(--font-family-alt);
          font-size: 3rem;
          line-height: 1;
          color: var(--kvizle-color-2);

          @media (max-width: 576px) {
            font-size: 2.25rem;
          }
        }
      }

      button {
        @include mixins.button-link;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.75rem;
        margin-top: 2rem;
        padding: 0.45em 1.5em;
        font-size: 1.5rem;
        font-weight: 500;

        @media (max-width: 576px) {
          margin-top: 0.75rem;
          font-size: 1.25rem;
        }

        img {
          flex-shrink: 0;
          width: 2.25rem;

          @media (max-width: 576px) {
            width: 1.75rem;
          }
        }
      }
    }
  }

  .link-section {
    padding-block: 2.5rem;

    @media (max-width: 576px) {
      padding-block: 1.75rem;
    }

    .subtitle {
      font-size: 1.3125rem;
      font-weight: 500;
      text-align: center;

      @media (max-width: 576px) {
        font-size: 1rem;
      }
    }

    .link-group {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.75rem;
      margin-top: 2rem;
      text-align: center;

      @media (max-width: 576px) {
        flex-direction: column;
        gap: 0.5rem;
        margin-top: 1.25rem;
      }

      input {
        width: 16ch;
        padding: 0.5em 0.5em;
        background: var(--color-bg-white);
        border: 1px solid var(--color-text);
        font-size: 1.3125rem;
        line-height: 1;
        font-weight: 500;
        text-align: center;
        color: var(--color-text);

        @media (max-width: 576px) {
          font-size: 1rem;
        }

        @include mixins.focus-visible;
      }

      button {
        @include mixins.button-link;
        padding: 0.55em 2em;
        font-size: 1.25rem;
        font-weight: 500;

        @media (max-width: 576px) {
          font-size: 1rem;
        }
      }
    }
  }
}
</style>
