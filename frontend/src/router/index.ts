import { createRouter, createWebHistory } from 'vue-router'
import IntroView from '../views/IntroView.vue'
import ChaptersListView from '../views/ChaptersListView.vue'
import ChapterView from '../views/ChapterView.vue'
import ChapterIntroView from '../views/ChapterIntroView.vue'
import ChapterQuestionView from '../views/ChapterQuestionView.vue'
import ChapterResultView from '../views/ChapterResultView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'intro',
      component: IntroView,
    },
    {
      path: '/seznam-poglavij',
      name: 'chapters-list',
      component: ChaptersListView,
    },
    {
      path: '/poglavje/:id',
      name: 'chapter',
      component: ChapterView,
      children: [
        {
          path: 'intro',
          name: 'chapter-intro',
          component: ChapterIntroView,
        },
        {
          path: 'vprasanje/:questionId',
          name: 'chapter-question',
          component: ChapterQuestionView,
        },
        {
          path: 'rezultat',
          name: 'chapter-result',
          component: ChapterResultView,
        },
      ],
    },
    // {
    //   path: '/about',
    //   name: 'about',
    //   // route level code-splitting
    //   // this generates a separate chunk (About.[hash].js) for this route
    //   // which is lazy-loaded when the route is visited.
    //   component: () => import('../views/AboutView.vue')
    // }
  ],
})

export default router
