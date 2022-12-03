import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',      
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/lobby',
      name: 'lobby',      
      component: () => import('../components/Lobby.vue')
    },
    {
      path: '/login',
      name: 'login',      
      component: () => import('../components/Login.vue')
    },
    {
      path: '/register',
      name: 'register',      
      component: () => import('../components/Register.vue')
    },
    {
      path: '/game',
      name: 'game',      
      component: () => import('../components/Game.vue')
    },
  ]
})

export default router
