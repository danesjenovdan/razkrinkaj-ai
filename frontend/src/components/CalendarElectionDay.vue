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
@use "@sass-fairy/string";
@use "@sass-fairy/url";
@use "@/assets/variables" as vars;
@use "@/assets/mixins";

.calendar-election-day {
  grid-column: span 3;
  display: flex;
  align-items: center;
  gap: 2rem;
  min-height: 9.5rem;
  padding: 0.5rem 1rem;
  background: var(--kvizle-color-5);
  border: 2px solid var(--kvizle-color-2);

  @media (max-width: 576px) {
    grid-column: span 2;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem 0.5rem;
  }

  .text {
    flex: 0;
    width: min-content;
    font-family: var(--font-family-alt);
    font-size: 2.75rem;
    line-height: 0.9;
    color: var(--kvizle-color-2);
    letter-spacing: 3%;
    text-decoration: none;
    text-shadow:
      8px 4px 0 var(--kvizle-color-2),
      12px 7px 0 var(--kvizle-color-3);
    -webkit-text-fill-color: var(--kvizle-color-1);
    -webkit-text-stroke: 2px;

    @media (max-width: 576px) {
      text-align: center;
    }
  }

  .button-container {
    flex: 1;

    button {
      @include mixins.button-link;
      display: block;
      width: 100%;
      padding: 0.65em 0.45em 0.7em;
      font-size: 1.125rem;
      font-weight: 500;

      @media (max-width: 576px) {
        padding-inline: 1em;
      }
    }
  }
}
</style>
