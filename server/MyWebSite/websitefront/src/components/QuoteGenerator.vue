<template>
    <section>
        <transition appear mode="out-in"
            enter-active-class="animate__animated animate__zoomInDown"
            leave-active-class="animate__animated animate__zoomOutDown">
            <div v-if="!loading">
                <h1>Quotes Generator</h1>
                <div class="quote-container" id="quote-container">
                    <div class="quote-text">
                        <i class="fas fa-theater-masks"></i>
                        <span id="quote" 
                        :class="{ 'long-quote':quote.text.length > 100 }">
                        {{ quote.text }}
                        </span>
                        <div class="quote-author">
                            <span id="author"> {{ quote.author ? quote.author : "Unknown Author" }}</span>
                        </div>
                        <div class="button-container">
                            <button class="twitter-button" id="twitter" 
                            title="Tweet this!" @click="tweetQuote">
                                <i class="fab fa-twitter">
                                </i>
                            </button>
                            <button class="bullhorn" id="bullhorn" hidden>
                                <audio id="audio" controls hidden></audio>
                                <i class="fas fa-bullhorn"></i>
                            </button>
                            <button id="new-quote" @click="selectQuote">
                                new quote
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </transition>
        <transition appear mode="out-in" 
            enter-active-class="animate__animated animate__fadeIn"
            leave-active-class="animate__animated animate__fadeOut">
            <div class="loader" id="loader" v-if="loading"></div>
        </transition>
    </section>
</template>

<script>
import { apiService } from "../common/api.service";
import { localQuotes } from "../common/localQuotes";

export default {
    name: "QuoteGenerator",
    title() {
      return "Quote Generator"
    },
    data() {
        return {
            apiQuotes : [],
            quote: "",
            apiUrl : "https://type.fit/api/quotes",
            loading : false,
        }
    },
    methods: {
        getQuotes() {
            this.loading = true;
            apiService(this.apiUrl)
            .then(data=> {
                this.apiQuotes.push(...data)
                this.selectQuote();
                })
            .catch(err => {
                    console.log("error occured: '" + err + "'. Taken quote from local storage")
                    this.apiQuotes = localQuotes
                    this.selectQuote();
                }
            )     
        },
        selectQuote() {
            this.quote = this.apiQuotes[Math.floor(Math.random()*this.apiQuotes.length)]
            this.loading = false;
        },
        tweetQuote() {
            let twitterUrl = `https://twitter.com/intent/tweet?text=${this.quote.text} - ${this.quote.author}`;
            window.open(twitterUrl, '_blank');
        },
    },
    created() {
        this.getQuotes()
    }
}
</script>

<style scoped>
.animate__animated {
  animation-duration: 2s;
}
.quote-container {
    width: auto;
    max-width: 900px;
    padding: 20px 30px;
    border-radius: 10px;
    background-color: var(--quote-container-background);
    box-shadow: 0 10px 10px 10px rgba(0,0,0, 0.2);
}

.quote-text {
    font-size: 2.75rem;
}

.long-quote {
    font-size: 2rem;
}

.fa-quote-left {
    font-size: 4rem;
}
.fa-bullhorn {
    font-size: 25px;
    text-shadow: 4px 6px 5px var(--quote-icons-shadow);
}
.fas, .fab {
    margin-right: 0;
    color: var(--quote-icons);
}
.fa-theater-masks {
    color: darkred;
}
.fa-bullhorn:hover {
    color: var(--contact-hover);
}

.quote-author {
    margin-top: 15px;
    font-size: 2rem;
    font-weight: 400;
    font-style: italic;
}

.button-container {
    margin-top: 15px;
    display: flex;
    justify-content: space-between;
}

/* ##### Awesome buttons */

button {
    cursor: pointer;
    font-size: 1.2rem;
    height: 2.5rem;
    border: none;
    border-radius: 10px;
    color: #fff;
    background: #333;
    outline: none;
    padding: 0.5rem 1.8rem;
    box-shadow: var(--quote-button-shadow);
}

button:hover {
    filter:brightness(130%);
}


button:active {
    transform: translate(0, 0.3rem);
    box-shadow: 0 0.1rem rgba(255, 255, 255, 0.65);
}

.twitter-button:hover {
    color: #38a1f3;
}
.fa-twitter {
    font-size: 1.5rem
}
/* #### Awesome buttons end */

/* loader */
.loader {
    position: absolute;
    border: 16px solid var(--quote-loader);
    border-top: 16px solid var(--quote-loader-alt);
    border-radius: 50%;
    width: 50px;
    height: 50px;
    animation: spin 1.5s linear infinite;
}

@keyframes spin {
    0% {transform: rotate(0def);}
    100% {transform: rotate(360deg);}
}


/* Media query: Tablet or phone */
@media screen and (max-width:1000px) {
    .quote-container {
        margin: auto 10px;
    }
    .quote-text {
        font-size: 2.5rem;
    }
}



</style>