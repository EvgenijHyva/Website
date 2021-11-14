<template>
  <div class="nav-container">
    <nav id="nav" :class="{'show': showMobileMenu , 'hide': !showMobileMenu}">
        <!-- Auth -->
        <div class="auth" 
        v-if="this.authModalShow" >
        <router-link :to="{ name : 'Auth', params: { tab: 'register'} }"  tag="span" 
            @click="showMobileMenu = false" 
            replace> 
          <span class="auth-method register" 
          href="#">Registration 
            <i class="fas fa-money-check icon"></i>
          </span>
          </router-link> 
          <span class="separator">|</span>

          <router-link :to="{ name : 'Auth', params: { tab: 'login'} }"  tag="span" 
           @click="showMobileMenu = false" 
           replace> 
          <span class="auth-method login" >Login 
            <i class="fas fa-sign-in-alt icon"></i>
          </span> 
          </router-link>  
        
        </div>
        <div class="auth" v-else>
        <router-link :to="{ name : 'Auth', params: { tab: 'edit'} }"  tag="span" 
            @click="this.$store.state.showAuth = !this.$store.state.showAuth,
            showMobileMenu = false" 
            replace> 
          <span class="auth-method user">{{this.user}}
            <i class="fas fa-user-edit icon" @click="editProfile"></i>
            <span class="tooltiptext">edit profile</span>
            </span> 
          </router-link> 
          <span class="separator">|</span>
          <span class="auth-method sign-out" @click="logout">Logout
            <i class="fas fa-sign-out-alt icon"></i>
            </span> 
        </div>
        <!-- Theme switch -->
        <div class="theme-switch-wrapper">
        <span id="toggle-icon">
            <span id="toggle-text" class="toggle-text">{{ this.userDarkThemeMode ? "Dark mode": "Light Mode"}}</span>
            <i class="mode fas " :class="{'fa-sun': !this.userDarkThemeMode, 'fa-moon': this.userDarkThemeMode }"></i>
        </span>
        <label class="theme-switch">
            <input type="checkbox" 
            v-model="this.$store.state.userDarkThemeMode" >
            <div class="slider round"></div>
        </label>
        </div>
        <!-- Navigations -->
        <div class="main-nav">
        
            <router-link :to="{'path': '/'}"> 
              <select name="projects" id="projects" :value="this.$store.state.activeProject" @change="changeProject">
                  <option value="Mainpage" title="Website mainpage">Mainpage</option>
                  <option value="Slider" title="Slider">Slider Api</option>
                  <option value="Bookmarks" title="Add your bookmarks">Bookmarks</option>
                  <option value="Calculator" title="Simple calculator">Calculator</option>
                  <option value="QuoteGenerator" title="Quote generator">Quotes</option>
                  <option value="SpockRockGame" title="Rock-Paper-Scissors-Lizard-Spock game">R-P-S-L-S</option>
                  <option value="Kanban" :title="user==='Anonymous'? 'Login required': 'Kanban board' " :disabled="user==='Anonymous'" >Kanban</option>
                  <option value="MathSprint" title="Math sprint game">Math game</option>
                  <option value="NasaApod" title="Nasa Apod">Nasa Apod</option>
              </select>
            </router-link>
          
          <router-link :to="{'path': '/forum/'}" :class="{'disabled-link': authModalShow}" :title="authModalShow? 'Login required': 'Forum'"> Forum </router-link>
        </div>
    </nav>
        <div class="menu-bars" id="menu-bars" :class="{'change': showMobileMenu}"
          @click="toggleNav">
          <div class="bar1"></div>
          <div class="bar2"></div>
          <div class="bar3"></div>
        </div>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { axios } from "../common/api.service";

export default {
    name: "NavbarComponent",
    data() {
      return {
        initial : true,
        showMobileMenu: false,
        timeout: null,
      }
    },
    computed: {
      //array or object can be used
      ...mapState(["authModalShow", "user", "userDarkThemeMode", "activeProject"]), // maping state doesn need getter
    },
    methods: {
      changeProject(event) {
        this.$store.state.activeProject = event.target.value
        localStorage.Project = this.activeProject;
      },
        
      setThemeMode() {     
        document.documentElement.setAttribute("data-theme", !this.userDarkThemeMode ?  "light" :"dark" )
        localStorage.setItem("Dark", this.userDarkThemeMode)
      },

      async uploadUserSettings() {
        if (this.user !== "Anonymous") {
          const method = "PUT";
          const endPoint = "/api/settings/";
          const data = {
            dark: this.userDarkThemeMode,
          }
          try {
            await axios({
              method: method,
              url: endPoint,
              data: data
            })
          } catch (err) {
            console.log(err)
          }
        }
      }, 
      toggleNav() {
        this.showMobileMenu = !this.showMobileMenu
      },
      async logout() {
        const endPoint = "/api/dj-rest-auth/logout/"
        const method = "POST"
        try {
          let response = await axios({
            method: method,
            url: endPoint,
          })              
          if(response.status === 200) {
            console.log(`loging out (${response.data.detail})`)
            this.$store.state.authModalShow = true
            this.$store.state.user = "Anonymous"
          } else {
            console.log("warning ",response)
          }
        } catch (err) {
          console.log(err)
        }
      },
      editProfile() {
        console.log("editing") // TODO edit profile
      },
    },
    mounted() {
      if (!this.userDarkThemeMode) {
        let storedLocal = localStorage.getItem("Dark")
        if (storedLocal) {
          this.$store.state.userDarkThemeMode = JSON.parse(storedLocal)
        }
      }
    },
    watch: {
      userDarkThemeMode : function () {
        this.setThemeMode()
        if (!this.initial) {
          clearTimeout(this.timeout)
          this.timeout = setTimeout(this.uploadUserSettings, 3000)
        }
        this.initial = false;
      }
    }
  }
