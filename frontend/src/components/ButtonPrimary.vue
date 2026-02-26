<script setup lang="ts">
withDefaults(
  defineProps<{
    text: string;
    link: object;
    target?: string;
  }>(),
  {
    target: undefined,
  },
);
</script>

<template>
  <RouterLink :to="link" :target="target" class="button-primary">
    <span class="text">{{ text }}</span>
    <img src="/arrow.svg" alt="" />
  </RouterLink>
</template>

<style scoped lang="scss">
@use "@sass-fairy/string";
@use "@sass-fairy/url";
@use "@/assets/variables" as vars;
@use "@/assets/mixins";

.button-primary {
  @include mixins.button-link;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  padding: 0.5em 1em;
  font-size: 1.5rem;
  font-weight: 500;

  @media (max-width: 576px) {
    font-size: 1.25rem;
  }

  img {
    flex-shrink: 0;
    width: 1.75rem;
    height: auto;

    @media (max-width: 576px) {
      width: 1.5rem;
    }
  }
}
</style>
