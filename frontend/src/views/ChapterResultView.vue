<script setup lang="ts">
import type { Chapter, LeaderboardData } from '@/types'
import { onMounted, ref } from 'vue'
import { useStore } from '@/stores/store'
import PageFooter from '@/components/PageFooter.vue'
import ButtonPrimary from '@/components/ButtonPrimary.vue'

const props = defineProps<{ chapter: Chapter }>()

const store = useStore()

const leaderboardData = ref<LeaderboardData | null>(null)

const leaderboardMeText = ref('Tvoj rezultat')
const nickname = ref('')

async function onSubmitNickname() {
  if (nickname.value.trim().length === 0) {
    window.alert('Vzdevek ne sme biti prazen!')
    return
  }
  const success = await store.submitLeaderboardNickname(nickname.value.trim())
  if (success) {
    if (leaderboardData.value) {
      leaderboardData.value.my_nickname = nickname.value.trim()
    }
    leaderboardMeText.value = nickname.value.trim()
    nickname.value = ''
  } else {
    window.alert('Prišlo je do napake :(')
  }
}

function displayNick(entry: { nickname?: string; attempt_guid: string }) {
  if (entry.nickname) {
    return entry.nickname
  }
  return `Anonimnež (${entry.attempt_guid.slice(-4).toUpperCase()})`
}

// const totalChapterScore = computed(() => {
//   if (props.chapter.pages) {
//     return props.chapter.pages.reduce((prev, curr) => {
//       if (curr.type === 'quiz') {
//         return prev + curr.points
//       }
//       return prev
//     }, 0)
//   }
//   return 0
// })

// const totalAnswers = computed(() => {
//   const answers = [...store.currentChapterAnswers.values()]
//   return answers.length
// })

// const correctAnswers = computed(() => {
//   const answers = [...store.currentChapterAnswers.values()].filter(
//     answer => answer.correct,
//   )
//   return answers.length
// })

// const shareResultMessage = computed(() => {
//   return `

// Moj rezultat na razkrinkaj.ai

// Poglavje: ${props.chapter.title}

// 💪 Zbranih točk: ${store.currentChapterScore}
// 🎓 Pravilni odgovori: ${correctAnswers.value}/${totalAnswers.value}
// 🚀 Skupaj točk: ${store.score}

//   `.trim()
// })

// async function copyTextToClipboard(text: string) {
//   try {
//     await navigator.clipboard.writeText(text)
//     return true
//   } catch (error) {
//     console.error(error)
//     return false
//   }
// }

// async function onShareResult() {
//   if (await copyTextToClipboard(shareResultMessage.value)) {
//     window.alert(
//       `Tvoj rezultat smo skopirali v odložišče. Objavi ga na svojem najljubšem kanalu!\n\n${shareResultMessage.value}`,
//     )
//   } else {
//     window.alert(
//       'Ups, nekaj je šlo narobe pri kopiranju v odložišče. Rezultat imaš spodaj, skopiraj in deli ga!',
//     )
//   }
// }

onMounted(() => {
  // save score and answers
  if (!store.finishedChapters.has(props.chapter.id)) {
    store.finishedChapters.set(props.chapter.id, {
      score: store.currentChapterScore,
      answers: new Map(store.currentChapterAnswers),
    })
    store.inProgressChapters.delete(props.chapter.id)
    store.sendFinishedChapterDataToApi(props.chapter.id)
  }

  // unlock all feedback chapters that are not finished yet
  for (const chapter of store.chapters.values()) {
    if (
      chapter.is_feedback &&
      !store.finishedChapters.has(chapter.id) &&
      !store.unlockedChapters.includes(chapter.id)
    ) {
      store.unlockedChapters.push(chapter.id)
    }
  }

  // // unlock next chapter
  // const chapterIds = [...store.chapters.keys()]
  // const currentChapterIndex = chapterIds.findIndex(
  //   cid => cid === props.chapter.id,
  // )
  // const nextChapterId = chapterIds[currentChapterIndex + 1]
  // if (nextChapterId) {
  //   if (!store.justUnlockedChapters.includes(nextChapterId)) {
  //     store.justUnlockedChapters.push(nextChapterId)
  //   }
  //   if (!store.unlockedChapters.includes(nextChapterId)) {
  //     store.unlockedChapters.push(nextChapterId)
  //   }
  // }

  // fetch leaderboard data
  store.fetchLeaderboard().then(data => {
    leaderboardData.value = data
    if (data?.my_nickname) {
      leaderboardMeText.value = data.my_nickname
    }
  })

  // persist data to local storage
  store.saveLocalStorage()
})
</script>

