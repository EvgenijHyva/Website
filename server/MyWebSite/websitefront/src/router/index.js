import { createRouter, createWebHistory } from 'vue-router'
import AppAuthModal from "@/components/AuthModal.vue"
import NotFound from "@/components/NotFound.vue"

const routes = [
  {
    path: '/auth/:tab',
    name: 'Auth',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "auth", */  '../components/AuthModal.vue'),
    props: true
  }, 
  {
    path: '/',
    name: 'authmodal',
    component: AppAuthModal
  },
  {
    path: "/:catchAll(.*)",
    component: NotFound
  }
]

const router = createRouter({
  history: createWebHistory(), // process.env.BASE_URL
  routes
})

export default router
