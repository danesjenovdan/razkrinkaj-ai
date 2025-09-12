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
  $bg-svg-string: '<svg viewBox="0 0 404 78" preserveAspectRatio="none" fill="#FFF"><path vector-effect="non-scaling-stroke" stroke="#000" stroke-width="3" d="M202 1.5c96.782 0 147.089 6.0657 173.162 13.9023 13.035 3.9179 19.825 8.2258 23.37 12.2676C402.011 31.636 402.5 35.499 402.5 39c0 3.6287-.17 7.4717-3.205 11.4023-3.082 3.9913-9.29 8.2836-21.952 12.1983C352.01 70.4323 301.714 76.5 202 76.5c-99.714 0-150.0096-6.0677-175.3428-13.8994-12.6627-3.9147-18.8705-8.207-21.9521-12.1983C1.6703 46.4717 1.5 42.6287 1.5 39c0-3.501.489-7.364 3.9678-11.3301 3.5453-4.0418 10.335-8.3497 23.3701-12.2676C54.9112 7.5657 105.218 1.5 202 1.5Z"/></svg>';
  position: relative;
  display: flex;
  gap: 0.68rem;
  align-items: center;
  justify-content: space-between;
  padding: 1.1875rem 3.875rem;
  background-image: url.svg($bg-svg-string);
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
    $bg-svg-string-primary: string.replace(
      $bg-svg-string,
      '#FFF',
      '#{vars.$manipulacija-color-2}'
    );
    background-image: url.svg($bg-svg-string-primary);
  }

  &.button-color-secondary {
    $bg-svg-string-secondary: string.replace(
      $bg-svg-string,
      '#FFF',
      '#{vars.$manipulacija-color-6}'
    );
    background-image: url.svg($bg-svg-string-secondary);
    padding-inline: 1.3125rem;
    font-size: 1.3125rem;
    justify-content: center;
    text-align: center;
  }

  .icon {
    flex-shrink: 0;
    display: flex;

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
