import { createRouter, createWebHistory } from 'vue-router'
import RootView from '../views/RootView.vue'
import IntroView from '../views/IntroView.vue'
import ChapterListView from '../views/ChapterListView.vue'
import ChapterView from '../views/ChapterView.vue'
import ChapterIntroView from '../views/ChapterIntroView.vue'
import ChapterPageView from '../views/ChapterPageView.vue'
import ChapterResultView from '../views/ChapterResultView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  },
  routes: [
    {
      path: '/',
      name: 'root',
      component: RootView,
      children: [
        {
          path: '',
          name: 'intro',
          component: IntroView,
        },
        {
          path: 'seznam-poglavij',
          name: 'chapter-list',
          component: ChapterListView,
        },
        {
          path: 'poglavje/:id',
          name: 'chapter',
          component: ChapterView,
          children: [
            {
              path: 'intro',
              name: 'chapter-intro',
              component: ChapterIntroView,
            },
            {
              path: 'stran/:pageIndex',
              name: 'chapter-page',
              component: ChapterPageView,
            },
            {
              path: 'rezultat',
              name: 'chapter-result',
              component: ChapterResultView,
            },
          ],
        },
      ],
    },
  ],
})

export default router
