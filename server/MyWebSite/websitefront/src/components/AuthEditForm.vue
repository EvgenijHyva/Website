<template>
    <section v-if="user !== 'Anonymous'">
        <div class="container">
            <h1>{{message}}</h1>
                    <vee-form 
            :validation-schema="schema" 
            @submit="change"
            :initial-values="userDefaultData">
            <div class="form-field name">
                <div  class="form-group">
                    <label for="username">Username</label>
                    <vee-field name="username" type="text"
                    placeholder="Enter you username">                    
                    </vee-field>
                </div>
                <ErrorMessage name="username" class="error-message" />
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
            <div>
                <div class="form-group">
                    <label for="age">Age</label>
                    <vee-field name="age" type="number"
                        placeholder="Enter your age">                    
                    </vee-field>
                </div>
                <ErrorMessage name="age"  class="error-message" />
            </div>
            <div>
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
                        <option v-for="(key, value) in meta_choices" :value="key" :key="value">{{value}}</option>            
                    </vee-field>
                </div>
                <ErrorMessage name="gender"  class="error-message" />
            </div>
            <div  >
                <div class="form-group">
                    <label for="password1">Password</label>
                    <vee-field name="password1" type="password"
                        placeholder="Enter your password">             
                    </vee-field>
                </div>  
                <ErrorMessage name="password1"  class="error-message" />
            </div>
            <div >
                <div class="form-group">
                    <label for="password2">Confirm password</label>
                    <vee-field name="password2" type="password"
                        placeholder="Confirm password">                    
                    </vee-field>
                </div>
                <ErrorMessage name="password2" class="error-message" />
            </div>
            <div class="form-group send_mail">
                    <label for="send_mail">Allow to send me email</label>
                    <vee-field name="send_mail" type="checkbox" :value="!userDefaultData.send_mail" v-model="userDefaultData.send_mail" />                    
                <ErrorMessage name="send_mail"  class="error-message" />
            </div>
            <div class="button-group">
                <button type="submit" class="outline" >
                    Save
                </button>
            </div>
        </vee-form>
        </div>
    </section>
</template>

<script>
import { axios } from "../common/api.service.js";
import { mapState } from "vuex";

export default {
    name: "EditForm",
    props: ["user"],
    title () {
        return "Profile editing"
    },
    data() {
        return {
            message: "Edit your information",
            schema: {
                username: "required|min:3|max:150|alpha_spaces",
                email: "required|min:3|max:100|email",
                first_name: "min:2|max:30",
                last_name: "min:2|max:150",
                age: "min_value:18|max_value:99",
                password1: "required|min:8|max:50",
                password2: "password_mismatch:@password1",
                phone: "required|min_value:010000000|max_value:9999999999",
                gender: "required|exclude_gender:U,E,A,D",
            },
            userDefaultData: {
                username: "",
                email: null,
                first_name: "",
                last_name: "",
                gender: "D",
                phone: null,
                send_mail: false,
                avatar:null,
                age: null,
            },
        }
    },
    computed: {
      ...mapState(["meta_choices",]),
    },
    methods: {
        async change(values) {
            let method = "PUT"
            let endpoint = "/api/user/"
            try {
                let response = await axios({
                    method: method,
                    url: endpoint,
                    data: values
                })
                if (response.status==200){
                    console.log(response)
                } else {
                    console.log("resp_change", response)
                }
            } catch (err) {
                console.log(err)
            }
        },
        async getRegisteredData() {
            let endpoint = "/api/user/"
            try {
                let response = await axios.get(endpoint)
                if (response.status === 200) {
                    for ( let i in response.data) {
                        this.userDefaultData[i] = response.data[i]
                    }
                }
            } catch (err) {
                console.log(err)
            }
        }
    },
    created() {
        this.getRegisteredData()
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
  border-radius: 50px;
  box-shadow: 0 5px 30px 10px var(--auth-shadow);
}

.gender label{
    width: 5.7vw;
}
.send_mail label{
    width: 11vw;
    
}
.send_mail {
    flex-direction: row;
}
.send_mail input {
    width: 3vw;
}

select {
    font-size: 15px;
    color: #0a4416;
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
    .send_mail label{
        width: 21vw;
    }
    .send_mail {
        flex-direction: row;
    }
    .send_mail input {
        width: 3vw;
    }
}
@media screen and (max-width: 800px) {
    label {
        width: 40vw;
    }
    select {
        font-size: 10px;
    }
    .gender label {
        width: 26.7vw;
    }
    .container {
      margin-top: 5vh ;
      width: 95vw; 
      font-size: 1.5vh; 
      border-radius: 15px; 
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