</script>

<style>
/* Navigation */
#nav {
  padding: 20px 0;
}

#nav a {
  font-weight: bold;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

nav {
  z-index: 11;
  position: fixed;
  font-size: 24px;
  letter-spacing: 3px;
  width: 100vw;
  background: var(--nav);
}
.menu-bars {
  display: none;
}

a {
  color: var(--primary-color);
  text-decoration: none;
  border-bottom: 3px solid transparent;
  font-weight: bold;
}
select {
    display: inline-block;
    width: auto;
    letter-spacing: 0.15rem;
    border-bottom: 3px solid transparent;
    font-size: 24px;
    font-weight: bold;
    border-width: 0;
    cursor: pointer;
    color: var(--primary-color);
    background: var(--select);
    line-height: 1.3;
    box-sizing: border-box;
}
select.open::after {
    transform: translateY(50%) rotate(180deg);
}
select:focus {
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
.fa-user-edit {
  position: relative;
}
.fa-user-edit:hover {
  text-shadow: 0px 0px 7px #348eaf8f;
  color: green;
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
  top: 25px;
  font-size: 10px;
  width: 55px;
  letter-spacing: 0.1px;
  filter: brightness(1.5);
}

.user:hover .tooltiptext{
  visibility: visible;
  opacity: 1;
}
.login:hover, .register:hover {
  color: #029008;
}


/* Dark Mode Toggle */
.theme-switch-wrapper {
  display: flex;
  align-items: center;
  z-index: 100;
  position: absolute;
  right: 15px;
  top: 20px;
}

.auth {
    position: absolute;
    top: 15px;
    left: 10px;
}
.auth a  {
  margin-right: auto;
}

.auth-method {
    text-shadow: 10px 20px 10px var(--mode-text);
    color: var(--auth-method);
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
  font-size: 1.5rem;
  position: relative;
}

.theme-switch-wrapper span {
    margin-right: 7px;
    color:var(--mode-text);
    text-shadow: 10px 20px 10px var(--mode-text);
    font-size: 1.1rem;
    display: inline-block;
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
  margin-left: .5vw;
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
.disabled-link {
  cursor: not-allowed;
  pointer-events: none;
  text-decoration: line-through;
}
@media screen and (max-width: 1024px) { 
  span {
    margin: 0;
  }
  .theme-switch-wrapper {
    right: 1vw;
  }
}

@media screen and (max-width: 800px) { 
  .text {
    margin: 1vh;
    padding: 10vw;
  }
  .toggle-text {
    top: -8vh;
    right: -32vw;
  }
  
  .menu-bars {
    position: fixed;
    top: 1rem;
    right: 2rem;
    z-index: 15;
    display: inline;
    cursor: pointer;
  }
  .bar1,
  .bar2,
  .bar3 {
    width: 35px;
    height: 2px;
    background-color: var(--nav-animated-bars);
    margin: 8px 0;
    transition: 0.4s;
  }
  .change .bar1 {
    transform: rotate(-45deg) translate(-7px, 8px);
  }
  .change .bar2 {
    opacity: 0;
  }
  .change .bar3 {
    transform: rotate(45deg) translate(-6px, -8px);
  }
  #nav {
    height: 100vh;
    background: var(--nav-small-menu);
    padding: 0;
  }
  .hide {
    animation: hideMenu 2s;
    display: none;
  }
  .show{
    display: flex !important;
    flex-direction: column;
    animation: showMenu 2s;
  }
  .auth {
    position: unset;
    margin: 15vh 0 ;
  }
  .theme-switch-wrapper {
    position: unset;
  }
  .main-nav {
    display: flex;
    flex-direction: column;
    margin: 10vh 0 auto;
  }
  .main-nav select {
    margin: auto;
    width: 50vw;
  }
  @keyframes showMenu {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  @keyframes hideMenu {
   from {
     opacity: 1;
   } 
   to {
     opacity: 0;
   }
  }
}

</style>