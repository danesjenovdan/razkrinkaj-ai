<script setup lang="ts"></script>

<template>
  <div class="calendar-election-day">
    <div class="text">22.&nbsp;3. VOLILNA NEDELJA</div>
    <div class="button-container">
      <button type="button">Dodaj opomnik v koledar</button>
    </div>
  </div>
</template>

<style scoped lang="scss">
@use '@sass-fairy/string';
@use '@sass-fairy/url';
@use '@/assets/variables' as vars;

.calendar-election-day {
  grid-column: span 3;
  display: flex;
  align-items: center;
  gap: 2rem;
  padding: 0.25rem 1rem;
  background: var(--kvizle-color-5);
  border: 2px solid var(--kvizle-color-2);

  .text {
    flex: 0;
    width: min-content;
    font-family: var(--font-family-alt);
    font-size: 2.875rem;
    line-height: 0.9;
    color: var(--kvizle-color-2);
    letter-spacing: 3%;
    text-decoration: none;
    text-shadow:
      8px 4px 0 var(--kvizle-color-2),
      12px 7px 0 var(--kvizle-color-3);
    -webkit-text-fill-color: var(--kvizle-color-1);
    -webkit-text-stroke: 2px;
  }

  .button-container {
    flex: 1;

    button {
      $calendar-button-link-bg-string: string.replace(
        string.replace(
          vars.$button-link-bg-string,
          '#000',
          '#{vars.$kvizle-color-2}'
        ),
        '#FFF',
        '#{vars.$kvizle-color-4}'
      );
      $calendar-hover-button-link-bg-string: string.replace(
        string.replace(
          vars.$button-link-bg-string,
          '#000',
          '#{vars.$kvizle-color-2}'
        ),
        '#FFF',
        '#{vars.$kvizle-color-5}'
      );

      display: block;
      width: 100%;
      padding: 0.65em 0.4rem 0.75rem;
      background-color: transparent;
      background-image: url.svg($calendar-button-link-bg-string);
      background-repeat: no-repeat;
      background-size: 100% 100%;
      border: none;
      font-size: 1.125rem;
      font-weight: 500;
      line-height: 1.3;
      color: var(--kvizle-color-2);
      text-align: center;
      text-decoration: none;
      cursor: pointer;
      transition:
        scale 0.15s ease-in-out,
        filter 0.15s ease-in-out;
      will-change: scale, filter;

      &:not(:disabled):hover {
        scale: 1.05;
        background-image: url.svg($calendar-hover-button-link-bg-string);
        filter: drop-shadow(0 0 2px var(--kvizle-color-2));
      }

      &:focus-visible {
        outline: 2px solid var(--kvizle-color-2);
        outline-offset: 2px;
      }
    }
  }
}
</style>
