<template>
    <nav id="nav">
        <!-- Auth -->
        <div class="auth" v-if="!this.userSettings">
          <span class="auth-method" href="#">Registration 
            <i class="fas fa-money-check icon"></i>
          </span>
          <span class="separator">|</span>
          <span class="auth-method" href="#">Login 
            <i class="fas fa-sign-in-alt icon"></i>
          </span>   
        </div>
        <div class="auth" v-else-if="this.userSettings">
          <span class="auth-method user">{{this.userSettings.user}}
            <i class="fas fa-user icon"></i>
            <span class="tooltiptext">edit profile</span>
            </span> 
          <span class="separator">|</span>
          <span class="auth-method sign-out">Logout
            <i class="fas fa-sign-out-alt icon"></i>
            </span> 
        </div>
        <!-- Theme switch -->
        <div class="theme-switch-wrapper">
        <span id="toggle-icon">
            <span id="toggle-text" class="toggle-text">Light Mode</span>
            <i class="mode fas fa-sun"></i>
        </span>
        <label class="theme-switch">
            <input type="checkbox" v-model="dark" >
            <div class="slider round"></div>
        </label>
        </div>
        <!-- Navigations -->
        <div class="main-nav">
          <select name="projects" id="projects" :value="project" @change="changeProject" >
              <option value="Mainpage"><a href="#projects">MainPage</a></option>
              <option value="proj1"><a href="#projects">Project1</a></option>
          </select>
          <a href="#home">Home</a>
          <a href="#about">About</a>
          <a href="#contact" v-show="userSettings !== (undefined || null)">Contact</a>
        </div>
    </nav>
</template>

<script>
import { apiService } from "../common/api.service";
const settingsEndpoint = "/api/settings/";

export default {
    name: "NavbarComponent",
    props: {
      project: {
        type: String,
        required: true
      }
    },
    emits: ["project-change"],
    data() {
        return {
            userSettings: undefined,
            dark: false || localStorage.getItem("Dark"),
        }
    },
    methods: {
        getUserSettings() {  
            apiService(settingsEndpoint)
                .then(settings => {
                    //console.log(data), // settings object
                    this.userSettings = settings 
                    this.dark = settings.dark
                }).catch(err=> console.log(err))
        },
        changeUserSettings() {
            const method = "PUT";
            const data = {
                "dark": this.dark,
                "tagline": "update via comput"
            }
            apiService(settingsEndpoint, method, data)
        },
        changeProject(event) {
          this.$emit("project-change", event.target.value)
        },
    }, 
    computed: {
      darkTheme() {
          this.dark ? document.documentElement.setAttribute("data-theme", "dark") : 
          document.documentElement.setAttribute("data-theme", "light") 
          return this.dark
      },
      themeChange() {
        this.changeUserSettings();
        localStorage.setItem("Dark", this.dark)
        return this.dark
      }
      
    },
    created: function () {
        this.getUserSettings();
        //this.changeUserSettings()
    },
    
}
//const DARK_THEME = "dark";
//const LIGHT_THEME = "light";
//const currentTheme = localStorage.getItem("theme");
</script>

<style>
/* Navigation */
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

nav {
  z-index: 10;
  position: fixed;
  font-size: 24px;
  letter-spacing: 3px;
  padding: 25px;
  width: 100vw;
  background: var(--nav);
}

a {
  margin-right: 25px;
  color: var(--primary-color);
  text-decoration: none;
  border-bottom: 3px solid transparent;
  font-weight: bold;
}
select {
    letter-spacing: 0.15rem;
    border-bottom: 3px solid transparent;
    font-size: 24px;
    font-weight: bold;
    border-width: 0;
    margin-right: 25px;
    cursor: pointer;
    color: var(--primary-color);
    background: var(--select);
}

select:hover, select:focus {
  color: var(--on-background);
  border-bottom: 3px solid;
}
select:focus-visible {
  outline: -webkit-focus-ring-color none;
}

option {
  font-family: 'Font Awesome 5 Brands';
  background: var(--background);
}

a:hover,
a:focus {
  border-bottom: 3px solid;
  color: var(--on-background);
}
span {
  font-weight: bold;
  margin: 0 10px 0 10px ;
}
a .user {
  text-decoration:none;
}
.fa-user {
  position: relative;
}
.tooltiptext {
  visibility: hidden;
  background-color: var(--help-text-background);
  color: var(--help-text);
  text-align: center;
  border-radius: 6px;
  padding: 5px 10px;
  position: absolute;
  z-index: 1;
  opacity: 0;
  transition: opacity 2s;
  margin-top: 55px;
  font-size: 10px;
  margin-left: 53px;
  width: 55px;
  letter-spacing: 0.1px;
  filter: brightness(1.5);
}

.user:hover .tooltiptext{
  visibility: visible;
  opacity: 1;
}

.fa-user:hover {
  text-shadow: 0px 0px 7px #348eaf8f;
  color: green;
}
/* Dark Mode Toggle */
.theme-switch-wrapper {
  display: flex;
  align-items: center;
  z-index: 100;
  position: fixed;
  right: 25px;
  top: 20px;
}

.auth {
  position: absolute;
}
.auth-method {
    text-shadow: 10px 20px 10px var(--mode-text);
    color: var(--auth-method);
    top: -8px;
    position: relative;
    margin-right: 0;
    font-size: 1rem;
    display: inline-flex;
    align-items: center;
}
.sign-out:hover {
  color:var(--auth-hover);
}
.separator {
  color: var(--auth-method);
  top: -8px;
  font-size: 1.5rem;
  position: relative;
}

.theme-switch-wrapper span {
  margin-right: 10px;
    color:var(--mode-text);
    text-shadow: 10px 20px 10px var(--mode-text);
    font-size: 1.1rem;
}

.theme-switch-wrapper:hover {
  filter: brightness(var(--mode-brightness));
}

.toggle-text {
  position: relative;
  top: -4px;
  right: 5px;
  color: var(--on-background);
}

.theme-switch {
  display: inline-block;
  height: 34px;
  position: relative;
  width: 60px;
}

.theme-switch input {
  display: none;
}

.fas {
  font-size: 30px;
  margin-right: 5px;
}
.mode {
  color: var(--mode);
}
.icon {
  font-size: 20px;
  margin-left: 7px;
}
.slider {
  background: #716f6f;
  bottom: 0;
  cursor: pointer;
  left: 0;
  position: absolute;
  right: 0;
  top: 0;
  transition: 0.4s;
}

.slider::before {
  background: #fff;
  bottom: 4px;
  content: "";
  height: 26px;
  left: 4px;
  position: absolute;
  transition: 0.4s;
  width: 26px;
}

input:checked + .slider {
  background: var(--primary-color);
}

input:checked + .slider::before {
  transform: translateX(26px);
}

.slider.round {
  border-radius: 34px;
}

.slider.round::before {
  border-radius: 50%;
}
.main-nav, select {
  text-shadow: -1px 3px 5px;
}

</style>