<template>
    <section id="home">
      <!-- Home -->
        <div class="title-group">
            <h1>{{ this.content ? this.content.title : "" }}</h1>
            <h2 class="home">{{ this.content ? this.content.home : "" }}</h2>  
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
}
</script>


<style>
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

</style>