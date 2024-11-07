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
  <RouterLink :to="link" class="button-primary">
    <span>{{ buttonText }}</span>
    <span v-if="emoji">{{ emoji }}</span>
    <span v-if="icon" class="icon">{{ icon }}</span>
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
  font-family: var(--font-family-heading);
  font-size: 1rem;
  line-height: 1;
  font-weight: 700;
  color: #fff;
  text-decoration: none;
}
</style>
