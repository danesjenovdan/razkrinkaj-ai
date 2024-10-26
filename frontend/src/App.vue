<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'

</script>

<template>
  <div class="wrapper">
    <div class="content">
      <RouterView />
    </div>
  </div>
</template>

<style scope lang="scss">
.wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.content {
  max-width: 27rem;
  width: 100%;
  max-height: 58rem;
  height: 100%;
}
</style>
