<template>
    <section>
        <div class="question-detail">
            <div class="card" v-if="question">
                <div class="card-body">
                    <i class="fas fa-chevron-circle-left" @click="$router.back()"></i>
                    <h3>{{question.title}}</h3>
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

            <div class="not-found" v-else>
                <h1 class="error text-center">Error 404: Question Not found</h1>
                <img src="../assets/pulpFiction.gif" alt="gif-file">
                <button class="outline" @click="$router.back()">Back to previous page</button>
            </div>

            <div v-if="answers" class="container">
                <AnswerView v-for="answer in answers" 
                    :key="answer.uuid"
                    :answer="answer"/>
            </div>

        </div>
    </section>
</template>

<script>
import AnswerView from "../views/Answer.vue";
import {axios} from "../common/api.service.js";


export default {
    name: "Question-Detal",
    title() {
        return this.question? "Forum: question-detail" : "Forum: 404 page not found"
    }, 
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    components: {
        AnswerView 
    },
    data() {
        return {
            question: " ",
            answers: [],
            next: null,
            loadingAnswers: false,
        }
    },
    methods: {
        async getQuestionData() {
            const endpoint = `/forum/api/questions/${this.slug}/`;
            try {
                let responce = await axios.get(endpoint);
                this.question = responce.data
            } catch (err) {
                console.log(err)
                this.question = null
            }
        },
        async getQuestionAnswers() {
            const endpoint = `/forum/api/questions/${this.slug}/answers/`
            try {
                let responce = await axios.get(endpoint);
                this.next = responce.data.next
                this.answers.push(...responce.data.results)
            } catch (err) {
                console.log(err)
            }
        },
    },
    created() {
        this.getQuestionData()
        this.getQuestionAnswers()
    },
    watch: {
        question: function() {
             document.title = this.$options.title.call(this)
        }
    }
    
}
</script>

<style scoped>
.card-body div {
    display: flex;
    flex-wrap: wrap;
    position: relative;
}
.question-detail{
    margin:auto;
}
.content-info {
    display: flex;
}
.fas {
    font-size: 15px;
}
.card {
    opacity: 0.85;
    box-shadow: var(--forum-card-shadow);
    width: 80vw;
    margin: auto;
}
.outline {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='80' height='80' viewBox='0 0 80 80'%3E%3Cg fill='%239C92AC' fill-opacity='0.4'%3E%3Cpath fill-rule='evenodd' d='M0 0h40v40H0V0zm40 40h40v40H40V40zm0-40h2l-2 2V0zm0 4l4-4h2l-6 6V4zm0 4l8-8h2L40 10V8zm0 4L52 0h2L40 14v-2zm0 4L56 0h2L40 18v-2zm0 4L60 0h2L40 22v-2zm0 4L64 0h2L40 26v-2zm0 4L68 0h2L40 30v-2zm0 4L72 0h2L40 34v-2zm0 4L76 0h2L40 38v-2zm0 4L80 0v2L42 40h-2zm4 0L80 4v2L46 40h-2zm4 0L80 8v2L50 40h-2zm4 0l28-28v2L54 40h-2zm4 0l24-24v2L58 40h-2zm4 0l20-20v2L62 40h-2zm4 0l16-16v2L66 40h-2zm4 0l12-12v2L70 40h-2zm4 0l8-8v2l-6 6h-2zm4 0l4-4v2l-2 2h-2z'/%3E%3C/g%3E%3C/svg%3E");    background-size: 12px;
    color: var(--on-background-alt);
    font-weight: bold;
    background-size: 12px;
    margin: 10px  auto;
}
.not-found {
    display: flex;
    flex-direction: column;
}
.not-found img {
    border-radius: 10px;
    width: 50vw;
    height: 50vh;
    z-index: -1;
    margin: auto;
}
.fa-chevron-circle-left {
    position: absolute;
    top: 15px;
    left: 15px;
    font-size: 20px;
}
.fa-chevron-circle-left:hover {
    color: #dd715f;
    filter: brightness(1.2);
}
@media  screen and (max-width: 800px) {
    .not-found img {
        width: 95vw;
        height: unset;
    }
    .card {
        width: 95vw;
    }
}
</style>