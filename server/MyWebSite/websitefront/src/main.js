import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import VeeValidatePlugin from './includes/validation';
import titleMixin from './mixins/titleMixin';
//import "./includes/firebase";

createApp(App)
.use(VeeValidatePlugin)
.use(store)
.use(router)
.mixin(titleMixin)
.mount('#app');
