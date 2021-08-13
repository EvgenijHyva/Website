<template>
    <section id="home">
      <!-- Home -->
        <div class="title-group">
            <h1>{{ this.content ? this.content.title : "" }}</h1>
            <h2>{{ this.content ? this.content.home : "" }}</h2>  
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

</style>