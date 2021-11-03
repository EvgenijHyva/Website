<template>
    <section id="home">
      <!-- Home -->
      <div class="title-group">
        <transition appear
          enter-active-class="animate__animated animate__fadeInDown"
          enter-leave-class="animate__animated animate__bounceOut"
        >
          <h1>{{ this.content ? this.content.title : "" }}</h1>
        </transition>      
          <transition name="zoom" type="animation" appear>
            <h2 class="home" >{{ this.content ? this.content.home : "" }}</h2>  
          </transition>
      </div>
    </section>
</template>

<script>


export default {
  name: 'Home',
  props: {
    content: {
      required: true
    }
  },
  data() {
    return {
      flag : false,
    }
  },
}
</script>


<style>
.animate__animated {
  animation-duration: 0.5s;
}

/* Home Section */
.title-group {
  text-align: center;
  max-width: 1000px;
}
h1 {
  font-family: Caveat, sans-serif ;
  font-size: 100px;
  margin-bottom: 0;
  color: var(--title-alt);
  text-shadow: 10px 18px 5px var(--title-shadow);
}
h2 {
  font-size: 32px;
  font-weight: normal;
  color: var(--on-background-alt);
}
.home {
  background: linear-gradient(to right, var(--home));
  padding: 30px;
  border-radius: 20px;
  text-shadow: 1px 3px 1px var(--home-shadow);
}
/* animation */
@keyframes zoom-in {
  from {
    transform: scale(0, 0);
  }
  to {
    transform: scale(1, 1);
  }
}
.zoom-enter-active {
  animation: zoom-in 1s linear forwards;
  transition: all 1s linear;
}
.zoom-enter-from {
  opacity: 0;
}

@media screen and (max-width: 600px) {
  h2 {
    font-size: 25px
  }
  .home {
    margin: 1vh;
    padding: 10vw;
  }
}

</style>