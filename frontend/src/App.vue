<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="page-wrapper">
    <div class="page-content">
      <RouterView />
    </div>
  </div>
</template>

<style scoped lang="scss">
.page-wrapper {
  max-width: var(--page-max-width);
  margin-inline: auto;
  background: var(--color-bg);
}

.page-content {
  padding-inline: var(--page-gutter);
}
</style>
