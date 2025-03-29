import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import "./assets/css/reset.css";
import "./assets/css/main.css";

createApp(App).use(router).mount("#app");
