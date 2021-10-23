<template>
    <section>
        <side-bar />
        <div class="loader" id="loader" v-if="loading">
                <img src="../assets/Ripple-1s-200px.svg" alt="loading">
                <span class="loading-text"> I'm load, please wait </span>
        </div> 
        <div class="container" v-else>
            <div class="wrapper">
                <div v-for="question in questions" :key="question.slug" >
                    <div class="card mb-2 bg-body rounded">
                        <div class="card-body">
                            <h5 class="card-title">{{question.title}}</h5>
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
            <question-detail />
        </div>
    </section>
</template>

<script>
import {axios} from "@/common/api.service.js";
import SideBar from "../views/SideBar.vue";
import QuestionDetail from "../views/QuestionDetail.vue";
//import QuestionCreate from "@views/QuestionCreate.vue";

export default {
    name: "Forum",
    title()  {
        return "Forum"
    },
    components: {
        SideBar, QuestionDetail, //QuestionCreate
    },
    data() {
        return {
            questions: [],
            next: null,
            previous: null,
            error: null,
            loading: false, 
        }
    },
    methods: {
        async getQuestions(endpoint) {
            endpoint ? endpoint : endpoint = "api/questions/"
            this.loading = true
            try {
                const response = await axios.get(endpoint)
                this.questions = response.data.results;
                this.next = response.data.next;
                this.previous = response.data.previous;
                if (this.error) 
                    this.error = null;
                this.loading = false
            } catch(err){
                this.error = "Error " + err.response.status + " " + err.response.statusText;
                console.log(err.response)
                console.log(this.error)
            }
        }
    },
    async created() {
        await this.getQuestions()
    }
}

</script>

<style scoped>
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
    margin-right: 5px ;
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
}


</style>