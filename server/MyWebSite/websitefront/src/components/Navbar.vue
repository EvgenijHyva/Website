<template>
    <nav id="nav">
        <!-- Auth -->
        <div class="auth" v-if="!this.userSettings">
          <span class="auth-method" href="#">Registration 
            <i class="fas fa-money-check icon"></i>
          </span>
          <span class="auth-method separator">|</span>
          <span class="auth-method" href="#">Login 
            <i class="fas fa-sign-in-alt icon"></i>
          </span>   
        </div>
        <div class="auth" v-else-if="this.userSettings">
          <span class="auth-method">{{this.userSettings.user}}
            <i class="fas fa-user icon"></i>
            </span> 
          <span class="auth-method separator">|</span>
          <span class="auth-method">Logout
            <i class="fas fa-sign-out-alt icon"></i>
            </span> 
        </div>
        <!-- Theme switch -->
        <div class="theme-switch-wrapper">
        <span id="toggle-icon">
            <span id="toggle-text" class="toggle-text">Light Mode</span>
            <i class="fas fa-sun"></i>
        </span>
        <label class="theme-switch">
            <input type="checkbox">
            <div class="slider round"></div>
        </label>
        </div>
        <!-- Navigations -->
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <select name="projects" id="projects">
            <option value="all"><a href="#projects">Projects</a></option>
            <option value="proj1"><a href="#projects">Project1</a></option>
        </select>
        <a href="#contact" v-show="userSettings !== (undefined || null)">Contact</a>
        
    </nav>
</template>

<script>
import { apiService } from "../common/api.service";
const settingsEndpoint = "/api/settings/";

export default {
    name: "NavbarComponent",
    data() {
        return {
            userSettings: undefined,
        }
    },
    methods: {
        getUserSettings() {  
            apiService(settingsEndpoint)
                .then(settings => {
                    //console.log(data), // settings object
                    this.userSettings = settings 
                }).catch(err=> console.log(err))
        },
        changeUserSettings() {
            const method = "PUT";
            const data = {
                "dark": true,
                "tagline": "update via apiservice"
            }
            apiService(settingsEndpoint, method, data)
        },
        changeTheme() {
          document.documentElement.setAttribute("data-theme", "dark")
        },
    }, 
    created: function () {
        this.getUserSettings()
        //this.changeUserSettings()
    }
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
  background: rgb(255 255 255 / 50%);
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
    background: rgb(255 255 255 / 50%);
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
  background: #ecf7dd;

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
.fa-user:hover {
  color:green
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
    top: -8px;
    position: relative;
    margin-right: 0;
    font-size: 1rem;
    display: inline-flex;
    align-items: center;
}
.auth-method:hover {
  color:green
}
.separator {
  font-size: 1.5rem;
}

.theme-switch-wrapper span {
  margin-right: 10px;
  font-size: 1rem;
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
.fa-sun {
  color:burlywood;
}
.icon {
  font-size: 20px;
  margin-left: 7px;
}
</style>