import { createRouter, createWebHistory } from 'vue-router'
import IntroView from '../views/IntroView.vue'
import ChapterListView from '../views/ChapterListView.vue'
import ChapterView from '../views/ChapterView.vue'
import ChapterIntroView from '../views/ChapterIntroView.vue'
import ChapterPageView from '../views/ChapterPageView.vue'
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
      component: ChapterListView,
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
          path: 'stran/:pageId',
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