<template>
  <main>
    <div class="header-section bg-manipulacija-color-7">
      <div class="page-gutter">
        <div class="header-content">
          <RouterLink :to="{ name: 'intro' }">
            <div class="title">
              <img
                src="/manipulacija-logo.svg"
                alt="Manipulacija ni informacija"
                class="title-logo"
              />
            </div>
          </RouterLink>
        </div>
        <h2 class="section-title">
          <span class="emoji">🏆🏆🏆</span>
          <span class="text">TVOJ REZULTAT</span>
          <span class="emoji">🏆🏆🏆</span>
        </h2>
        <div class="streak-container">
          <div class="stat">
            <div class="icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 42 62"
              >
                <path
                  fill="#FF6224"
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-width="3"
                  d="M37.8546 51.02c-2.5589 5.5115-7.6763 8.0552-11.8123 8.7318-2.5543.4178-6.4065.0986-7.6805-.2548-1.4753-.1532-2.6929-.5567-3.915-.9616-1.2221-.405-9.0311-2.8519-11.5899-10.9071-1.6508-5.1969-.4965-11.8788.0006-13.0603.511-1.2149 1.0472-2.4694 1.8323-3.6401.8148-1.2149 1.7199-2.7168 2.7982-3.9435 1.068-1.2149 2.3181-2.5914 3.6114-3.6387 1.6371-1.3256 4.0724-3.1112 5.6025-4.7109 3.0407-3.1791 4.0125-4.2907 4.7709-5.6559.8147-1.4667 1.6974-5.2787.6561-7.532-.5615-1.215-2.0244-4.0534-1.4205-3.3308.2548.3049 1.3041.9649 2.5968 1.8216 1.2221.81 3.2125 2.6717 4.6275 4.2483 1.2755 1.4212 2.6487 3.1533 3.3047 4.6018.711 1.5698 2.3525 4.9287 2.3525 7.7071 0 5.9355-.8548 8.6615-1.2795 10.1751-.5111 1.8215-1.6107 5.3971-1.073 5.0875 1.4724-.848 3.8822-2.2034 4.9113-4.8296.5569-1.4212 1.2794-4.4975 1.7059-4.4975.4265 0 2.3201 11.8526 2.1324 14.8385-.4265 6.7834-1.2795 7.9139-2.1324 9.7511Z"
                />
                <path
                  fill="#FFD427"
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-width="3"
                  d="M11.2614 41.118c1.2664 3.1002 3.2587 4.8548 3.5776 4.9571-.1603-2.262-.1603-4.3071-.133-5.4087.0801-1.255.133-1.7244.1602-2.2636.1875-.6972.2451-1.3289.4544-1.9358.2139-.6205.3422-1.2761.6682-1.8592.3469-.6205.6258-1.2588.9615-1.8592.347-.6205 2.0984-2.6734 2.6676-3.1986.1875 1.1062.8283 3.9706 1.1785 4.624.4014.7491.6158 1.4386 1.0953 1.9877.8637.9893 5.9284 5.1731 6.5868 5.8096 1.7721 1.7133 2.3772 3.4556 2.5467 4.1324.2139.8545.9976 4.0058-.3315 7.4323-.8861 2.2844-2.2846 3.7389-2.9577 4.3689-.8813.825-1.4744 1.3175-2.1898 1.6508-.7748.361-3.4555.4789-5.2891.3339-.9887-.0783-1.7532-.3492-2.4575-.6988-1.0408-.5167-1.7272-.8677-2.322-1.3425-.9142-.7297-2.1303-1.7205-2.5632-2.3247-.4824-.6732-1.1353-1.49-1.6025-2.2984-.3734-.6461-.7203-1.3613-.988-2.3775-.2924-1.1101-.4127-1.8286-.5865-2.9778-.3091-2.0437-.0487-4.1797.2949-4.8958.3229-.6732.9798-2.4664 1.2291-1.8561Z"
                />
              </svg>
            </div>
            <div class="value">{{ store.attemptStreak }}</div>
            <div class="desc">zaporednih zmag</div>
          </div>
          <div class="stat">
            <div class="icon">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 64 60"
              >
                <path
                  fill="#FFD427"
                  stroke="#000"
                  stroke-linecap="round"
                  stroke-width="3"
                  d="M31.7372 2.8942c.4295-.3143 1.0396-.5419 1.7417-.344.6742.19 1.0783.6866 1.2876.999.4341.6476.7227 1.5678.93 2.3695.2211.855.4032 1.8025.5554 2.633.1584.8647.2765 1.5587.3804 2.0181.1477.6532.3235 1.1585.6085 2.1926.2697.9784.5846 2.261.9385 4.2108.4546 2.505 1.1644 4.7832 1.5633 6.1628.0044.0006.0089.0024.0134.003.4698.067 1.1669.0794 2.0238.0503.8398-.0285 1.7545-.0934 2.6352-.1598.8621-.0649 1.7165-.1331 2.374-.1576 1.3411-.0498 3.2787-.1103 5.1301-.0695 1.7835.0394 3.9181.1687 8.3207.8919.289.0475.6726.1439 1.0208.3837.4084.2815.7514.7592.7764 1.3855.021.5236-.1943.9234-.3284 1.1302-.1476.2277-.3231.413-.467.5485-3.1774 2.9915-7.3914 6.4544-8.9983 7.443-.5644.3472-1.106.7389-1.7351 1.1978-.6185.4511-1.3105.9581-2.1162 1.4779-.6914.4461-1.316.7489-1.7874.9733-.2459.1171-.4199.1983-.5682.276a2.568 2.568 0 0 0-.1581.0893c-.0024.0015-.0052.0024-.0075.0038-.0075.0586-.0144.1771.0085.3936.0295.278.0839.5556.1525.9652.0622.3705.1313.8308.1374 1.3067.033 2.5536-.0673 6.3598-.0985 8.0714-.0116.6372-.0619 1.208-.108 1.7254-.047.5276-.0889.9934-.1024 1.497-.0137.509-.1115 1.3791-.5198 2.1085-.2154.3847-.5873.8539-1.2009 1.1102-.6476.2705-1.3162.2018-1.8966-.0356-2.4641-1.0076-4.5884-2.7536-6.1841-4.3083-.8063-.7856-1.4975-1.5417-2.0453-2.1602-.5824-.6576-.9267-1.0696-1.1512-1.3-.2053-.2108-.4074-.4852-.5724-.7157-.1588-.2219-.4037-.576-.6022-.8557-.2968-.4182-.6396-.8804-1.0315-1.3587-2.0847 2.673-4.5585 5.6479-5.9396 7.234-1.5159 1.7408-3.2289 3.5735-4.6041 4.6168a2.3784 2.3784 0 0 0-.1258.1041c-.0441.0385-.1375.1219-.2231.1909-.0845.0682-.2402.189-.4416.2876-.2073.1016-.5618.2285-1.0015.1707-.8165-.1077-1.2206-.736-1.3295-.9135-.1612-.2632-.2636-.542-.3258-.7321-.1094-.3344-.1087-.7-.1074-.8732.0018-.2434.0191-.5326.0452-.8507.0526-.6408.1506-1.4888.285-2.5014.2695-2.0304.6938-4.7989 1.2201-8.0586.3063-1.8976.6017-3.2638.8349-4.2417.1156-.4847.2164-.8761.2896-1.1667.0103-.0406.0188-.079.0275-.1144-.1194-.0688-.282-.1535-.4992-.2548a28.3238 28.3238 0 0 0-.6507-.2911c-.2326-.1013-.4887-.2116-.7419-.3278-.4972-.2283-1.0647-.5121-1.5622-.8713a1.1022 1.1022 0 0 0-.0505-.0315 5.1287 5.1287 0 0 0-.1699-.0964c-.1492-.0815-.3403-.1807-.5859-.3077-.4841-.2504-1.1362-.5857-1.9172-1.017-1.5663-.8651-3.6507-2.1169-6.0768-3.9153-1.3578-1.0066-2.3733-1.9459-3.1301-2.6862-.3093-.3026-.754-.7509-.928-.9218-.2636-.2589-.391-.3681-.448-.408-.1869-.1309-.6383-.4911-.7407-1.1487-.1165-.7488.2983-1.2614.53-1.4756.2306-.2133.4853-.3391.6471-.41.1822-.0798.3752-.1444.5581-.1975.7064-.205 1.7195-.3687 2.7323-.5006 2.0605-.2683 4.5339-.4558 5.5085-.5437 1.781-.1606 7.3419-.7099 10.015-.9258.7889-3.8165 2.6034-8.2793 4.9015-12.3948 1.5577-2.7895 2.5291-3.8057 3.6455-5.0384.2294-.2534.4263-.4886.6308-.7268.1786-.208.4089-.4744.6368-.6755l.1725-.1384Z"
                />
              </svg>
            </div>
            <div class="value">{{ store.score }}</div>
            <div class="desc">točk</div>
          </div>
        </div>
      </div>
    </div>
    <div class="leaderboard-section bg-manipulacija-color-3">
      <div class="page-gutter">
        <div class="section-title">
          <span class="emoji">👑👑👑</span>
          <span class="text">TRENUTNA LESTVICA</span>
          <span class="emoji">👑👑👑</span>
        </div>
        <div v-if="leaderboardData" class="leaderboard">
          <div
            v-for="entry in leaderboardData.top_leaderboard"
            :class="{
              'leaderboard-entry': true,
              me: entry.attempt_guid === leaderboardData.attempt_guid,
            }"
            :key="entry.rank"
          >
            <div class="place">{{ entry.rank }}.</div>
            <div class="content">
              <div class="name">
                {{
                  entry.attempt_guid === leaderboardData.attempt_guid
                    ? leaderboardMeText
                    : displayNick(entry)
                }}
              </div>
              <div class="score">{{ entry.total_score }}</div>
            </div>
          </div>
          <div class="ellipsis">...</div>
          <div
            v-for="entry in leaderboardData.ranked_near_me"
            :class="{
              'leaderboard-entry': true,
              me: entry.attempt_guid === leaderboardData.attempt_guid,
            }"
            :key="entry.rank"
          >
            <div class="place">{{ entry.rank }}.</div>
            <div class="content">
              <div class="name">
                {{
                  entry.attempt_guid === leaderboardData.attempt_guid
                    ? leaderboardMeText
                    : displayNick(entry)
                }}
              </div>
              <div class="score">{{ entry.total_score }}</div>
            </div>
          </div>
        </div>
        <div v-if="!leaderboardData?.my_nickname" class="add-nickname">
          <div class="title">
            Tvoj rezultat trenutno ni viden.<br />
            Se želiš vpisati na lestvico?
          </div>
          <form class="nickname-form" @submit.prevent="onSubmitNickname">
            <label for="nickname">Vpiši svoj vzdevek</label>
            <input
              type="text"
              id="nickname"
              v-model="nickname"
              maxlength="20"
              required
            />
            <div>
              <button type="submit" class="submit-button">VPIŠI ME!</button>
            </div>
          </form>
        </div>
      </div>
    </div>
    <div class="share-section bg-manipulacija-color-7">
      <div class="page-gutter">
        <div class="share-with-us">
          <div class="text">
            Si v medijih zasledil_a kakšno zanimivo manipulacijo?
          </div>
          <div class="buttons">
            <ButtonPrimary
              class="button"
              button-text="POSREDUJ NAM JO!"
              href="mailto:tadej@danesjenovdan.si"
              target="_blank"
              icon="hand"
              color="white"
            />
          </div>
        </div>
      </div>
    </div>
  </main>
  <PageFooter />
