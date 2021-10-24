<template>
    <div div class="container login" v-if="user === 'Anonymous'">
        <h1>Login!</h1>
     <vee-form 
        :validation-schema="loginSchema"
        @submit="login">
         <div class="form-field">
                <div class="form-group">
                    <label class="small mb-1" for="username">Username</label>
                    <vee-field name="username" type="text"
                        placeholder="Enter your Username">                    
                    </vee-field>
                    <ErrorMessage name="username"  class="error-message" />
                </div>
                <div class="form-group">
                    <label class="small mb-1" for="password">Password</label>
                    <vee-field name="password" type="password"
                        placeholder="Enter your password">          
                    </vee-field>
                    <ErrorMessage name="password"  class="error-message" />
                </div>
                <div class="button-group">
                    <button  type="submit" class="outline btn-primary" :disabled="log_on_submition">
                        Login
                    </button>
                    <button type="reset" class="outline btn-primary" >
                        Reset
                    </button>
                </div>
                <h1 v-show="log_show_alert">{{log_alert_msg}}</h1>
            </div>
        </vee-form>
    </div>
</template>

<script>
import { apiService } from "../common/api.service";

export default {
    name: "LoginForm",
    props: ["user"],
    title () {
        return "Authenticate yourself"
    },
    data () {
        return {
            loginSchema: {
               username: "required|min:1|max:30",
               password: "required|min:8|max:50"
            },
            log_on_submition: false,
            log_show_alert: false,
            log_alert_msg: "",
        }
    },
    methods: {
      async login(values) {
        const LoginPoint = "/api/dj-rest-auth/login/"
        this.log_show_alert = true;
        this.log_on_submition = true;
        this.log_alert_msg = "Please wait! We are logging you in.";
        apiService(LoginPoint, "POST", values)
          .then(response => {
            if (response.key) {
              this.$store.state.key = response.key
            } else {
              this.log_on_submition = false
              this.log_alert_msg= "Ooops error occured:" + response
            }
          })
        this.$store.state.showAuth = false
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