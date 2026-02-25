<script setup lang="ts">
defineProps<{
  title: string;
  description?: string;
  score: number;
  hideScore?: boolean;
}>();
</script>

<template>
  <header class="score-header">
    <div class="page-gutter">
      <div class="header-content">
        <RouterLink :to="{ name: 'intro' }" class="title">
          VOLILNI KVIZLE
        </RouterLink>
        <div v-if="!hideScore" class="score">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 48 44"
          >
            <path
              fill="#F0EB98"
              stroke="#F0EB98"
              stroke-linecap="round"
              d="M21.2577 6.1952c-1.999 3.58-3.4986 7.4341-3.9717 10.5017-1.1732.0501-7.1856.6484-8.9509.8076-1.6195.146-7.7728.5897-6.8334 1.2476.554.3879 1.5812 1.7143 3.6451 3.2443 3.794 2.8124 6.5082 3.9067 7.0549 4.3014 1.2074.8716 3.486 1.2735 3.3382 2.2183-.0807.5155-.524 1.8032-1.0057 4.7868-.8444 5.2309-1.3539 8.8372-1.2031 9.2984.0785.2398.192.4816.3422.5014.1501.0197.3184-.1921.5531-.3702.9941-.7541 2.2973-2.1374 3.5173-3.5384 1.1611-1.3334 3.3086-3.917 5.0232-6.1363.287-.3715.6353-.7208 1.0399-.2803 1.1733 1.2776 1.8783 2.5297 2.2495 2.9107.825.8467 3.5861 4.5162 7.1266 5.9639.9733.398 1.2265-.8041 1.2444-1.4735.0241-.8969.152-1.6484.1689-2.5774.0255-1.3953.1057-4.4186.0795-6.4444-.0146-1.1352-.6464-2.4092.1715-3.0688.3916-.3157 1.1914-.5496 2.1646-1.1775 1.2274-.7918 2.1146-1.5478 3.1144-2.1629 1.1794-.7256 4.4888-3.4336 7.0317-5.8277.3102-.292.4435-.6017-.1739-.7031-3.4879-.573-5.1449-.6706-6.5129-.7008-1.4489-.032-2.9748.0154-4.0489.0554-1.9952.0741-6.4958.6816-6.7365-.2257-.2406-.9072-.9752-3.1183-1.4074-5.4997-.5555-3.0608-.9805-3.9802-1.232-5.0923-.3629-1.6047-.9199-6.4546-2.0977-5.415-.2196.194-.5256.5932-.9226 1.0315-.8705.9613-1.5815 1.6998-2.7683 3.825Z"
            />
          </svg>
          <strong>{{ score }}</strong>
        </div>
      </div>
      <!-- eslint-disable-next-line vue/no-v-html -->
      <div v-if="description" class="description" v-html="description"></div>
    </div>
  </header>
</template>

<style scoped lang="scss">
@use "@sass-fairy/url";
@use "@/assets/mixins";

.score-header {
  .header-content {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 65rem;
    margin-inline: auto;
    padding-block: 3.5rem;

    @media (max-width: 576px) {
      padding-block: 2rem;
    }

    .title {
      display: flex;
      font-family: var(--font-family-alt);
      font-size: 4.5rem;
      line-height: 1;
      color: var(--kvizle-color-2);
      letter-spacing: 3%;
      text-decoration: none;
      text-shadow:
        8px 4px 0 var(--kvizle-color-2),
        12px 7px 0 var(--kvizle-color-3);
      text-align: center;
      -webkit-text-fill-color: var(--kvizle-color-1);
      -webkit-text-stroke: 2px;

      @media (max-width: 576px) {
        font-size: 2.75rem;
      }

      @include mixins.focus-visible;
    }

    .score {
      position: absolute;
      top: 2rem;
      right: 0;
      background-color: magenta; // TODO
    }
  }

  .description {
    max-width: 65rem;
    margin-inline: auto;
    font-size: 1.5rem;
    font-weight: 500;
    text-align: center;

    @media (max-width: 576px) {
      font-size: 1.25rem;
    }

    :deep(b) {
      font-weight: 500;
      color: var(--kvizle-color-2);
    }
  }
}
</style>
