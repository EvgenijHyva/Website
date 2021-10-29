<template>
    <section>
        <div class="error">
            <p v-show="error !== null">{{error}}</p>
        </div>
        <div class="loader" id="loader" v-if="loading" >
            <img src="../assets/Ripple-1s-200px.svg" alt="loading">
            <span class="loading-text"> I'm load, please wait </span>
        </div> 
        <div class="container" v-else>
            <div class="wrapper">
                <div v-for="question in questions" :key="question.slug" >
                    <div class="card mb-2 bg-body rounded">
                        <div class="card-body">
                            <router-link :to="{'name': 'Forum-question-detail', params: { 'slug': question.slug} }" :title="'question: ' + question.slug">
                                <h5 class="card-title">{{question.title}} </h5>
                            </router-link>
                            <p class="mb-0 card-text" v-if="question.content"><span>{{question.content}}</span></p>
                            <div class="content-info">
                                <p class="mb-0">
                                    Posted by: <strong>{{question.author}}</strong> 
                                    <i class="fas fa-user-tie" v-if="question.author_is_admin" title="Admin user"></i>
                                    <i class="fas fa-user" v-else 
                                        :title="'User: ' + question.author">
                                    </i>&nbsp;|
                                </p>
                                <p class="mb-0"  :title="'Users have answered to this question ' + question.answers_count + ' times' "> 
                                    &nbsp;Answers: 
                                    <strong>{{question.answers_count}}</strong>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="pagination"> 
                <button class="secondary outline" :class="{'shadow-btn': next}"
                    :title=" next ? 'Load older questions page': 'You are viewing the last page'"
                    :disabled="next===null" 
                    @click.prevent="getQuestions(next)">
                    Next page
                </button>
                <button class="secondary outline" :class="{'shadow-btn': previous}"
                    :title=" previous ? 'Load newest questions page': 'You are viewing the first page'"
                    :disabled="previous===null" 
                    @click.prevent="getQuestions(previous)">
                    Previous page
                </button>
            </div>
        </div>
    </section>
</template>

<script>
import { mapState } from "vuex";
import { axios } from "@/common/api.service.js";


export default {
    name: "Forum",
    data() {
        return {
            questions: [],
            next: null,
            previous: null,
            error: null,
            loading: false, 
            LoadFail: false,
        }
    },
    computed: {
      ...mapState(["key",])
    },
    methods: {
        async getQuestions(endpoint) {
            endpoint ? endpoint : endpoint = "api/questions/"
            this.loading = true
            this.previousPageSetter(endpoint)
            try {
                const response = await axios.get(endpoint)
                this.questions = response.data.results;
                if (!this.questions && !this.LoadFail) {
                    this.previousPageDeleter()
                }
                this.next = response.data.next;
                this.previous = response.data.previous;
                if (this.error) 
                    this.error = null;
                this.loading = false
            } catch(err){
                if (!this.LoadFail) {
                    this.previousPageDeleter();
                }
                this.error = "Error occured: " + err.response.status ? err.response.status : "" + " " + err.response.statusText ? err.response.statusText : "";
            }
        },
        previousPageSetter(page) {
            localStorage.setItem("ForumPage", page )
        },
        previousPageGetter() {
            let page = localStorage.getItem("ForumPage")
            if (page) {
                return page
            } else {
                return null
            }
        },
        previousPageDeleter() {
            localStorage.removeItem("ForumPage")
            this.getQuestions();
            this.LoadFail = !this.LoadFail
        }

    },
    async created() {
        let page = this.previousPageGetter()
        await this.getQuestions(page)
    },
    watch: {
        key: async function() {
            this.getQuestions()
        },
    }
}

</script>

<style scoped>
a:hover h5, a:focus h5{
    color: var(--primary-variant);
}
a:visited h5 {
    color: black;
}
a:active h5 {
    color: green;
}

.error{
    position: fixed;
    top: 30vh;
    color: var(--on-background-alt);
    font-size: 20px;
    font-weight: bold;
    font-family: "Kaushan Script", Lobster;
    letter-spacing: 0.1rem;
}
.container {
    margin-top: 80px;
    background:  var(--forum-background); 
    padding: 15px 10px;
    border-radius: 10px;
}
.container .wrapper {
    overflow: hidden ;
    overflow-y: scroll;
}
.wrapper *, ::after {
    margin-right: 5px;
}
.shadow-btn{
    box-shadow: var(--forum-button-shadow);
}
.shadow-btn:active {
    transform: translate(0, 0.3rem);
    box-shadow: 0 0.1rem rgb(255 255 255 / 65%);
}
.pagination {
    justify-content: space-between;
}
.card {
    opacity: 0.85;
    box-shadow: var(--forum-card-shadow);
}
.card-body {
    text-align: left;
}
.card-title {
    margin-bottom: 0;
}
.content-info {
    display: flex;
}

.fas {
    font-size: 15px;
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
    opacity: 1;
}
.loading-text {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: var(--on-background);
    font-family: Lobster;
    letter-spacing: 0.1rem;
}


</style>