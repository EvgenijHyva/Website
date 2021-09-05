<template>
    <div>
        <h6 v-if="reg_show_alert" class="text text-alt">{{reg_alert_msg}}</h6>
     <vee-form 
        :validation-schema="loginSchema"
        @submit="login">
         <div class="form-field email">
                <div>
                    <label for="name">Email</label>
                    <vee-field name="email" type="email"
                        placeholder="Enter your email">                    
                    </vee-field>
                    <ErrorMessage name="email"  class="error-message" />
                </div>
                <div>
                    <label for="password">Password</label>
                    <vee-field name="password" type="password"
                        placeholder="Enter your password">          
                    </vee-field>
                    <ErrorMessage name="password"  class="error-message" />
                </div>
                <div>
                    <button type="submit" class="outline" :disabled="log_on_submition">
                        login
                    </button>
                    <button type="reset" class="outline" >
                        reset
                    </button>
                </div>
            </div>
        </vee-form>
    </div>
</template>

<script>
export default {
    name: "LoginForm",
    data () {
        return {
            loginSchema: {
               email: "required|email",
               password: "required|min:8|max:50"
            },

            log_on_submition: false,
            reg_in_submission: false, // if request is processing
            reg_show_alert: false,
            reg_alert_msg: "Please wait! Your account is being created.",
        }
    },
    methods: {
          login(values) {
            this.reg_show_alert = true;
            this.log_on_submition = true;
            this.reg_alert_msg = "Please wait! We are logging you in.";
            console.log(values)
        }
    }
}
</script>

<style scoped>
form {
    max-width: 800px;
    border: 1px solid var(--secondary-color);
    border-radius: 5px;
    padding: 5px;
    background-color: #91c0df;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='152' height='152' viewBox='0 0 152 152'%3E%3Cg fill-rule='evenodd'%3E%3Cg id='temple' fill='%23896805' fill-opacity='0.4'%3E%3Cpath d='M152 150v2H0v-2h28v-8H8v-20H0v-2h8V80h42v20h20v42H30v8h90v-8H80v-42h20V80h42v40h8V30h-8v40h-42V50H80V8h40V0h2v8h20v20h8V0h2v150zm-2 0v-28h-8v20h-20v8h28zM82 30v18h18V30H82zm20 18h20v20h18V30h-20V10H82v18h20v20zm0 2v18h18V50h-18zm20-22h18V10h-18v18zm-54 92v-18H50v18h18zm-20-18H28V82H10v38h20v20h38v-18H48v-20zm0-2V82H30v18h18zm-20 22H10v18h18v-18zm54 0v18h38v-20h20V82h-18v20h-20v20H82zm18-20H82v18h18v-18zm2-2h18V82h-18v18zm20 40v-18h18v18h-18zM30 0h-2v8H8v20H0v2h8v40h42V50h20V8H30V0zm20 48h18V30H50v18zm18-20H48v20H28v20H10V30h20V10h38v18zM30 50h18v18H30V50zm-2-40H10v18h18V10z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
div {
    flex-grow: 1;
}

.form-field {
    display: flex;
    flex-direction: column;
}

label {
    color: var(--on-primary);
    margin-right: 10px;
}
input {
    border-radius: 10px;
    margin: 5px 0 5px 0;
    padding: 5px;
}
option {
    color: orange;
}
select {
    letter-spacing: 0.15rem;
    border-bottom: 3px solid transparent;
    font-size: 15px;
    font-weight:lighter;
    border-width: 0;
    margin-right: auto;
    cursor: pointer;
    color: black;
    background: var(--select); 
}
.error-message {
    color:  var(--primary-variant);
}
.text {
    color: var(--primary-variant)
}
.text-alt {
    background: var(--help-text-background);
    padding: 5px;
    border-radius: 5px;
    margin: 3px;
}

</style>