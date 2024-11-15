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
  display: grid;
  width: var(--page-width);
  margin-inline: auto;
  background: var(--color-bg-light);
}

.page-content {
  display: flex;
  flex-direction: column;
  padding-inline: var(--page-gutter);

  :deep(> main) {
    flex: 1;
  }
}
</style>
