<template>
    <section class="auth-main-container" v-show="tab" @click="hideAuth" >
        <app-register-form v-if="tab==='register'" :user="user" />
        <app-login-form v-else-if="tab==='login'" :user="user" />
        <app-edit-form v-else-if="tab === 'edit'" :user="user" />
    </section>
</template>

<script>
import AppLoginForm from './AuthLoginForm.vue';
import AppRegisterForm from './AuthRegisterForm.vue';
import AppEditForm from './AuthEditForm.vue';
import { mapState } from "vuex";

export default {
    name: "AuthModal",
    title() {
        return "Mainpage"
    },
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
      ...mapState(["user", "showAuth",]),
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
        },
        user: function() {
            if(this.user !== "Anonymous") { // if user is authenticated redirect to mainpage
            this.$router.push("/")
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
    z-index: 10;
    width: 100%;
}
.background-hide {
    background: #0000008a;
    z-index: 1;
    width:100%;
    height: 100%;
}

</style>
