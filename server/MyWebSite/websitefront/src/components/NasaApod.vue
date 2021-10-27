<template>
    <section>
        <transition-group  mode="out-in" name="fade" >
            <div class="loader" v-show="loading" key="rocket">
                <img src="../assets/rocket.svg" alt="Rocket">
            </div>
            <div class="nasa-container" key="pages">
            <!-- Navigation -->
            <div class="navigation-container" >
                <span class="background"></span>
                <!-- Results Nav -->
                <span class="navigation-items" id="resultsNav" :class="{'hidden': tab === 'favorites'}">
                    <h3 class="clickable" @click="toggleTabs">Favorites</h3>
                    <h3>&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;</h3>
                    <h3 class="clickable" @click="loadMore">Load More</h3>
                </span>
                <!-- Favorites Nav -->
                <span class="navigation-items" id="favoritesNav" :class="{'hidden': tab === 'results'}">
                    <h3 class="clickable" @click="toggleTabs">Load More Nasa Images</h3>
                </span>
            </div>
                <div class="images-container" v-show="!loading" ref="container">
                    <transition-group name="articlesFade" mode="out-in" tag="div"
                        enter-active-class="animate__animated animate__fadeIn"
                        leave-active-class="animate__animated animate__fadeOut">
                    <div class="card" v-for="article in articles" :key="article">
                        <a :href="article.hdurl" title="View Full Image" target="_blank">
                            <img :src="article.url" alt="NASA Picture of the Day"
                            class="card-img-top" loading="lazy"> 
                        </a>
                        <div class="card-body">
                            <h5 class="card-title">{{article.title}}</h5>
                            <p class="clickable" @click="toggleFavorites(article)" >
                                {{tab !== "results" ? "Remove from favorites" :  favorites[article.url] ? "Remove from favorites" : "Add to Favorites"  }}
                            </p>
                            <p class="card-text"> {{article.explanation}} </p>
                            <small class="text-muted">
                                <strong>{{article.date}}</strong>
                                <span> {{article.copyright ? article.copyright : ""}}</span>
                            </small>
                        </div>
                    </div> 
                    </transition-group>     
                </div>
            </div>
        </transition-group>
        <transition tag="div" mode="out-in" 
            enter-active-class="animate__animated animate__zoomIn"
            leave-to-class="animate__animated animate__zoomOut">
            <div class="save-confirmed" v-if="showMessage">
                <h1>{{message}}</h1>
            </div>
        </transition>
    </section>
</template>

<script>
import {apiService} from "../common/api.service"
//
export default {
    name: "NasaApod",
    title() {
      return "Nasa API"
    },
    data() {
        return {
            loading: true,
            favorites: {},
            articles: [],
            pages: [],
            count: 10,
            tab: "results",
            message: "",
            showMessage: false
        }
    },
    methods: {
        getNasaArticles() {
            const API_key = "bmAIOIxPkuiRkvTsIwJtkRXX5zIwp2sntaJY7g38"
            let API_URL = `https://api.nasa.gov/planetary/apod?api_key=${API_key}&count=${this.count}`
            this.articles.length = 0 // clear array
            apiService(API_URL) 
            .then(data => {
                if (data) {
                    this.articles = data
                }
            })
            .catch(err=> console.log(err))
        },
        toggleTabs() {
            this.tab = this.tab === "results" ? "favorites" : "results"
        },
        toggleFavorites(article){
            //add and remove favorite articles 
            if (this.favorites[article.url]) {
                delete this.favorites[article.url]
                this.toggleInfo("Removed from list!")
            } else {
                this.favorites[article.url] = article
                this.toggleInfo("Added succefully!")
            }
            
        },
        scrollToTop() {
            this.$refs["container"].scrollTo({
                top: 0,
                behavior: "smooth"
            })
        },
        loadMore() {
            this.scrollToTop()
            this.getNasaArticles()
        }, 
        toggleInfo(context) {
            this.message = context
            this.showMessage = true
        },
        storeFavorites() { 
            if (Object.values(this.favorites).length)
                localStorage.setItem("NasaFavorites", JSON.stringify(this.favorites))
            else
                localStorage.removeItem("NasaFavorites")
        },
        getFavorites() {
            if (localStorage.getItem("NasaFavorites")) {
                this.favorites = JSON.parse(localStorage.getItem("NasaFavorites"))
            }
        }
    },
    beforeMount: function () {
        this.getNasaArticles()
        this.getFavorites()
    },
    watch: {
        showMessage: function () {
            if (this.showMessage) {
                setTimeout(() => {
                this.showMessage = false
            }, 3000)
            }
        },
        "articles.length": function () {
            if (!this.articles.length) {
                this.loading = true
            } else {
                this.loading = false
            }
        },
        tab: function () {
            if (this.tab === "favorites" &&  Object.values(this.favorites).length) {
                this.pages = this.articles
                this.articles = Object.values(this.favorites)
            } else if (this.tab === "results" && this.pages.length) {
                this.articles = this.pages
            } else {
                this.toggleInfo("You have no favorites articles yet")
                this.tab = "results"
            }
            this.scrollToTop()
        },
        favorites: {
            handler() {
                if (this.tab === "favorites") {
                    this.articles = Object.values(this.favorites)
                }
                setTimeout(this.storeFavorites, 10000)
                if (!Object.values(this.favorites).length) {
                    this.tab = "results"
                }
            }, deep:true 
        },
         
    }
}
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Markazi+Text&display=swap');
img {
    width: 10vw;
    height: 15vh;
}

