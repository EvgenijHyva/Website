<template>
    <div div class="container login" v-if="user === 'Anonymous'">
        <h1>Login!</h1>
     <vee-form 
        :validation-schema="loginSchema"
        @submit="login">
         <div class="form-field">
                <div class="form-group">
                    <label class="small mb-1" for="name">Email</label>
                    <vee-field name="email" type="email"
                        placeholder="Enter your email">                    
                    </vee-field>
                    <ErrorMessage name="email"  class="error-message" />
                </div>
                <div class="form-group">
                    <label class="small mb-1" for="password">Password</label>
                    <vee-field name="password" type="password"
                        placeholder="Enter your password">          
                    </vee-field>
                    <ErrorMessage name="password"  class="error-message" />
                </div>
                <div class="button-group">
                    <button  type="submit" class="outline btn btn-primary" :disabled="log_on_submition">
                        Login
                    </button>
                    <button type="reset" class="outline btn btn-primary" >
                        Reset
                    </button>
                </div>
                <h6 v-if="reg_show_alert" class="text text-alt">{{reg_alert_msg}}</h6>
            </div>
        </vee-form>
    </div>
</template>

<script>
export default {
    name: "LoginForm",
    props: ["user"],
    title () {
        return "Authenticate yourself"
    },
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
      async login(values) {
        //const LoginPoint = "/api/dj-rest-auth/login/"
        this.reg_show_alert = true;
        this.log_on_submition = true;
        this.reg_alert_msg = "Please wait! We are logging you in.";
        console.log(values)
      }
    }
}
</script>

<style scoped>
h1 {
  font-size: 3vh;
  margin: 10px 0;
  font-family: Texturina;
  text-shadow: none;
}

form {
  width: 90%;
}

input {
  background-color: var(--auth-on-background);
  opacity: 0.8;
  font-family: "Lora", "serif";
  color: var(--auth-secondary-color-variant);
  border-radius: 10px;
  width: 100%;
  padding: 5px;
  height: 34px;
  border: 1px solid var(--auth-secondary-color);
  outline:none;
  box-sizing: border-box;
  transition: all 1s;
}
input:hover {
  filter: brightness(var(--auth-input-brighness));
}
input:valid {
  background-color: var(--auth-valid);
  border: 1px solid green;
}
input:invalid {
  background-color: var(--auth-invalid);
  border:1px solid red;
  color: #c1f523;
}

.button-group {
    display: flex;
    margin: 1vh 0 3vh 0;
}
.button-group button {
    flex-grow: 1;
    margin: auto;
}
.button-group button:first-child {
  margin-right: 10px;
}

button {
  cursor: pointer;
  color: var(--auth-secondary-color);
  background-color: var(--auth-background-button);
  font-family: "VT323", "Allan", monospace, cursive;
  box-shadow: 0 1px 2px 2px var(--auth-shadow-buttons);
  border-radius: 5px;
  border: none;
  height: 4vh;
  width: 100%;
  font-size: 20px;
  letter-spacing: 2px;
}

button:hover {
  filter: brightness(130%);
  background: var(--auth-button-hover);
}
button:active {
  transform: translate(0, 2px);
}

.button-container {
  display: flex;
  flex-grow: 1;
}

.form-group {
  display: flex;
  flex-direction: column;
  margin: .5vh auto;
}
label {
  position: relative;
  bottom: 3px;
}

.container {
  max-width: 600px;
  font-family: Texturina, sans-serif;
  width: 40vw;
  background-color: var(--auth-on-background-alt);
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 50px;
  box-shadow: 0 5px 30px 10px var(--auth-shadow);
}


@media screen and (max-width: 1024px) {
    .container {
      width: 60vw;   
      font-size: 20px;
    }
}
@media screen and (max-width: 600px) {
    .container {
      width: 95vw; 
      font-size: 1.5vh;  
      border-radius: 15px;
    }
}

</style>