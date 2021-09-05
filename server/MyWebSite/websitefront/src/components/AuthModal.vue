<template>
    <section>
        <h1>Auth-form</h1>
        <app-register-form v-if="tab==='register'" />
        <app-login-form v-else-if="tab==='login'" />
        <button @click="toggle"> {{ tab }}</button>
    </section>
</template>

<script>
import AppLoginForm from './LoginForm.vue';
import AppRegisterForm from './RegisterForm.vue';

export default {
    components: { 
      AppRegisterForm, AppLoginForm 
    },
    name: "AuthModal",
    data() {
        return {
            tab: "login",
        }
    },
    methods: {
        toggle() {
            console.log("test")
            this.tab = this.tab === 'register'? 'login': 'register'
        }
    }
}
</script>
