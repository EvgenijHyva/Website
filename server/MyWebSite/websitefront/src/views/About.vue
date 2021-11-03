<template>
  <section id="about" v-if="this.content">
    <!-- About -->
        <h1>Undraw Illustrations</h1>
        <div class="about-container">
            <div class="image-container">
                <h2>Savings</h2>
                <img :src="this.content.image" alt="Photo" id="image1">
            </div>
            <div class="image-container">
                <h2>Photos</h2>
                <img src="images/Light_undraw_Photos_re_pvh3.svg" alt="Photos" id="image2">
            </div>
            <div class="image-container">
                <h2>Floating</h2>
                <img src="images/Light_undraw_Floating_re_xtcj.svg" alt="Floating" id="image3">
            </div>
        </div>
    </section>
</template>

<script>
export default {
  name: "About",
  props: {
    content: {
      required: true
    }
  },
  beforeUnmount() {
    console.log("unmounting about comp")
  }
}
</script>

<style>
/* About Section */
.about-container {
  display: flex;
}

.image-container {
  border: 1px solid var(--secondary-color);
  border-radius: 10px;
  padding: 10px 20px;
  margin-right: 25px;
  width: auto;
  background: var(--background);
  box-shadow: var(--box-shadow);
}

img {
  height: 300px;
  width: 300px;
}
@media screen and (max-width: 600px) {
  .about-container {
    display: flex;
    flex-direction: column;
    margin: 1vh;
  }
  .image-container {
    margin: 1vh; 
  }
}


</style>