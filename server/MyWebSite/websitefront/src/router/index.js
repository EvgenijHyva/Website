import { createRouter, createWebHistory } from 'vue-router'
import Base from "@/components/Base.vue";
import AppAuthModal from '@/components/AuthModal.vue'



const routes = [
  {
    path: '/auth/:tab',
    name: 'Auth',
    // route level code-splitting
    // this generates a separate chunk (auth.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component:AppAuthModal,
    props: true
  },
  {
    path: '/'  ,
    name: 'Base',
    component: Base,
    meta: {
      KeepAlive: true
    }
  },
  {
    path: '/forum/',
    name: 'Forum',
    component: () => import(/* webpackChunkName: "NotFound",*/ "@/components/Forum.vue"),
    meta: {
      KeepAlive: false
    }
  },
  {
    path: "/:catchAll(.*)",
    name:"Page not found",
    component: () => import(/* webpackChunkName: "NotFound", */  '../components/NotFound.vue'),
    meta: {
      KeepAlive: false
    }
  }
]

const router = createRouter({
  history: createWebHistory("/"), // process.env.BASE_URL
  routes
})

export default router