section {
    font-family: Verdana, sans-serif;
    font-size: 1rem;
    line-height: 1.8rem;
}

a{
  margin-right:0 ;
}

.nasa-container {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 5px;
}


/* Loader */
.loader {
  background: #eec6ff4d;
  height: 100vh;
  width: 100vw;
  display: flex;
  position: fixed;
  justify-content: center;
  align-items: center;
  z-index: -1;
}


/* Navigation */
.navigation-container {
  position: fixed;
  top: 12.5vh;
}

.navigation-items {
  display: flex;
  justify-content: center;
}

.background {

  position: fixed;
  width: 100%;
  z-index: -1;
}
.clickable {
  color: dodgerblue;
  cursor: pointer;
  user-select:none;
}
.clickable:hover {
  filter: brightness(75%);
}

/* Images Container */
.images-container {
  width: 800px;
  margin-top: 15vh;
  height: 80vh;
  overflow: scroll;
}

.card {
  
  background: white;
  margin: 0 10px 20px;
  border-radius: 5px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
}

.card:hover {
  box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.2);
}

.card-img-top {
  align-self: center;
  width: 100%;
  height: auto;
  border-radius: 5px 5px 0 0;
}

.card-body {
  padding: 20px;
}

.card-title {
  margin: 10px auto;
  font-size: 24px;
}

/* Save Confirmation */
.save-confirmed {
  background: #e4bebe;
  padding: 3px 16px;
  border-radius: 10px;
  box-shadow: 5px 6px 11px 0 rgb(0 0 0 / 50%);
  transition: 0.3s;
  position: fixed;
  bottom: 25px;
  left: 50px;
  font-family: 'Markazi Text', sans-serif;
  /*animation: popup 5s;*/
}
.save-confirmed h1 {
    margin: auto;
    font-size: 3vh;
}

@keyframes popup {
  0% {
    opacity: 0;
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0;
  }
}


.save-confirmed h1 {
  text-shadow: 5px 7px 10px #af7c6c;
    color: #626735;
}

/* Hidden */
.hidden {
  display: none;
}

/* Large Smartphone (Vertical) */
@media screen and (max-width: 800px) {
  body {
    line-height: 1.4rem;
    font-size: 0.9rem;
    text-align: justify;
  }
  img {
      width: 30vw;
      height: 40vw;
  }
  .images-container {
    width: 95vw;
  }

  .card-title {
    font-size: 20px;
  }

  .save-confirmed {
    right: 25px;
  }
  .save-confirmed {
    bottom: 5vh;
  } 
  .save-confirmed h1 {
    font-size: 2vh;
  }
  .images-container {
    margin-top: 8vh;
  }
  .navigation-container{
    top: 8.5vh;
  }
}

::-webkit-scrollbar {
    width: 7px;
    height: 0;
}
::-webkit-scrollbar-track {
  background: #bd256ba6;
}

</style>