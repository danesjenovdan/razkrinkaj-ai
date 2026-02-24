import { createRouter, createWebHistory } from "vue-router";
import RootView from "../views/RootView.vue";
// import IntroView from '../views/IntroView.vue'
// import TacticsView from '../views/TacticsView.vue'
import CalendarView from "../views/CalendarView.vue";
// import ChapterView from '../views/ChapterView.vue'
// import ChapterPageView from '../views/ChapterPageView.vue'
// import ChapterResultView from '../views/ChapterResultView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition;
    } else if (to.path === from.path) {
      return;
    } else {
      return { top: 0 };
    }
  },
  routes: [
    {
      path: "/",
      name: "root",
      component: RootView,
      children: [
        {
          path: "",
          name: "intro",
          component: CalendarView,
        },
        // {
        //   path: 'koledar',
        //   name: 'calendar',
        //   component: CalendarView,
        // },
        // {
        //   path: 'taktike',
        //   name: 'tactics',
        //   component: TacticsView,
        // },
        // {
        //   path: 'dan/:slug',
        //   name: 'chapter',
        //   component: ChapterView,
        //   children: [
        //     {
        //       path: '',
        //       name: 'chapter-intro',
        //       component: ChapterPageView,
        //     },
        //     {
        //       path: 'stran/:pageIndex',
        //       name: 'chapter-page',
        //       component: ChapterPageView,
        //     },
        //     {
        //       path: 'rezultat',
        //       name: 'chapter-result',
        //       component: ChapterResultView,
        //     },
        //   ],
        // },
      ],
    },
  ],
});

export default router;
