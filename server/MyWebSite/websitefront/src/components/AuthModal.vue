<template>
    <section class="auth-main-container" v-if="showAuth && tab" @click="hideAuth" >
        <app-register-form v-if="tab==='register'" :user=user />
        <app-login-form v-else-if="tab==='login'" :user=user />
        <app-edit-form v-else-if="tab === 'edit'" :user=user />
    </section>
</template>

<script>
import AppLoginForm from './AuthLoginForm.vue';
import AppRegisterForm from './AuthRegisterForm.vue';
import AppEditForm from './AuthEditForm.vue';
import { mapState } from "vuex";

export default {
    name: "AuthModal",
    data() {
        return {
            previous: null,
        }
    },
    components: { 
      AppRegisterForm, AppLoginForm, AppEditForm
    },
    props: {
        tab: {
            type: String
        }
    },
    computed: {
      ...mapState(["user", "showAuth"]), // maping state doesn need getter
    }, 
    methods: {
        hideAuth(event) {
            if (event.target.classList.contains("auth-main-container"))
                this.$store.state.showAuth = false
        }
    },
    watch : {
      tab: {
        handler(oldVal, newVal) {
            if (this.previous === newVal) {
                this.$store.state.showAuth = !this.$store.state.showAuth
            } else if (this.previous !== oldVal)
                this.previous = oldVal
            this.$store.state.showAuth = true
        }
      }
    }
}
</script>

<style >
 .form-group label {
    color: #029008;
    margin: .5vh;
}

.error-message {
    color: #d24610;
    margin: .5vh;
}

.auth-main-container {
    position: fixed;
    z-index: 10;
    background: #0000008a;
    width: 100%;
}
</style>
