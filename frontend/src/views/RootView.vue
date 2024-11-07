<script setup lang="ts">
import { useStore } from '@/stores/store'

const store = useStore()
store.initHomeData()
</script>

<template>
  <RouterView v-if="store.homeDataLoaded" />
  <div v-else>root loading...</div>
</template>
