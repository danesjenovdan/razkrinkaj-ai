<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(
  defineProps<{
    buttonText?: string
    link?: object
    href?: string
    icon?: string
    sideIcon?: string
    color?: string
  }>(),
  {
    color: 'primary',
  },
)

const text = computed(() => props.buttonText || 'Nadaljuj')

const componentName = computed(() =>
  props.link ? 'RouterLink' : props.href ? 'a' : 'button',
)
</script>

<template>
  <component
    :is="componentName"
    :to="link"
    :href="href"
    :class="['button-primary', `button-color-${color}`]"
  >
    <span v-if="sideIcon" class="side-icon">
      <template v-if="sideIcon === 'hand-down'">
        <img class="hand-down" src="/hand-down.svg" alt="" />
      </template>
    </span>
    <span>{{ text }}</span>
    <span v-if="icon" class="icon">
      <template v-if="icon === 'hands'">
        <img class="hands" src="/hands.svg" alt="" />
      </template>
      <template v-if="icon === 'hand'">
        <img class="hand" src="/hand.svg" alt="" />
      </template>
      <span v-else>{{ icon }}</span>
    </span>
    <span v-if="sideIcon" class="side-icon">
      <template v-if="sideIcon === 'hand-down'">
        <img class="hand-down" src="/hand-down.svg" alt="" />
      </template>
    </span>
  </component>
</template>

<style scoped lang="scss">
@use '@sass-fairy/string';
@use '@sass-fairy/url';
@use '@/assets/variables' as vars;

.button-primary {
  position: relative;
  display: flex;
  gap: 0.68rem;
  align-items: center;
  justify-content: space-between;
  padding: 1.1875rem 3.875rem;
  background-image: url.svg(vars.$button-bg-svg-string);
  background-repeat: no-repeat;
  background-size: 100% 100%;
  font-family: var(--font-family-alt);
  font-size: 2.5rem;
  line-height: 1;
  font-weight: 600;
  color: var(--color-text);
  text-decoration: none;
  cursor: pointer;
  transition:
    scale 0.15s ease-in-out,
    filter 0.15s ease-in-out;
  will-change: scale, filter;

  &.button-color-primary {
    $button-bg-svg-string-primary: string.replace(
      vars.$button-bg-svg-string,
      '#FFF',
      '#{vars.$manipulacija-color-2}'
    );
    background-image: url.svg($button-bg-svg-string-primary);
  }

  &.button-color-secondary {
    $button-bg-svg-string-secondary: string.replace(
      vars.$button-bg-svg-string,
      '#FFF',
      '#{vars.$manipulacija-color-6}'
    );
    background-image: url.svg($button-bg-svg-string-secondary);
    padding-inline: 1.3125rem;
    font-size: 1.3125rem;
    justify-content: center;
    text-align: center;
  }

  .icon {
    flex-shrink: 0;
    display: flex;

    .hand,
    .hands {
      width: auto;
      height: 1.5rem;
    }
  }

  .side-icon {
    flex-shrink: 0;
    display: flex;
    position: absolute;
    left: -0.375rem;

    &:last-child {
      left: auto;
      right: -0.375rem;
      transform: scaleX(-1);
    }

    .hand-down {
      width: auto;
      height: 2.875rem;
    }
  }

  &:hover {
    scale: 1.05;
    filter: drop-shadow(0 0 4px var(--manipulacija-color-4));
  }
}
</style>
