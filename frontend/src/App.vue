<script setup lang="ts">
import { RouterView } from 'vue-router'
</script>

<template>
  <div class="page-wrapper">
    <RouterView />
  </div>
</template>

<style scoped lang="scss">
.page-wrapper {
  display: flex;
  flex-direction: column;

  :deep(> main) {
    flex: 1;
  }
}
</style>
