<script setup lang="ts">
defineProps<{
  title: string;
  description?: string;
  score: number;
  hideScore?: boolean;
  backButton?: boolean;
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
          <span>Tvoj rezultat</span>
          <div>
            <img src="/star.svg" alt="" />
            <strong>{{ score }}</strong>
          </div>
        </div>
        <div v-if="backButton" class="back-button-container">
          <RouterLink :to="{ name: 'intro' }" class="back-to-calendar">
            <img src="/share-arrow.svg" alt="" />
            <span>Nazaj na koledar</span>
          </RouterLink>
        </div>
      </div>
      <!-- eslint-disable-next-line vue/no-v-html -->
      <div v-if="description" class="description" v-html="description"></div>
    </div>
  </header>
</template>

<style scoped lang="scss">
@use "@sass-fairy/string";
@use "@sass-fairy/url";
@use "@/assets/variables" as vars;
@use "@/assets/mixins";

.score-header {
  .header-content {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    max-width: 65rem;
    margin-inline: auto;
    padding-block: 3.5rem;

    @media (max-width: 576px) {
      flex-direction: column;
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
      $bg-header-score-border-string: string.replace(
        vars.$header-score-border-string,
        "#000",
        "#{vars.$kvizle-color-5}"
      );

      position: absolute;
      top: 2rem;
      right: 0;
      padding: 0.75rem 1.75rem 0.5rem 1.5rem;
      background-color: transparent;
      background-image: url.svg($bg-header-score-border-string);
      background-repeat: no-repeat;
      background-size: 100% 100%;
      color: var(--kvizle-color-2);

      @media (max-width: 576px) {
        position: static;
        margin-top: 1rem;
      }

      span {
        font-family: var(--font-family-alt);
        font-size: 1rem;
        line-height: 1;
        letter-spacing: 3%;
      }

      div {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
        font-size: 1.75rem;
        font-weight: 500;

        img {
          width: 2rem;
          height: 2rem;

          @media (max-width: 576px) {
            width: 1.5rem;
            height: 1.5rem;
          }
        }

        strong {
          font-family: var(--font-family-alt);
          font-size: 3rem;
          line-height: 1;
          letter-spacing: 3%;

          @media (max-width: 576px) {
            font-size: 2rem;
          }
        }
      }
    }

    .back-button-container {
      width: 100%;
      max-width: 21rem;
      margin-inline: auto;

      @media (max-width: 576px) {
        max-width: 18rem;
      }

      .back-to-calendar {
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
          scale: -1 1;

          @media (max-width: 576px) {
            width: 1.75rem;
          }
        }
      }
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
