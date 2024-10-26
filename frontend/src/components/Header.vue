<script setup lang="ts">
import { defineComponent } from 'vue'

const props = defineProps({
    score: Number
})

</script>

<template>
    <header>
        <div>
            <span>Razkrinkaj.AI</span>
            <span>{{ score }} točk</span>
        </div>
        <hr />
    </header>
</template>

<style>
header div {
    display: flex;
    justify-content: space-between;
}
</style>