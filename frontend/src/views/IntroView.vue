<script setup lang="ts">
import { useStore } from '@/stores/store'
import ButtonPrimary from '@/components/ButtonPrimary.vue'
import PageFooter from '@/components/PageFooter.vue'

const store = useStore()
</script>

<template>
  <div class="page-wrapper">
    <main>
      <div class="intro">
        <img
          src="/manipulacija-logo.svg"
          alt="Manipulacija ni informacija"
          class="title-logo"
        />
        <div class="narrow">
          <div class="description" v-html="store.introductionDescription"></div>
          <ButtonPrimary
            class="button"
            :buttonText="store.introductionButtonText"
            :link="{ name: 'chapter-list' }"
            icon="hands"
          />
        </div>
      </div>
    </main>
    <PageFooter />
  </div>
</template>

<style scoped lang="scss">
.page-wrapper {
  background-color: var(--manipulacija-color-3);
}

main {
  padding-bottom: 8.69rem;

  .intro {
    .title-logo {
      width: 100%;
      max-width: 960px;
      padding-top: 5.75rem;
      padding-bottom: 2.875rem;
      margin-inline: auto;
    }

    .narrow {
      margin-inline: auto;
      max-width: 550px;

      .description {
        font-size: 1.5rem;
        font-weight: 500;

        :deep(a) {
          font-weight: 600;
          color: #092bba;
        }
      }

      .button {
        margin-top: 2.875rem;
        margin-inline: auto;
        max-width: 404px;
      }
    }
  }
}
</style>
