<template>
    <section>
        <app-register-form v-if="tab==='register'" />
        <app-login-form v-else-if="tab==='login'" />
    </section>
</template>

<script>
import AppLoginForm from './LoginForm.vue';
import AppRegisterForm from './RegisterForm.vue';

export default {
    name: "AuthModal",
    title() {
      return "Authentication"
    },
    components: { 
      AppRegisterForm, AppLoginForm 
    },
    data() {
        return {
            tab: "register",
        }
    },
    methods: {
        toggle() {
            this.tab = this.tab === 'register'? 'login': 'register'
        }
    }
}
</script>

<style >
.error-message, label {
    color: #029008;
    margin: .5vh;
}
</style>
