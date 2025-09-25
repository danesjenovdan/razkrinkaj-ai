<script setup lang="ts">
import type { QuizPage } from '@/types'
import { computed, onBeforeUnmount, onMounted, ref } from 'vue'
import { useStore } from '@/stores/store'
import ButtonAnswer from './ButtonAnswer.vue'
import RichText from './RichText.vue'
import { preloadPageImages } from '@/utils/image'
import { slugify } from '@/utils/stringify'

const props = defineProps<{ page: QuizPage }>()
const emit = defineEmits<{ done: [] }>()

const store = useStore()

const selectedAnswer = ref<number | null>(null)

const modalOpen = ref(false)
const modalExplanationId = ref<number | null>(null)

const percentPeopleCorrect = ref(-1)

function getAnswerBySlug(slug: string) {
  for (const [id, explanation] of store.explanations) {
    if (slugify(explanation.name) === slug) {
      return id
    }
  }
  return -1
}

function openModal(buttonText: string) {
  const id = getAnswerBySlug(slugify(buttonText))
  if (id === -1) return

  modalOpen.value = true
  modalExplanationId.value = id
  document.body.style.overflow = 'hidden'

  window.history.pushState(window.history.state, '', `#modal`)
}

function closeModal() {
  modalOpen.value = false
  modalExplanationId.value = null
  document.body.style.overflow = ''
  window.history.go(-1)
}

function onPopState() {
  modalOpen.value = false
  modalExplanationId.value = null
  document.body.style.overflow = ''
}

const modalExplanation = computed(() => {
  if (modalExplanationId.value == null) return null
  return store.explanations.get(modalExplanationId.value) || null
})

function onAnswerClick(index: number) {
  selectedAnswer.value = index
  const correct = props.page.answers[index].correct
  const points = correct ? props.page.points : -props.page.points
  // add points
  store.currentChapterScore += points
  // store answer
  store.currentChapterAnswers.set(props.page.id, {
    answerIndex: index,
    correct,
    answerText: props.page.answers[index].text,
  })
  // update in progress chapters
  store.inProgressChapters.set(store.currentChapterId, {
    score: store.currentChapterScore,
    answers: new Map(store.currentChapterAnswers),
  })
  store
    .sendProgressChapterDataToApi(store.currentChapterId)
    .then(() =>
      store.fetchPageCorrectPercent(store.currentChapterId, props.page.id),
    )
    .then(value => {
      percentPeopleCorrect.value = value
    })

  // persist data to local storage
  store.saveLocalStorage()
  emit('done')
}

onMounted(() => {
  if (window.location.hash === '#modal') {
    window.history.replaceState(
      window.history.state,
      '',
      window.location.pathname + window.location.search,
    )
  }
  window.addEventListener('popstate', onPopState)

  preloadPageImages(props.page)

  if (
    store.finishedChapters.has(store.currentChapterId) ||
    store.inProgressChapters.has(store.currentChapterId)
  ) {
    const index = store.currentChapterAnswers.get(props.page.id)?.answerIndex
    if (index != null) {
      selectedAnswer.value = index
      store
        .fetchPageCorrectPercent(store.currentChapterId, props.page.id)
        .then(value => {
          percentPeopleCorrect.value = value
        })
      emit('done')
    }
  }
})

onBeforeUnmount(() => {
  document.body.style.overflow = ''
  window.removeEventListener('popstate', onPopState)
})
</script>

