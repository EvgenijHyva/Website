<template>
    <section>
        <h1>Slider Unsplash API</h1> 
        <transition-group name="fade">
            <div class="loader" id="loader" v-if="!loaded">
                <img src="../assets/Blocks-1s-200px.svg" alt="loading">
                <span class="loading-text"> Loading from <a href="https://api.unsplash.com" target="_blank"> https://api.unsplash.com</a></span>
            </div>    
        
        <div class="image-container" v-else >  
            <div class="image-wrapper animated" v-for="image in photosArray" :key="image.id">
                <img class="image" :src="image.urls.regular" 
                :title="image.location.title ? image.location.title : 'Untitled'" 
                :alt="image.alt_descriptiong ? image.alt_descriptiong : 'Image loading failed'" 
                @click="showImage"> 
                <div class="image-info">
                   <p class="text">Author: {{image.user.name}} ({{image.user.username}})</p>
                   <p class="text" v-if="image.user.instagram_username"> Instagram link: 
                       <a v-if="`${image.user.instafram_username}`.includes('https://www.instagram.com/')" 
                            :href="image.user.instagram_username" 
                            target="_blank" class="instagram-link"> {{image.user.instagram_username}}</a> 
                       <a v-else    
                            :href="'https://www.instagram.com/'+image.user.instagram_username+'/'" 
                            target="_blank" class="instagram-link"> {{image.user.instagram_username}}</a> 
                   </p>
                   
                   <span class="created_at" v-if="image.created_at"> created: {{ image.created_at ? image.created_at : "No data :(" }}</span>
                </div> 
            </div>
            <div class="modal-image" ref="fullScreenImage" :class="{'show': showFullScreen}">
                    <div class="full-screen-image-wrapper" @click="showFullScreen = !showFullScreen">
                        <img class="modal-image-content"  > 
                        <span id="caption"></span>
                </div>
            </div>
        </div>
        
        </transition-group>

    </section>
</template>

<script>
//https://www.w3schools.com/howto/howto_js_slideshow_gallery.asp
//https://animate.style/

import { apiService } from "../common/api.service";

export default {
    name: "Slider",
    title() {
      return "Slider API"
    },
    data() {
        return { 
            pictureCount: 30,
            photosArray: [],
            loaded: false,
            showFullScreen: false,
        }
    },
    methods: {
        addItem(ind) {
            this.numbers.splice(ind, 1)
            const num = Math.floor(Math.random()*100+1)
            const index = Math.floor(Math.random()*this.numbers.length)
            this.numbers.splice(index,0, num)
        },
        getPhotos () {
            const apiKey = 'D_aDnrARt6sVfmknOgRgeHLjqKebX9pzozYcZZCME3s';
            let API = `https://api.unsplash.com/photos/random/?client_id=${apiKey}&count=${this.pictureCount}`
            this.loaded = false
            apiService(API)
                .then(photos => {
                    this.photosArray.push(...photos)
                    this.loaded = true
                })
        },
        showImage(e) {
            let component = this.$refs["fullScreenImage"]
            component.childNodes[0].childNodes[0].src=e.target.src
            component.childNodes[0].childNodes[1].textContent=e.target.title
            this.showFullScreen = true
        }
    },
    beforeMount: function () {
        this.getPhotos();
    }
}

</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Lato&display=swap');

h1 {
    font-size: 50px;
    font-family: lato, Lobster;
    margin-bottom: 1vh;
    margin-top: 12vh ;
}
img {
    height: 32.3vh;
    width: 25vw;
}
.image-container {
    border: none;
    margin: auto;
    width: 90vw;
    height: 66vh;
    display: flex;
    flex-wrap: wrap;
    flex-direction: column;
    overflow-x: hidden; /* scroll add a scroll bar*/
    overflow-y: hidden ;
    padding: 0;
    background: var(--slider-background);
}