</template>

<style scoped lang="scss">
@use '@sass-fairy/string';
@use '@sass-fairy/url';
@use '@/assets/variables' as vars;

main {
  .header-section {
    padding-bottom: 4.125rem;

    @media (max-width: 576px) {
      padding-bottom: 2rem;
    }
  }

  .header-content {
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 650px;
    margin-inline: auto;
    padding-block: 3.5rem 3rem;

    @media (max-width: 576px) {
      padding-block: 2rem 1.5rem;
    }

    .title {
      display: flex;

      .title-logo {
        width: 450px;
        height: auto;

        @media (max-width: 576px) {
          width: 200px;
        }
      }
    }
  }

  .section-title {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0;
    font-size: 2.25rem;
    font-weight: 700;
    text-align: center;

    @media (max-width: 576px) {
      font-size: 1.5rem;
    }

    .emoji {
      white-space: nowrap;
      letter-spacing: -4px;
    }

    .text {
      line-height: 1.1;

      @media (max-width: 576px) {
        margin-inline: 0.5rem;
      }
    }
  }

  .streak-container {
    display: flex;
    justify-content: space-between;
    max-width: 600px;
    margin-inline: auto;
    margin-top: 1.5rem;
    padding: 2.75rem 3.75rem;
    background-image: url('/jagged-border-streak.svg');
    background-repeat: no-repeat;
    background-size: 100% 100%;

    @media (max-width: 576px) {
      flex-direction: column;
      align-items: center;
      gap: 1rem;
      padding: 1.5rem 1.75rem;
    }

    .stat {
      display: flex;
      align-items: center;
      gap: 0.5rem;

      .icon {
        width: auto;
        height: 3.5rem;

        @media (max-width: 576px) {
          height: 2.5rem;
        }

        svg {
          width: 100%;
          height: 100%;
        }
      }

      .value {
        font-family: var(--font-family-alt);
        font-size: 4.5rem;
        font-weight: 500;
        line-height: 1;

        @media (max-width: 576px) {
          font-size: 2.5rem;
        }
      }

      .desc {
        width: min-content;
        font-size: 1.3125rem;
        font-weight: 600;

        @media (max-width: 576px) {
          font-size: 1rem;
        }
      }
    }
  }

  .leaderboard-section {
    padding-block: 3rem 4rem;
  }

  .leaderboard {
    max-width: 400px;
    margin-inline: auto;
    padding-block: 1.5rem;

    @media (max-width: 576px) {
      width: 100%;
    }

    .leaderboard-entry {
      display: flex;
      align-items: center;

      &:not(:last-child) {
        margin-bottom: 0.5rem;
      }

      .place {
        flex-shrink: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        width: 60px;
        height: 60px;
        background-color: var(--manipulacija-color-5);
        border: 3px solid black;
        border-radius: 50%;
        font-family: var(--font-family-alt);
        font-weight: 600;
        font-size: 2rem;
        z-index: 1;

        @media (max-width: 576px) {
          width: 48px;
          height: 48px;
          font-size: 1.5rem;
        }
      }

      .content {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 0.5rem;
        width: 100%;
        margin-left: -2rem;
        padding: 0.5rem 1rem 0.5rem 2.5rem;
        background-color: #fff;
        border: 3px solid black;
        border-radius: 1rem;

        @media (max-width: 576px) {
          margin-left: -1.5rem;
          padding: 0.25rem 0.75rem 0.25rem 2rem;
        }

        .name {
          flex: 1;
          font-size: 1.25rem;
          font-weight: 600;
          white-space: nowrap;
          overflow: hidden;
          text-overflow: ellipsis;

          @media (max-width: 576px) {
            font-size: 1rem;
          }
        }

        .score {
          font-family: var(--font-family-alt);
          font-size: 1.5rem;
          font-weight: 600;

          @media (max-width: 576px) {
            font-size: 1.25rem;
          }
        }
      }

      &.me {
        .content {
          background-color: var(--manipulacija-color-12);

          .name {
            font-weight: 700;
          }
        }
      }
    }

    .ellipsis {
      margin-top: -0.2em;
      margin-bottom: 0.4em;
      font-family: var(--font-family-alt);
      font-size: 2.25rem;
      line-height: 1;
      font-weight: 700;
      text-align: center;
    }
  }

  .add-nickname {
    max-width: 340px;
    margin-inline: auto;
    margin-top: 1rem;

    .title {
      font-weight: 600;
      text-align: center;
    }

    .nickname-form {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
      margin-top: 1.5rem;
      font-size: 0.875rem;

      input {
        padding: 0.2em 0.5em;
        background: var(--manipulacija-color-8);
        border: 3px solid #000;
        border-radius: 5px;
        font-weight: 500;
        font-size: 1rem;
        line-height: 1rem;
      }

      .submit-button {
        display: inline-flex;
        gap: 0.5em;
        align-items: center;
        padding: 0.4em 1.125em 0.3em;
        background-color: transparent;
        background-image: url.svg(vars.$button-link-bg-string);
        background-repeat: no-repeat;
        background-size: 100% 100%;
        border: none;
        font-family: var(--font-family-alt);
        font-size: 1.125rem;
        font-weight: 600;
        line-height: 1.3;
        color: inherit;
        text-decoration: none;
        cursor: pointer;
        transition:
          scale 0.15s ease-in-out,
          filter 0.15s ease-in-out;
        will-change: scale, filter;

        &:not(:disabled):hover {
          scale: 1.05;
          filter: drop-shadow(0 0 4px var(--manipulacija-color-4));
        }
      }

      .submit-button {
        $button-link-bg-string-submit: string.replace(
          vars.$button-link-bg-string,
          '#FFF',
          '#{vars.$manipulacija-color-6}'
        );
        background-image: url.svg($button-link-bg-string-submit);
        margin-top: 0.5rem;
        border: 0;

        &:disabled {
          cursor: wait;
          filter: grayscale(1);
        }
      }
    }
  }

  .share-section {
    padding-block: 3rem;

    .share-with-us {
      max-width: 600px;
      margin-inline: auto;
      text-align: center;

      .text {
        font-size: 1.5rem;
        font-weight: 600;
        margin-bottom: 1.25rem;

        @media (max-width: 576px) {
          font-size: 1.25rem;
        }
      }

      .buttons {
        .button-primary {
          max-width: 380px;
          margin-inline: auto;
          font-size: 1.3125rem;
        }
      }
    }
  }
}
</style>
