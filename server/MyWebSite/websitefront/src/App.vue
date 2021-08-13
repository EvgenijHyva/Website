<template>
  <div class="container">
    <NavbarComponent/>
    <Mainpage/>
</div>
</template>

<script>
import NavbarComponent from "./components/Navbar.vue"
import Mainpage from "./components/MainPage.vue"

export default {
  name: "App",
  components: {
    NavbarComponent, Mainpage,
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
  --primary-color: rgb(255, 92, 92);
  --primary-variant: #ff2d2d;
  --secondary-color: #1b9999;
  --on-primary: rgb(250, 250, 250);
  --on-background: rgb(66, 66, 66);
  --on-background-alt: rgba(66, 66, 66, 0.7);
  --background: rgb(255, 255, 255);
  --box-shadow: 0 5px 20px 1px rgba(0, 0, 0, 0.5);
}

[data-theme="dark"] {
  --primary-color: rgb(150, 65, 255);
  --primary-variant: #6c63ff;
  --secondary-color: coral;
  --on-primary: #000;
  --on-background: rgba(255, 255, 255, 0.9);
  --on-background-alt: rgba(255, 255, 255, 0.7);
  --background: #121212;
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

h1 {
  font-family: Caveat, sans-serif ;
  font-size: 100px;
  margin-bottom: 0;
}

h2 {
  font-size: 32px;
  font-weight: normal;
  color: var(--on-background-alt);
}


</style>
