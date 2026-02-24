<script setup lang="ts">
import { useStore } from "@/stores/store.ts";

const store = useStore();
</script>

<template>
  <div v-if="!store.hasConsented" class="consent-prompt">
    <div class="text">
      Za shranjevanje napredka v kvizu nam dovoli, da ti naložimo identifikator.
      Povezan bo samo s tvojim rezultatom.
    </div>
    <div class="consent-button">
      <button
        type="button"
        :disabled="store.consentClickedButNotDone"
        @click.prevent="store.giveConsent"
      >
        DOVOLIM
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 30 25">
          <path
            fill="#BDFB7B"
            stroke="#000"
            stroke-width="3"
            stroke-linecap="round"
            stroke-linejoin="round"
            d="M22.2842 2.254c1.1172-1.005 2.8212-1.005 3.9385 0l.1103.1034v.001l1.3027 1.2978.1963.2159a2.9266 2.9266 0 0 1 .668 1.8642c-.0001.7862-.3116 1.5269-.8613 2.0772l-.003.003-14.8955 14.8261c-1.1484 1.1433-3.0096 1.1432-4.1582 0l-6.2177-6.1905c-1.1521-1.1471-1.1521-3.011 0-4.1582l1.1835-1.1787.1192-.1181.2168-.1953a2.9405 2.9405 0 0 1 1.8633-.6631l.291.0146a2.9397 2.9397 0 0 1 1.5703.6465l.2158.1943.003.003 2.8339 2.8222L22.1738 2.3574l.1104-.1035Z"
          />
        </svg>
      </button>
    </div>
  </div>
</template>

<style lang="scss" scoped>
@use "@sass-fairy/string";
@use "@sass-fairy/url";
@use "@/assets/variables" as vars;

.consent-prompt {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  max-width: 630px;
  margin-inline: auto;
  padding: 1rem 1.5rem 1rem 1.75rem;
  $percentile-bg-svg-string-consent: string.replace(
    vars.$percentile-bg-svg-string,
    "#FFF",
    "magenta"
  );
  background-image: url.svg($percentile-bg-svg-string-consent);
  background-repeat: no-repeat;
  background-size: 100% 100%;

  @media (max-width: 576px) {
    flex-direction: column;
    gap: 0.75rem;
    padding: 1.5rem;
    text-align: center;
  }

  .text {
    font-size: 1rem;
    font-weight: 500;
  }

  .consent-button {
    button {
      display: inline-flex;
      gap: 0.25em;
      align-items: center;
      padding: 0.4em 0.875em 0.3em;
      background-color: transparent;
      $button-link-bg-string-consent: string.replace(
        vars.$button-link-bg-string,
        "#FFF",
        "magenta"
      );
      background-image: url.svg($button-link-bg-string-consent);
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

      &:disabled {
        cursor: wait;
        filter: grayscale(1);
      }

      svg {
        width: 0.875rem;
      }
    }
  }
}
</style>
