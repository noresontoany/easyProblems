import { createRouter, createWebHistory } from 'vue-router'
import AdminView from '@/views/AdminView.vue'
import TestView from '@/views/TestView.vue'
import LoginView from '@/views/LoginView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/students",
      name: AdminView,
      component: AdminView,
      props: {resource: "students"}
    },
    {
      path: "/languages",
      name: AdminView,
      component: AdminView,
      props: {resource: "programingLanguages"}
    },
    {
      path: "/lessons",
      name: AdminView,  
      component: AdminView,
      props: {resource: "lessonNames"}
    },
    {
      path: "/problems",
      name: AdminView,
      component: AdminView,
      props: {resource: "problems"}
    },
    {
      path: "/submissions",
      name: AdminView,
      component: AdminView,
      props: {resource: "submissions"}
    },
    {
      path: "/study",
      name: AdminView,
      component: AdminView,
      props: {resource: "students"}
    },
    {
      path: "/login",
      name: LoginView,
      component: LoginView
    }

  ]
})

export default router