<template>
  <div class="quiz-page">
    <div v-if="page.question" class="question">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 58 40"
        class="quotes"
      >
        <path
          fill="#FF6224"
          d="M45.9922 1.7363c-2.3271.0265-4.3721 1.3855-6.0215 2.916-2.5663 2.4241-4.426 5.5054-5.8477 8.713-1.2094 2.809-2.0804 5.7882-2.3808 8.8378-.0924 1.6924-.1076 3.3954.0254 5.086.3334 2.9136 1.3115 5.8913 3.4394 7.996 2.1785 2.1784 5.2527 3.3338 8.3125 3.3712 2.6722.0559 5.495-.336 7.752-1.8672 2.0524-1.3926 3.601-3.4925 4.3398-5.8594.5868-1.7181.982-3.5174.9395-5.3418.0514-2.84-.5736-5.8193-2.3672-8.0879-1.344-1.807-3.4388-2.9067-5.6035-3.3945 1.1793-2.0285 2.1855-4.2199 2.5195-6.5606.2111-1.5512-.1074-3.3016-1.3379-4.373-.9867-.9958-2.3803-1.4768-3.7695-1.4356Zm-29.9258.0235c-.135-.0016-.2712.0009-.4062.002-1.7687-.0004-3.3941.9019-4.7754 1.9335-2.925 2.2812-4.9594 5.4934-6.5489 8.7988-2.3468 4.897-3.494 10.4896-2.5976 15.8907.4067 2.5952 1.4694 5.1599 3.4004 6.9922 2.0134 2.0098 4.813 3.113 7.6347 3.2539 2.5997.1312 5.3282-.1542 7.6387-1.4356 2.3852-1.3607 4.1946-3.657 5.0098-6.2754.6903-1.9766 1.0455-4.0764.918-6.1719-.0734-2.6459-.7765-5.3754-2.4922-7.4453-.9752-1.1314-2.1859-2.0717-3.5918-2.6015-.607-.2463-1.2357-.4396-1.873-.5899 1.1583-2.0078 2.1518-4.1664 2.5214-6.4707.2622-1.5965-.1369-3.369-1.3555-4.4941-.9168-.9084-2.1895-1.4278-3.4824-1.3867Z"
        />
        <path
          fill="#000"
          d="M15.9043.6992c-1.945 0-3.7266.79-5.293 1.9258-.0065.0044-.013.0092-.0195.0137-.022.016-.0446.0308-.0664.0468l.002.002c-1.6541 1.1538-3.173 2.8529-4.5919 4.9102l-.0078.0097-.0078.0117c-1.6904 2.499-3.0401 5.2398-4.0547 8.211l-.0097.0312-.0098.0313C.9036 18.8638.4043 21.7392.4043 24.5c0 4.5146 1.0116 8.4648 3.6074 11.246l.0176.0196.0176.0196c2.5724 2.661 5.924 3.914 9.7578 3.914 3.1065 0 5.9532-.6386 8.1836-2.287 1.9719-1.4576 3.4023-3.3495 4.2148-5.6349h.002c.0052-.0136.0085-.0274.0137-.041.0065-.0186.015-.036.0215-.0547h-.002c.7602-2.0067 1.166-4.0399 1.166-6.082 0-3.6733-.8929-6.9712-3.1543-9.3848l.002-.002c-.0153-.0173-.0314-.0336-.0469-.0507l-.037-.0391-.002.002c-1.133-1.244-2.581-2.0982-4.2364-2.6523.3577-.6776.6607-1.3225.8848-1.92h-.002c.6892-1.6724 1.1914-3.347 1.1914-4.8535 0-1.5046-.4561-3.1282-1.7793-4.3183l.002-.002C19.0034 1.1556 17.433.6992 15.9043.6992Zm30.1953 0c-1.9448 0-3.7266.79-5.293 1.9258-.0065.0044-.013.0092-.0195.0137-.022.016-.0445.0308-.0664.0468l.002.002c-1.654 1.1538-3.173 2.8529-4.5918 4.9102l-.0078.0097-.0078.0117c-1.6905 2.499-3.0402 5.2398-4.0547 8.211l-.0098.0312-.0098.0313c-.942 2.9712-1.4414 5.8466-1.4414 8.6074 0 4.5146 1.0116 8.4648 3.6074 11.2461l.0176.0195.0176.0196c2.5725 2.661 5.924 3.914 9.7578 3.914 3.1066 0 5.9532-.6386 8.1836-2.287 1.9719-1.4576 3.4022-3.3495 4.2148-5.6349h.002c.0052-.0136.0085-.0274.0137-.041.0065-.0186.015-.036.0215-.0547h-.002c.7602-2.0067 1.166-4.0399 1.166-6.082 0-3.6733-.8928-6.9712-3.1543-9.3848l.002-.002c-.0153-.0173-.0314-.0336-.0469-.0507l-.037-.0391-.002.002c-1.133-1.244-2.581-2.0982-4.2364-2.6523.3577-.6776.6607-1.3225.8848-1.92h-.002c.6893-1.6724 1.1914-3.347 1.1914-4.8535 0-1.5046-.4561-3.1281-1.7793-4.3183l.002-.002C49.1987 1.1556 47.6284.6992 46.0996.6992Zm-30.1953 3c.9333 0 1.6679.2675 2.2012.8008.6.4667.8984 1.1992.8984 2.1992 0 .9334-.3333 2.2008-1 3.8008-.4896 1.3057-1.4926 3.0338-2.959 5.1387 3.282.178 5.6039 1.0286 6.959 2.5605 1.6 1.6667 2.4004 4.1337 2.4004 7.4004 0 1.6667-.3333 3.3663-1 5.0996-.6 1.7333-1.666 3.1675-3.1992 4.3008-1.5333 1.1333-3.6671 1.6992-6.4004 1.6992-3.1333 0-5.6663-1-7.5996-3-1.8667-2-2.8008-5.0659-2.8008-9.1992 0-2.4.4341-4.966 1.3008-7.6992.9333-2.7333 2.1659-5.2333 3.6992-7.5 1.3333-1.9334 2.6337-3.3345 3.9004-4.2012 1.2667-.9333 2.4663-1.4004 3.5996-1.4004zm30.1953 0c.9333 0 1.6679.2675 2.2012.8008.6.4667.8984 1.1992.8984 2.1992 0 .9334-.3333 2.2008-1 3.8008-.4896 1.3057-1.4926 3.0338-2.959 5.1387 3.282.178 5.6039 1.0286 6.959 2.5605 1.6 1.6667 2.4004 4.1337 2.4004 7.4004 0 1.6667-.3333 3.3663-1 5.0996-.6 1.7333-1.666 3.1675-3.1992 4.3008-1.5333 1.1333-3.6671 1.6992-6.4004 1.6992-3.1333 0-5.6663-1-7.5996-3-1.8667-2-2.8008-5.0659-2.8008-9.1992 0-2.4.434-4.966 1.3008-7.6992.9333-2.7333 2.166-5.2333 3.6992-7.5C39.933 7.3674 41.2333 5.9663 42.5 5.0996c1.2667-.9333 2.4663-1.4004 3.5996-1.4004z"
        />
      </svg>
      <span>{{ page.question }}</span>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 58 40"
        class="quotes"
      >
        <path
          fill="#FF6224"
          d="M45.9922 1.7363c-2.3271.0265-4.3721 1.3855-6.0215 2.916-2.5663 2.4241-4.426 5.5054-5.8477 8.713-1.2094 2.809-2.0804 5.7882-2.3808 8.8378-.0924 1.6924-.1076 3.3954.0254 5.086.3334 2.9136 1.3115 5.8913 3.4394 7.996 2.1785 2.1784 5.2527 3.3338 8.3125 3.3712 2.6722.0559 5.495-.336 7.752-1.8672 2.0524-1.3926 3.601-3.4925 4.3398-5.8594.5868-1.7181.982-3.5174.9395-5.3418.0514-2.84-.5736-5.8193-2.3672-8.0879-1.344-1.807-3.4388-2.9067-5.6035-3.3945 1.1793-2.0285 2.1855-4.2199 2.5195-6.5606.2111-1.5512-.1074-3.3016-1.3379-4.373-.9867-.9958-2.3803-1.4768-3.7695-1.4356Zm-29.9258.0235c-.135-.0016-.2712.0009-.4062.002-1.7687-.0004-3.3941.9019-4.7754 1.9335-2.925 2.2812-4.9594 5.4934-6.5489 8.7988-2.3468 4.897-3.494 10.4896-2.5976 15.8907.4067 2.5952 1.4694 5.1599 3.4004 6.9922 2.0134 2.0098 4.813 3.113 7.6347 3.2539 2.5997.1312 5.3282-.1542 7.6387-1.4356 2.3852-1.3607 4.1946-3.657 5.0098-6.2754.6903-1.9766 1.0455-4.0764.918-6.1719-.0734-2.6459-.7765-5.3754-2.4922-7.4453-.9752-1.1314-2.1859-2.0717-3.5918-2.6015-.607-.2463-1.2357-.4396-1.873-.5899 1.1583-2.0078 2.1518-4.1664 2.5214-6.4707.2622-1.5965-.1369-3.369-1.3555-4.4941-.9168-.9084-2.1895-1.4278-3.4824-1.3867Z"
        />
        <path
          fill="#000"
          d="M15.9043.6992c-1.945 0-3.7266.79-5.293 1.9258-.0065.0044-.013.0092-.0195.0137-.022.016-.0446.0308-.0664.0468l.002.002c-1.6541 1.1538-3.173 2.8529-4.5919 4.9102l-.0078.0097-.0078.0117c-1.6904 2.499-3.0401 5.2398-4.0547 8.211l-.0097.0312-.0098.0313C.9036 18.8638.4043 21.7392.4043 24.5c0 4.5146 1.0116 8.4648 3.6074 11.246l.0176.0196.0176.0196c2.5724 2.661 5.924 3.914 9.7578 3.914 3.1065 0 5.9532-.6386 8.1836-2.287 1.9719-1.4576 3.4023-3.3495 4.2148-5.6349h.002c.0052-.0136.0085-.0274.0137-.041.0065-.0186.015-.036.0215-.0547h-.002c.7602-2.0067 1.166-4.0399 1.166-6.082 0-3.6733-.8929-6.9712-3.1543-9.3848l.002-.002c-.0153-.0173-.0314-.0336-.0469-.0507l-.037-.0391-.002.002c-1.133-1.244-2.581-2.0982-4.2364-2.6523.3577-.6776.6607-1.3225.8848-1.92h-.002c.6892-1.6724 1.1914-3.347 1.1914-4.8535 0-1.5046-.4561-3.1282-1.7793-4.3183l.002-.002C19.0034 1.1556 17.433.6992 15.9043.6992Zm30.1953 0c-1.9448 0-3.7266.79-5.293 1.9258-.0065.0044-.013.0092-.0195.0137-.022.016-.0445.0308-.0664.0468l.002.002c-1.654 1.1538-3.173 2.8529-4.5918 4.9102l-.0078.0097-.0078.0117c-1.6905 2.499-3.0402 5.2398-4.0547 8.211l-.0098.0312-.0098.0313c-.942 2.9712-1.4414 5.8466-1.4414 8.6074 0 4.5146 1.0116 8.4648 3.6074 11.2461l.0176.0195.0176.0196c2.5725 2.661 5.924 3.914 9.7578 3.914 3.1066 0 5.9532-.6386 8.1836-2.287 1.9719-1.4576 3.4022-3.3495 4.2148-5.6349h.002c.0052-.0136.0085-.0274.0137-.041.0065-.0186.015-.036.0215-.0547h-.002c.7602-2.0067 1.166-4.0399 1.166-6.082 0-3.6733-.8928-6.9712-3.1543-9.3848l.002-.002c-.0153-.0173-.0314-.0336-.0469-.0507l-.037-.0391-.002.002c-1.133-1.244-2.581-2.0982-4.2364-2.6523.3577-.6776.6607-1.3225.8848-1.92h-.002c.6893-1.6724 1.1914-3.347 1.1914-4.8535 0-1.5046-.4561-3.1281-1.7793-4.3183l.002-.002C49.1987 1.1556 47.6284.6992 46.0996.6992Zm-30.1953 3c.9333 0 1.6679.2675 2.2012.8008.6.4667.8984 1.1992.8984 2.1992 0 .9334-.3333 2.2008-1 3.8008-.4896 1.3057-1.4926 3.0338-2.959 5.1387 3.282.178 5.6039 1.0286 6.959 2.5605 1.6 1.6667 2.4004 4.1337 2.4004 7.4004 0 1.6667-.3333 3.3663-1 5.0996-.6 1.7333-1.666 3.1675-3.1992 4.3008-1.5333 1.1333-3.6671 1.6992-6.4004 1.6992-3.1333 0-5.6663-1-7.5996-3-1.8667-2-2.8008-5.0659-2.8008-9.1992 0-2.4.4341-4.966 1.3008-7.6992.9333-2.7333 2.1659-5.2333 3.6992-7.5 1.3333-1.9334 2.6337-3.3345 3.9004-4.2012 1.2667-.9333 2.4663-1.4004 3.5996-1.4004zm30.1953 0c.9333 0 1.6679.2675 2.2012.8008.6.4667.8984 1.1992.8984 2.1992 0 .9334-.3333 2.2008-1 3.8008-.4896 1.3057-1.4926 3.0338-2.959 5.1387 3.282.178 5.6039 1.0286 6.959 2.5605 1.6 1.6667 2.4004 4.1337 2.4004 7.4004 0 1.6667-.3333 3.3663-1 5.0996-.6 1.7333-1.666 3.1675-3.1992 4.3008-1.5333 1.1333-3.6671 1.6992-6.4004 1.6992-3.1333 0-5.6663-1-7.5996-3-1.8667-2-2.8008-5.0659-2.8008-9.1992 0-2.4.434-4.966 1.3008-7.6992.9333-2.7333 2.166-5.2333 3.6992-7.5C39.933 7.3674 41.2333 5.9663 42.5 5.0996c1.2667-.9333 2.4663-1.4004 3.5996-1.4004z"
        />
      </svg>
    </div>
    <div class="answers">
      <div v-for="(answer, index) in page.answers" :key="index" class="answer">
        <ButtonAnswer
          :buttonText="answer.text"
          :correct="answer.correct"
          :revealed="selectedAnswer !== null"
          :selected="selectedAnswer === index"
          :points="page.points"
          @click="onAnswerClick(index)"
        />
        <button type="button" class="help" @click="openModal(answer.text)">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 32 32"
          >
            <circle cx="16" cy="16" r="16" fill="#4063F6" />
            <path
              fill="#FEFDF5"
              d="M14.9376 6.734c2.2706 0 3.9866.546 5.148 1.638 1.1786 1.0747 1.768 2.4787 1.768 4.212 0 1.04-.182 1.976-.546 2.808-.3467.8147-.858 1.5427-1.534 2.184-.6587.6413-1.4474 1.2393-2.366 1.794-.6414.3813-1.2394.65-1.794.806-.5547.156-1.0747.234-1.56.234-.5374 0-.9794-.13-1.326-.39-.3467-.2773-.52-.6413-.52-1.092 0-.416.1386-.806.416-1.17.2946-.364.7626-.7367 1.404-1.118.8493-.4853 1.534-.9187 2.054-1.3.52-.3813.78-.8147.78-1.3 0-.3293-.0954-.5893-.286-.78-.1734-.1907-.4767-.286-.91-.286-.3467 0-.7627.0173-1.248.052a18.637 18.637 0 0 1-1.378.052c-.9187 0-1.6294-.2513-2.132-.754-.5027-.5027-.754-1.2047-.754-2.106 0-.7973.1993-1.4473.598-1.95.3986-.52.9533-.9013 1.664-1.144.728-.26 1.5686-.39 2.522-.39Zm-3.224 17.42c0-.572.1386-1.0313.416-1.378.2946-.364.6673-.6327 1.118-.806.468-.1733.9533-.26 1.456-.26.8666 0 1.5253.1993 1.976.598.468.3987.702.936.702 1.612 0 .832-.286 1.4387-.858 1.82-.572.364-1.2654.546-2.08.546-.884 0-1.56-.1907-2.028-.572-.468-.3987-.702-.9187-.702-1.56Z"
            />
          </svg>
        </button>
      </div>
      <div v-if="selectedAnswer === null" class="answer-info">
        <strong>Previdno:</strong> Napačen odgovor prinaša minus točke. Če nisi
        prepričan_a, odgovori z “Ne vem” ali preveri opis.
      </div>
    </div>
    <div v-if="selectedAnswer !== null" class="answer-description-wrapper">
      <div class="answer-stats">
        Na to vprašanje je pravilno odgovorilo
        <template v-if="percentPeopleCorrect !== -1">
          <em>{{ percentPeopleCorrect }} %</em>
        </template>
        <template v-else>
          <em>...</em>
        </template>
        uporabnikov.
      </div>
      <h2>OBRAZLOŽITEV</h2>
      <div class="answer-description">
        <RichText :content="page.answer_description" />
      </div>
    </div>
    <div v-if="modalOpen && modalExplanation !== null" class="help-modal">
      <div class="modal-content">
        <button
          type="button"
          class="close-button"
          @click="closeModal"
          aria-label="Zapri"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 54 54"
          >
            <circle
              cx="27"
              cy="27"
              r="25.5"
              fill="#fff"
              stroke="#000"
              stroke-width="3"
            />
            <path
              fill="#4063F6"
              stroke="#000"
              stroke-width="3"
              d="M19.0725 15.0012c-.5601.0131-1.0905.2166-1.4941.6193l-1.9573 1.9596c-.92.9183-.804 2.5129.2566 3.5739l5.8453 5.8475-5.8453 5.8447c-1.0605 1.0605-1.177 2.6556-.2566 3.5756l1.9573 1.9581c.9201.918 2.5135.8038 3.5753-.257l5.8452-5.8466 5.8453 5.8466c1.0628 1.0609 2.6572 1.175 3.5753.257l1.9601-1.9581c.9183-.9198.8041-2.5148-.2587-3.5756l-5.845-5.8447 5.8453-5.8472c1.0628-1.0609 1.177-2.6555.2587-3.5739l-1.9602-1.9596c-.9182-.9201-2.5127-.8038-3.5753.2585l-5.8452 5.845-5.8452-5.8448c-.5966-.5986-1.3627-.8956-2.0813-.8782l-.0002-.0001Z"
            />
          </svg>
        </button>
        <div class="modal-body">
          <div class="title-section">
            <div class="name">{{ modalExplanation.name }}</div>
            <div class="desc">{{ modalExplanation.description }}</div>
          </div>
          <RichText :content="modalExplanation.content" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@use '@sass-fairy/string';
