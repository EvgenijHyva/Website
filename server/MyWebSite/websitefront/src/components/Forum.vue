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

                <transition-group mode="out-in" name="aniamate_questions" appear
                        appear-active-class="animate__animated animate__fadeIn"
                        leave-active-class="animate__animated animate__backOutDown">
                    <div v-for="question in questions" :key="question.slug" >
                        <div class="card mb-2 bg-body rounded">
                            <div class="card-body">

                                <div class="header-block">
                                    <router-link :to="{'name': 'Forum-question-detail', params: { 'slug': question.slug} }" :title="'question: ' + question.slug">
                                        <h5 class="card-title">{{question.title}} </h5>
                                    </router-link>

                                    <div class="question-editor">
                                        <router-link :to="{'name': 'Forum-question-create-edit', params: {'slug': question.slug} }" tag="i" 
                                            v-if="question.author.split(' ').join('') == user && !question.answers_count">
                                            <i class="fas fa-pen-alt" title="Edit question"></i>
                                        </router-link>
                                        <i class="fas fa-times" title="Delete question"
                                            @click="deleteQuestion(question)" 
                                            v-if="question.author.split(' ').join('') == user"></i>
                                    </div>  
                                </div>

                                <p class="mb-1 card-text" v-if="question.content"><span>{{question.content}}</span></p>
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
                </transition-group>

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

            <question-delete-confirmation 
                :question="questionToDelete" 
                v-if="showConfirmDelete"
                @close-confirmation-module="showConfirmDelete = false; questionToDelete = null"
                @deleted-question="confirmedDelete" />
        </div>
    </section>
</template>

<script>
import { mapState } from "vuex";
import { axios } from "@/common/api.service.js";
import QuestionDeleteConfirmation from "../views/DeleteConfirmation.vue";

export default {
    name: "Forum",
    components: {
        QuestionDeleteConfirmation
    },
    data() {
        return {
            questions: [],
            next: null,
            previous: null,
            error: null,
            loading: false, 
            loadFail: false,
            questionToDelete: null,
            showConfirmDelete: false,
        }
    },
    computed: {
      ...mapState(["key", "user"])
    },
    methods: {
        async getQuestions(endpoint) {
            endpoint ? endpoint : endpoint = "api/questions/"
            this.loading = true
            this.previousPageSetter(endpoint)
            try {
                const response = await axios.get(endpoint)
                this.questions = response.data.results;
                if (!this.questions && !this.loadFail) {
                    this.previousPageDeleter()
                }
                this.next = response.data.next;
                this.previous = response.data.previous;
                if (this.error) 
                    this.error = null;
                this.loading = false
            } catch(err){
                if (!this.loadFail) {
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
        },
        deleteQuestion(question){
            this.questionToDelete = question
            this.showConfirmDelete = true;
        },
        confirmedDelete(question) {
            let index = this.questions.indexOf(question)
            this.questions.splice(index, 1)
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
        questions: function () {
            return this.questions.forEach(question => {
                question.title = question.title[0].toUpperCase() + question.title.slice(1)
                if (question.content)
                    question.content = question.content[0].toUpperCase() + question.content.slice(1)
            });
        }
    }
}

</script>

<style scoped>
.animate__animated {
    animation-duration: 1.3s;
}
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
    margin-top: 100px;
    background:  var(--forum-background); 
    padding: 15px 10px;
    border-radius: 10px;
}
.container .wrapper {
    max-height: 80vh;
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
.card-body .header-block {
    display: flex;
    justify-content: space-between;
    margin: unset;
}

.card-title {
    margin-bottom: 0;
}
.content-info {
    display: flex;
}
.header-block .question-editor i {
    border-bottom: unset;
    margin: unset;
    color: #040404ba;
}
.header-block i:hover {
    color: rgb(26, 201, 26);
}
.fas {
    font-size: 15px;
}
.header-block .question-editor {
    position: absolute;
    top: 2px;
    right: 2px;
}
.fa-times {
    font-size: 20px;
}
.fa-times:hover {
    color: red !important;
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
@media screen and (max-width:800px) {
    .container {
        margin-top: unset;
    }
    .wrapper {
        max-height: 75vh !important;
    }
}

</style>