@keyframes scroll-grid {
    0% { 
        -webkit-transform: translate3d(0,0,0);
    }
    100% {
        -webkit-transform: translate3d(-2500px, 0, 0)
    }
}
.animated {
    animation: scroll-grid 180s linear infinite; /*HERE TO animate*/
}

::-webkit-scrollbar {
    height: 10px;
    width: 5px;
}
::-webkit-scrollbar-track {
    background: var(--slider-scroll);
    border-radius: 0px 0px 10px 10px;
}
::-webkit-scrollbar-thumb {
    background:  linear-gradient(to right, #ff4e50, #f9d423); /*#7778af*/
    border-radius: 50px;
}
::-webkit-scrollbar-thumb:hover {
    background: rgb(29, 86, 24);
}

.image {
    margin: auto;
    margin-right: 5px ;
}
.image-info {
    width: 100%;
    transition: .5s ease;
    opacity: 0;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    -ms-transform: translate(-50%, -50%);
    text-align: center;
}
.image-wrapper {
    position: relative;
    z-index: 5;
}
.image-wrapper:hover .image {
    opacity: 0.2;
}
.image-wrapper:hover .image-info {
    opacity: 1;
}
.text {
    color: var(--title-alt);
    line-height: 25px;
    font-size: 15px;
    font-family:  Caveat ,Lato, Parisienne;
}
.created_at {
    font-size:10px;
    font-family: Lato, Comfortaa;
    color: var(--score-info);
    margin: auto;
}
.instagram-link {
    font-size: 20px;
}
.modal-image {
    overflow-y: hidden;
    display: none; 
    position: fixed; 
    z-index: 10; 
    left: 0;
    top: 0;
    width: 100%; 
    height: 100%; 
    overflow: auto; 
    background-color: rgba(0,0,0,0.5); 
}
.show {
    display: block;
}

.modal-image-content {
    padding-top: 15vh; /* Location of the box */
    margin: auto;
    display: block;
    width: 80%;
    max-width: 50vw;
    max-height: 80vh;
    height: 80%;
}
.full-screen-image-wrapper {
    position: relative;
}
#caption {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
  text-align: center;
  color: #ccc;
  padding: 10px 0;
  height: 150px;
}

@keyframes zoom {
  from {transform:scale(0)}
  to {transform:scale(1)}
}

.modal-image-content {
    animation-name: zoom;
    animation-duration: 1s;
}

/* Container for image text */
.caption-container {
  text-align: center;
  background-color: #222;
  padding: 2px 16px;
  color: white;
}

@media screen and (max-width: 1024px) {
    .image-container {
        width: 89vw;
        height: 45vh;
    }
    .modal-image-content {
        max-width: 90vw;
    }
    ::-webkit-scrollbar {
        height: 5px;
    }
    img {
        height: 22vh;
    }
}

@media screen and (max-width: 375px) {
    img {
        width: 87vw;
        height: 37vh;
    }
    h1 {
        margin-top:  5vh;
    }
    section {
        align-items:unset;
    }
    .image {
        margin-right: 0 ;
    }
    .image-container {
        width: 95vw;
        height: 75vh;
        display: unset;
        margin: auto;
    }
    .modal-image-content {
        max-width: 90vw;
        margin-top: 10vh;
    }
    ::-webkit-scrollbar {
        width: 7px;
    }
    ::-webkit-scrollbar-track {
        border-radius: 25px;
    }
    ::-webkit-scrollbar-thumb {
        border-radius: 50px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgb(29, 86, 24);
    }
    .image-container {
        overflow-y: hidden; /*scroll*/
        overflow-x: hidden ;
    }
    @keyframes scroll-grid {
    0% { 
        -webkit-transform: translate3d(0,0,0);
    }
    100% {
        -webkit-transform: translate3d(0, -2500px, 0)
    }
}
}

.loader {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: var(--slider-loader);
}

.loader img {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    opacity: 0.8;
}
.loading-text {
    position: fixed;
    top: 20vh;
    left: 40vw;
    color: var(--on-background);
}



</style>