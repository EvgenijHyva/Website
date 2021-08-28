<template>
  <div class="container">
    <navbar-component 
    :project="activeProject" 
    @project-change="changeActiveProject" />
    <!-- name of component should be imported to component -->
    <transition name="change" mode="out-in">
      <component :is="activeProject"></component>
    </transition>
    <!-- <keep-alive> component </keep-alive> to store in memory-->
  </div>
</template>

<script>
import NavbarComponent from "./components/Navbar.vue";
import Mainpage from "./components/MainPage.vue";
import Project from "./components/Project.vue";
import Slider from "./components/Slider.vue";
import Calculator from "./components/Calculator.vue";
import AuthModal from "./components/AuthModal.vue";
import QuoteGenerator from "./components/QuoteGenerator.vue"

import { apiService } from "./common/api.service";
const settingsEndpoint = "/api/settings/";

export default {
  name: "App",
  components: {
    NavbarComponent, Mainpage, Project, Slider, Calculator, AuthModal,
    QuoteGenerator
  },
  data() {
    return {
      activeProject: localStorage.getItem("Project") || "Mainpage",

      userSettings : null,
    }
  },
  methods: {
    changeActiveProject(value) {
      this.activeProject = value;
      localStorage.setItem("Project", this.activeProject)
    },

    getUserSettings() {  
      apiService(settingsEndpoint)
        .then(settings => {
        //console.log(data), // settings object
          if (settings){
            this.$store.state.authModalShow = false, 
            this.$store.state.userDarkThemeMode = settings.dark,
            this.$store.state.user = settings.user
            this.userSettings = settings
          }
          else {
            this.$store.state.authModalShow = true
          }
        }).catch(err=> console.log(err))
    },
  },
  beforeMount: function () {
    this.getUserSettings()
  },
}
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}



@import url('https://fonts.googleapis.com/css2?family=Caveat&family=Comfortaa&family=Kaushan+Script&family=Lobster&family=Ma+Shan+Zheng&family=Parisienne&display=swap');

:root {
  --primary-color: rgb(255, 92, 92);
  --primary-variant: #ff2d2d;
  --secondary-color: #1b9999;
  --on-primary: rgb(250, 250, 250);
  --on-background: rgb(66, 66, 66);
  --on-background-alt: rgba(66, 66, 66, 0.7);
  --background: rgb(255, 255, 255);
  --box-shadow: 0 5px 20px 1px rgba(0, 0, 0, 0.5);
  --title-alt: #0d062b9e; 
  --title-shadow: #de868670 ;
  --home: #005aa742, #f3f1d8b0;
  --home-shadow: #f314001; 
  --select: rgb(255 255 255 / 50%);
  --nav: rgb(255 255 255 / 50%);
  --auth-method: #08085dc2;
  --mode: #ff5c5c ;
  --mode-text: #ff5c5c ;
  --mode-brightness: 1.1;
  --auth-hover: rgb(111 181 59);
  --help-text: var(--primary-variant); 
  --help-text-background: #7c7c7d ;
  --contact-icons: var(--primary-color);
  --contact-hover: #464a68;
  --contact-shaddow: #9393e6;
  --text-box: rgb(0 0 0 / 50%) ;
  --calculator-shadow: 9px 22px 27px 25px rgb(163 18 18 / 50%);
  --calculator-background: #e4e896;
  --calculator-display-num-color: #cc9544;
}

[data-theme="dark"] {
  --primary-color: rgb(150, 65, 255);
  --primary-variant: #6c63ff;
  --secondary-color: coral;
  --on-primary: #000;
  --on-background: rgb(249 246 255);
  --on-background-alt: rgba(255, 255, 255, 0.7);
  --background: #121212;
  --title-alt: #9dc10cc7;
  --title-shadow: #4d12b970;
  --home: #9f61f742, #756d07b0;
  --home-shadow: #2900f3;
  --select: rgb(98 91 99 / 0%);
  --nav: rgb(98 91 99 / 50%);
  --auth-method: #f1b037;
  --mode: #6563d0;
  --mode-text: #170340;
  --mode-brightness: 1.2;
  --auth-hover: #ff1a02;
  --help-text: #abdc16; 
  --help-text-background: #0ee25f30 ;
  --contact-icons: rgb(160 66 245);
  --contact-hover: rgb(152 7 7);
  --contact-shaddow: #fb2323de;
  --text-box: rgb(255 255 255 / 50%);
  --calculator-shadow: 10px 9px 33px 7px rgb(101 101 149 / 50%);
  --calculator-background: #f0f0f0;
  --calculator-display-num-color: #2f9af5;
}

html {
  box-sizing: border-box;
  scroll-behavior:smooth;
}

body {
  user-select: none;
  font-family: Comfortaa, sans-serif;
  margin: 0;
  color: var(--on-background);
  background-color: var(--background);
  background-image: url("data:image/svg+xml,%3Csvg width='42' height='44' viewBox='0 0 42 44' xmlns='http://www.w3.org/2000/svg'%3E%3Cg id='Page-1' fill='none' fill-rule='evenodd'%3E%3Cg id='brick-wall' fill='%239C92AC' fill-opacity='0.4'%3E%3Cpath d='M0 0h42v44H0V0zm1 1h40v20H1V1zM0 23h20v20H0V23zm22 0h20v20H22V23z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}

section {
  min-height: 100vh;
  display: flex;    
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.change-enter-from {
  opacity: 0;
}
.change-enter-active {
  transition: all 1s linear;
}
.change-enter-to {
  opacity: 1;
}
.change-leave-from {
  opacity: 1;
}
.change-leave-active {
  transition: all 1s ;
}
.change-leave-to {
  opacity: 0;
}

</style>
