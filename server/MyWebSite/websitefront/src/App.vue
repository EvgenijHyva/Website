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
    <backgrounds />
  </div>
</template>

<script>
import NavbarComponent from "./components/Navbar.vue";
import Mainpage from "./components/MainPage.vue";
import Bookmarks from "./components/Bookmarks.vue";
import Slider from "./components/Slider.vue";
import Calculator from "./components/Calculator.vue";
import AuthModal from "./components/AuthModal.vue";
import QuoteGenerator from "./components/QuoteGenerator.vue";
import SpockRockGame from "./components/SpockRockGame.vue";
import Backgrounds from "./components/Backgrounds.vue";
import Kanban from "./components/Kanban.vue";
import MathSprint from "./components/MathSprint.vue";
import NasaApod from "./components/NasaApod.vue";


import { apiService } from "./common/api.service";

export default {
  name: "App",
  title() {
      return "Main page"
  },
  components: {
    NavbarComponent, Mainpage, Bookmarks, Slider, Calculator, AuthModal,
    QuoteGenerator, SpockRockGame, Backgrounds, Kanban, MathSprint,
    NasaApod
  },
  data() {
    return {
      settingsEndpoint: "/api/settings/",
      activeProject: "Mainpage",
      userSettings : null,
    }
  },
  methods: {
    changeActiveProject(value) {
      this.activeProject = value;
      localStorage.Project = this.activeProject;
    },

    getUserSettings() {  
      apiService(this.settingsEndpoint)
        .then(settings => {
        //console.log(data), // settings object
          if (settings){
            this.$store.state.authModalShow = false, 
            this.$store.state.userDarkThemeMode = settings.dark,
            this.$store.state.user = settings.user,
            this.$store.state.background = settings.background
            this.userSettings = settings
          }
          else {
            this.$store.state.authModalShow = true
          }
        }).catch(err=> console.log(err))
    },
  },
  async created() {
    await this.getUserSettings()
  },
  beforeMount: function () {
    if (localStorage.Project)
      this.activeProject = localStorage.Project
  }
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
  --nav-small-menu: #d8d8d8f5;
  --nav-animated-bars: black;
  --primary-color: rgb(255, 92, 92);
  --primary-variant: #ff2d2d;
  --secondary-color: #1b9999;
  --on-primary: rgb(250, 250, 250);
  --on-background: rgb(66, 66, 66);
  --on-background-secondary: rgb(125 132 138);
  --on-background-alt: rgba(66, 66, 66, 0.7);
  --background: rgb(223 219 226);
  --box-shadow: 0 5px 20px 1px rgba(0, 0, 0, 0.5);
  --title-alt: #0d062b9e; 
  --title-shadow: #de868670 ;
  --home: #005aa742, #f3f1d8b0;
  --home-shadow: #f314001; 
  --select: rgb(232 223 247 / 0%);
  --nav: rgb(210 192 239 / 50%);
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
  --quote-container-background: rgb(193 214 244 / 68%);
  --quote-loader: #c2b6258c;
  --quote-loader-alt: #b52d2d;
  --quote-button-shadow: 4px 0.3rem rgb(218 117 30 / 42%);
  --quote-icons: rgb(252 160 23 / 87%);
  --quote-icons-shadow:#7979d5c7;
  --bookmarks-root: #7450ab;
  --border-radius: 5px;   
  --bookmarks-title-shadow:#ffffff;
  --bookmarks-link: #3aff92;
  --bookmarks-link-background: rgb(24 22 151 / 60%);
  --Spock-rock-game-primary-color: whitesmoke;
  --header: dodgerblue;
  --container-shadow-color: rgba(0, 0 ,0, 0.5);  
  --computer-select-color: rgb(180,43,52);
  --mode-brightness: 50%;
  --selected-icon: #98201a;
  --selected-icon-color: #9ff7a4;
  --score-info: #000000;
  --slider-loader: rgb(56 70 138 / 30%);
  --slider-scroll: #d84747;
  --slider-background: var(--background);
  --toggle-background: #585858bd;
  --column-1: #a2622d;
  --column-1-alt: #a2622d74;
  --column-2: #1b6161;
  --column-2-alt: #1b616157;
  --column-3: #248224;
  --column-3-alt: #24822458;
  --column-4: #bd2517;
  --column-4-alt: #8a0d027a;
  --screen-width: 80vh;
  --header-screen-width: 10vh;
  --kanban-li-back: rgb(231 232 228 / 0.7);
  --kanban-drag-column: rgba(0, 0, 0, 0.7);
  --math-primary-color: dodgerblue;
  --select-color: dodgerblue;
  --success: rgb(15, 158, 2);
  --danger: rgb(214, 23, 23);
}

