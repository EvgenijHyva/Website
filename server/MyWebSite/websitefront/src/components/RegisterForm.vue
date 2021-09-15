<template>
    <div class="container">
        <h1>Sign Up Today!</h1>
        <vee-form 
            :validation-schema="schema" 
            @submit="register"
            :initial-values="userDefaultData">
            <div class="form-field name">
                <div  class="form-group">
                    <label for="name">Name</label>
                    <vee-field name="name" type="text"
                    placeholder="Enter you full name">                    
                    </vee-field>
                </div>
                <ErrorMessage name="name" class="error-message" />
            </div>
            <div>
                <div class="form-group">
                    <label for="name">Email</label>
                    <vee-field name="email" type="email"
                    placeholder="Enter you email">                    
                    </vee-field>
                </div>
                <ErrorMessage name="email"  class="error-message" />
            </div>
            <div>
                <div class="form-group">
                    <label for="first_name">Firstname</label>
                    <vee-field name="first_name" type="text"
                    placeholder="Enter your firstname">                    
                    </vee-field>
                </div>
                <ErrorMessage name="first_name"  class="error-message" />
            </div>
            <div  >
                <div class="form-group">
                    <label for="last_name">Lastname</label>
                    <vee-field name="last_name" type="text"
                    placeholder="Enter your lastname">                    
                    </vee-field>
                </div>
                <ErrorMessage name="last_name"  class="error-message" />
            </div>
            <div >
                <div class="form-group">
                    <label for="phone">Phone</label>
                    <vee-field name="phone" type="number"
                    placeholder="Enter your phone">                    
                    </vee-field>
                </div>
                <ErrorMessage name="phone"  class="error-message" />
            </div>
            <div >
                <div class="form-group gender">
                    <label for="gender">Gender</label>
                    <vee-field as="select" name="gender" >
                        <option value="D" disabled>----</option> 
                        <option value="M">Male</option> 
                        <option value="F">Female</option>               
                        <option value="T">Transgender</option>               
                        <option value="O">Other</option>
                        <option value="U">UFO</option>               
                    </vee-field>
                </div>
                <ErrorMessage name="gender"  class="error-message" />
            </div>
            <div  >
                <div class="form-group">
                    <label for="password">Password</label>
                    <vee-field name="password" type="password"
                        placeholder="Enter your password">             
                    </vee-field>
                </div>  
                <ErrorMessage name="password"  class="error-message" />
            </div>
            <div >
                <div class="form-group">
                    <label for="confirm_password">Confirm password</label>
                    <vee-field name="confirm_password" type="password"
                        placeholder="Confirm password">                    
                    </vee-field>
                </div>
                <ErrorMessage name="confirm_password" class="error-message" />
            </div>
            <div class="form-group tos">
                    <label for="tos">Accept terms of sercice</label>
                    <vee-field name="tos" type="checkbox" value="1" />                    
                <ErrorMessage name="tos"  class="error-message" />
            </div>
            <div class="button-group">
                <button type="submit" class="outline" :disabled="reg_in_submission">
                    Submit form
                </button>
                <button type="reset">Reset</button>
                </div>
        </vee-form>
    </div>
</template>

<script>

export default{
    name: "RegisterForm",
    data() {
        return {
            schema: {
                name: "required|min:3|max:150|alpha_spaces",
                email: "required|min:3|max:100|email",
                first_name: "min:2|max:150",
                last_name: "min:2|max:150",
                password: "required|min:8|max:50",
                confirm_password: "password_mismatch:@password",
                phone: "required|min_value:010000000|max_value:9999999999",
                gender: "required|exclude_gender:U,E,A,D",
                tos: "tos"
            },

            userDefaultData: {
                gender: "D",
            },

            reg_in_submission: false, // if request is processing
            reg_show_alert: false,
            reg_alert_msg: "Please wait! Your account is being created.",
        }
    },
     methods: {
        register(values) {
            // TODO 
            this.reg_show_alert = true;
            this.reg_in_submission = true;
            this.reg_alert_msg= "Please wait! Your account is being created.",
            // 
            this.reg_alert_msg = "Success! Your account has been created.";
            console.log(values);
        },
    }
}
</script>

<style scoped>

h1 {
  font-size: 2vh;
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

button {
  cursor: pointer;
  color: var(--auth-secondary-color);
  background-color: var(--auth-background-button);
  font-family: "VT323", "Allan", monospace, cursive;
  box-shadow: 0 1px 3px 3px var(--auth-shadow-buttons);
  border-radius: 5px;
  border: none;
  width: 100%;
  font-size: 20px;
  letter-spacing: 2px;
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

.form-group {
    display: flex;
    margin: .5vw auto;
}
label {
  width: 7vw;
  text-align: -webkit-auto;
}

.container {
  margin-top: 10vh;
  max-width: 600px;
  font-family: Texturina, sans-serif;
  width: 40vw;
  background-color: var(--auth-on-background-alt);
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 10px;
  box-shadow: 0 5px 30px 10px var(--auth-shadow);
}

.gender label{
    width: 5.7vw;
}
.tos label{
    width: 11vw;
    
}
.tos {
    flex-direction: row;
}
.tos input {
    width: 3vw;
}

select {
    border-radius: 10px;
    background-color: #DFDBE5;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='4' height='4' viewBox='0 0 4 4'%3E%3Cpath fill='%239C92AC' fill-opacity='0.4' d='M1 3h1v1H1V3zm2-2h1v1H3V1z'%3E%3C/path%3E%3C/svg%3E");
}

@media screen and (max-width: 1024px) {
    .container {
      width: 60vw;   
      font-size: 20px;
    }
    label {
        width: 30vw;
    }
    .gender label {
        width: 20.5vw
    }
    .container {
      max-width: 800px;
      margin-top: 5vh ;
      width: 95vw; 
      font-size: 1.5vh;  
    }
    .tos label{
        width: 21vw;
    }
    .tos {
        flex-direction: row;
    }
    .tos input {
        width: 3vw;
    }
}
@media screen and (max-width: 600px) {
    label {
        width: 40vw;
    }
    .gender label {
        width: 26.7vw;
    }
    .container {
      margin-top: 5vh ;
      width: 95vw; 
      font-size: 1.5vh;  
    }
    .tos label{
        width: 25vw;
    }
    .tos {
        flex-direction: row;
    }
    .tos input {
        width: 3vw;
    }
}

</style>