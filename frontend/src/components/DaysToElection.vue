<script setup lang="ts">
const today = new Date();
const electionDay = new Date("2026-03-22");

const timeDiff = electionDay.getTime() - today.getTime();
const days = Math.ceil(timeDiff / (1000 * 3600 * 24));
</script>

<template>
  <div class="days-to-election">
    ŠE <em>{{ days }}</em> DNI DO VOLITEV!
  </div>
</template>

<style lang="scss" scoped>
.days-to-election {
  max-width: 65rem;
  margin-inline: auto;
  margin-block: 1rem;
  font-family: var(--font-family-alt);
  font-size: 3rem;
  letter-spacing: 3%;
  text-align: center;

  @media (max-width: 576px) {
    font-size: 1.75rem;
  }

  em {
    font-size: 3.75rem;
    font-style: normal;
    color: var(--kvizle-color-2);

    @media (max-width: 576px) {
      font-size: 2.5rem;
    }
  }
}
</style>