[data-theme="dark"] {
  --nav-small-menu: #4e0a3ce8;
  --nav-animated-bars:#fff;
  --primary-color: rgb(150, 65, 255);
  --primary-variant: #6c63ff;
  --secondary-color: coral;
  --on-primary: #000;
  --on-background: rgb(249 246 255);
  --on-background-secondary: var(--background);
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
  --mode-text: #6a5ffb;
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
  --quote-container-background: rgb(160 146 16 / 71%);
  --quote-loader: #ff4e4e8c;
  --quote-loader-alt: #2d5db5;
  --quote-button-shadow: 4px 0.3rem rgb(226 15 142 / 42%);
  --quote-icons: rgb(160 66 245);
  --quote-icons-shadow:#fb2323de ;
  --bookmarks-root: #7450ab;
  --bookmarks-title-shadow:#01830570;
  --bookmarks-link: #7d8ffa;
  --bookmarks-link-background: rgb(151 106 22 / 50%);
  --Spock-rock-game-primary-color: rgb(244 246 246 / 65%);
  --header: #5c3f84;
  --container-shadow-color: rgba(0, 0 ,0, 0.5); /* test */
  --computer-select-color: rgb(180,25, 25); /* test */
  --mode-brightness: 90%; /* test */
  --selected-icon: rgb(83, 35, 255); /* test */
  --selected-icon-color: #9ff7a4;
  --score-info: #fefe0285;
  --slider-loader: rgb(165 52 52 / 30%);
  --slider-scroll: #5872ee;
  --slider-background: #121212e0;
  --toggle-background: #6c63ff59 ;
  --kanban-li-back: #e8785f66;
  --kanban-drag-column: rgba(0, 0, 0, 0.8);
  --math-primary-color: dodgerblue;
  --select-color: dodgerblue;
  --success: rgb(15, 158, 2);
  --danger: rgb(214, 23, 23);
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

::-webkit-scrollbar {
  width: 5px;
  height: 0;
}
::-webkit-scrollbar-track {
  background: #5872ee;/*#d84747;*/
  border-radius: 50px;
  margin-right: 0;
}
::-webkit-scrollbar-thumb {
  background:  linear-gradient(to right, #ff4e50, #f9d423); /*#7778af*/
  border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
  background: #d84747;
}

@keyframes animated-scrollig {
    0% { 
        -webkit-transform: translate3d(0,0,0);
    }
    100% {
        -webkit-transform: translate3d(-2420px, 0, 0)
    }
}
.animated {
    animation: animated-scrolling 180s linear infinite; /*HERE TO animate*/
}


@media screen and (max-width: 600px) { 
  section {
    width: 100vw;
  }
  h1 {
    font-size: 5vh;
  }
}


.fade-enter-from {
  opacity: 0;
}
.fade-enter-to {
  opacity: 1;
}
.fade-enter-active {
  transition: all 1s linear;
}
.fade-leave-from {
  opacity: 1;
}
.fade-leave-active {
  transition: all 1s linear;
}
.fade-leave-to {
  opacity: 0;
}

</style>
