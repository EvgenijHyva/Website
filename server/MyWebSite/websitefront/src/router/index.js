import { createRouter, createWebHistory } from 'vue-router'
import Base from "@/components/Base.vue";
import AppAuthModal from '@/components/AuthModal.vue'



const routes = [
  {
    path: '/auth/:tab/',
    name: 'Auth',
    // route level code-splitting
    // this generates a separate chunk (auth.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component:AppAuthModal,
    props: true,
    meta: {
      keepAlive:false
    }
  },
  {
    path: '/'  ,
    name: 'Base',
    component: Base,
    meta: {
      keepAlive: true
    }
  },
  {
    path: '/forum/',
    name: 'Forum',
    component: () => import(/* webpackChunkName: "NotFound", */ "@/components/ForumBase.vue"),
    meta: {
      keepAlive: false
    }
  },
  {
    path: '/forum/:slug/',
    name: 'Forum-question-detail',
    component: () => import(/* webpackChunkName: "NotFound", */ "@/views/QuestionDetail.vue"),
    props: true,
    meta: {
      keepAlive: false
    },
  },

  
  {
    path: "/:catchAll(.*)",
    name:"Page not found",
    component: () => import(/* webpackChunkName: "NotFound", */  '../components/NotFound.vue'),
    meta: {
      keepAlive: false
    }
  }
]

const router = createRouter({
  history: createWebHistory("/"), // process.env.BASE_URL
  routes
})



export default router
