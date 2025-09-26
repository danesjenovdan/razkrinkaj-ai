<template>
  <div class="share-explanation">
    <label>
      <span>Deli povezavo:</span>
      <input type="text" :value="urlValue" onfocus="this.select();" />
    </label>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import type { Explanation } from '@/types'
import { slugify } from '@/utils/stringify'

const props = defineProps<{
  explanation: Explanation
}>()

const router = useRouter()

const urlValue = computed(() => {
  const baseUrl = window.location.origin
  const path = router.resolve({ name: 'tactics' }).href
  const hash = `#${slugify(props.explanation.name)}`
  return `${baseUrl}${path}${hash}`
})
</script>

<style scoped lang="scss">
.share-explanation {
  label {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-weight: 500;

    input {
      width: 380px;
      padding: 0.2em 0.5em;
      background: var(--manipulacija-color-8);
      border: 3px solid #000;
      border-radius: 5px;
      font-weight: 500;
      font-size: 1rem;
      line-height: 1rem;
    }
  }
}
</style>
