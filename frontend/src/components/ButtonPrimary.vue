<script setup lang="ts">
const props = defineProps<{
  buttonText: string
  link: object
  emoji?: string
  icon?: string
}>()

if (props.emoji && props.icon) {
  throw new Error('You can only use either emoji or icon, not both')
}
</script>

<template>
  <RouterLink :to="props.link" class="button-primary">
    <span>{{ props.buttonText }}</span>
    <span v-if="props.emoji">{{ props.emoji }}</span>
    <span v-if="props.icon" class="icon">{{ props.icon }}</span>
  </RouterLink>
</template>

<style scoped lang="scss">
.button-primary {
  display: flex;
  justify-content: space-between;
  padding: 0.68rem 0.875rem;
  border-radius: 3px;
  border: 0.5px solid #000;
  background: #4063f6;
  font-size: 1rem;
  line-height: 1;
  font-weight: 700;
  color: #fff;
  text-decoration: none;
}
</style>
