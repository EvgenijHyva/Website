import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VeeValidatePlugin from "./includes/validation"

createApp(App)
.use(VeeValidatePlugin)
.use(store)
.use(router)
.mount('#app');
