<template>
  <section id="about" v-if="content">
        <h1>About myself</h1>
        <div class="about-container">
            <div class="about-image-container image-container" v-show="content.image">
                <img :src="content.image" alt="Photo" id="image">
                <div class="overlay">
                  <div class="text">My photo</div>
                </div>
            </div>
            <div class="text-box" id="text_box">
              <p>{{content.about}}</p>
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
  }
}
</script>

<style>

.about {
  position: relative;
  width: 50%;
  max-width: 300px;
}

.about .image {
  display: block;
  width: 100%;
  height: auto;
}

.overlay {
  font-family: Ma Shan Zhen;
  position: absolute; 
  bottom: 0;
  right: 0;
  left: 0; 
  background: rgba(0, 0, 0, 0.5); /* Black see-through */
  width: 100%;
  transition: .5s ease;
  opacity:0;
  color: white;
  font-size: 20px;
  padding: 10px;
  text-align: center;
}

.about-image-container:hover .overlay {
  opacity: 1;
}
.about-container {
  display: flex;
  max-width: 1000px;
  justify-content: center;
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
.about-image-container {
  padding: unset;
  margin-right: 3px;
  overflow: hidden;
  position: relative;
}
.image-container img {
  height: auto;
  width: 300px;
}

.text-box {
  width: 40%;
  text-align: justify;
  background-color: var(--text-box);
  color: var(--on-primary);
  border-radius: 10px;
  padding: 30px;
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
  .text-box {
    width: 95vw;
    height: fit-content;
  }
 .image-container img {
    max-height: 70vh;
    width: 90vw;
  }
}


</style>