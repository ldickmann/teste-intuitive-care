import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    pat: "/",
    name: "home",
    component: () => import("../views/HomeView.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