@use '@sass-fairy/url';
@use '@/assets/variables' as vars;

.quiz-page {
  padding-block: 0.75rem 2.5rem;

  .question {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.75rem;
    max-width: 603px;
    margin: 0 auto;
    padding: 2.5rem 5rem;
    background-image: url('/jagged-border-question.svg');
    background-repeat: no-repeat;
    background-size: 100% 100%;
    font-size: 2rem;
    font-weight: 500;
    text-align: center;

    .quotes {
      width: 3.5rem;
      height: auto;

      &:last-child {
        transform: scale(-1);
      }
    }
  }

  .answers {
    display: grid;
    gap: 0.875rem;
    max-width: 455px;
    margin-top: 2rem;
    margin-inline: auto;

    .answer {
      display: flex;
      align-items: center;
      gap: 0.75rem;

      .help {
        width: 2rem;
        height: 2rem;
        padding: 0;
        border: none;
        background: transparent;
        flex-shrink: 0;
        cursor: help;

        svg {
          width: 100%;
          height: 100%;
        }
      }
    }

    .answer-info {
      margin-top: 1rem;
      font-size: 0.875rem;
      text-align: center;

      strong {
        font-weight: 700;
      }
    }
  }

  .answer-description-wrapper {
    margin-top: 3rem;

    .answer-stats {
      max-width: 514px;
      margin-inline: auto;
      padding: 1rem;
      $percentile-bg-svg-string-default: string.replace(
        vars.$percentile-bg-svg-string,
        '#FFF',
        '#{vars.$manipulacija-color-5}'
      );
      background-image: url.svg($percentile-bg-svg-string-default);
      background-repeat: no-repeat;
      background-size: 100% 100%;
      font-size: 1.75rem;
      line-height: 1;
      font-weight: 500;
      text-align: center;
      rotate: -1.7deg;

      em {
        font-family: var(--font-family-alt);
        font-style: normal;
        font-size: 2.25rem;
        font-weight: 600;
      }
    }

    h2 {
      margin-top: 4.5rem;
      margin-bottom: 0;
      font-size: 2.25rem;
      text-align: center;
    }

    .answer-description {
      max-width: 700px;
      margin-inline: auto;
      margin-top: 1rem;
      padding: 2rem 2.25rem;
      background-image: url('/jagged-border.svg');
      background-repeat: no-repeat;
      background-size: 100% 100%;

      .rich-text {
        padding-block: 0;
      }
    }
  }

  .help-modal {
    position: fixed;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #4063f6b2;
    backdrop-filter: blur(4px);
    z-index: 10;

    .modal-content {
      position: relative;
      display: flex;
      flex-direction: column;
      width: 100%;
      max-width: 700px;
      max-height: calc(100vh - 5rem);
      margin-inline: auto;
      padding: 0.5rem;
      background-image: url('/jagged-border.svg');
      background-repeat: no-repeat;
      background-size: 100% 100%;

      .close-button {
        position: absolute;
        top: 1.5rem;
        right: 1.5rem;
        width: 2.5rem;
        height: 2.5rem;
        padding: 0;
        border: none;
        background: transparent;
        cursor: pointer;

        svg {
          width: 100%;
          height: 100%;
        }
      }

      .modal-body {
        padding: 2rem 2.25rem;
        overflow-y: auto;

        .title-section {
          flex: 1;
          font-weight: 600;

          .name {
            margin-bottom: 0.25rem;
            font-family: var(--font-family-alt);
            font-size: 2rem;
            text-transform: uppercase;
          }

          .desc {
            font-size: 1.25rem;
          }
        }
      }
    }
  }
}
</style>
