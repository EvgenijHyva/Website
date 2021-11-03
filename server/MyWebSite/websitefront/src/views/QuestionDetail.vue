<template>
    <section>
        <admin-answer-panel v-if="is_staff" 
            @toggle-deleted="toggleDeleted" 
            :hidenMessages="inactiveMessages" />
        <div>

        <div class="wrapper overflow" ref="wrapper">
            <div class="question-detail">

                <div class="card" v-if="question">
                    <div class="card-body">
                        <i class="fas fa-chevron-circle-left" @click="$router.push({name:'Forum'})" 
                            title="Return to previous"></i>
                        <i class="fas fa-plus-circle" title="Add a new answer" 
                            @click="addNewAnswer = true"></i>
                        <h3>{{question.title}}</h3>
                        <p class="mb-0 card-text" v-if="question.content">
                            <span>{{question.content}}</span></p>
                        <div class="content-info">
                            <div>
                            <p class="mb-0">
                            Posted by: <strong>{{question.author}}</strong> 
                            <i class="fas fa-user-tie" title="Admin user"
                                v-if="question.author_is_admin" ></i>
                            <i class="fas fa-user" v-else 
                                :title="'User: ' + question.author">
                            </i>&nbsp;|
                            </p>
                            <p class="mb-0"  :title="'Users have answered to this question ' + question.answers_count + ' times' "> 
                            &nbsp;Answers: 
                                <strong>{{question.answers_count}}</strong>
                            </p>&nbsp;|
                            <p>&nbsp;
                                <router-link :to="{'name': 'Forum-question-create-edit', params: {'slug': question.slug} }" tag="i"
                                    v-if="question.author && question.author.split(' ').join('') == user && !question.answers_count">
                                    <i class="fas fa-pencil-alt" title="Edit question"></i>&nbsp;
                                </router-link>
                                <i class="far fa-trash-alt" title="Delete question"
                                    v-if="question.author && question.author.split(' ').join('') == user"
                                    @click="showQuestionConfirmDelete = true"></i>&nbsp;
                            </p>
                            </div>
                            <p class="answer-added info-text" v-if="question.user_has_answered">You have already answered that question</p>
                            <p class="add-answer info-text" v-else @click="addNewAnswer = true">Add a new answer!</p>                           
                        </div>

                        <i class="fas fa-angle-up" title="Hide answers"
                            v-show="addNewAnswer" 
                            v-if="showAnswers && addNewAnswer && answers.length" 
                            @click="toggleAnswerContainer"></i>
                        <i class="fas fa-angle-down"  title="Show answers"
                            v-show="addNewAnswer" 
                            v-else-if="!showAnswers && addNewAnswer" 
                            @click="toggleAnswerContainer"></i>

                        <question-delete-confirmation 
                            :question="question" 
                            v-if="showQuestionConfirmDelete" 
                            @close-confirmation-module="showQuestionConfirmDelete = false;"
                            @deleted-question="confirmedQuestionDelete"/>

                    </div>
                </div>

                <div class="not-found" v-else>
                    <h1 class="error text-center">Error 404: Question Not found</h1>
                    <img src="../assets/pulpFiction.gif" alt="gif-file">
                    <button class="outline" @click="$router.back()">Back to previous page</button>
                </div>

                <div v-if="answers" class="container">
                    <answer-create-view 
                        v-if="addNewAnswer" 
                        @close-form="addNewAnswer = false" 
                        @answer-submited="newPost"
                        :slug="slug"
                        :lastAnswer="answers[0]"/>
                        
                    <answer-view v-for="answer in answers" 
                        v-show="showAnswers"
                        :key="answer.uuid"
                        :answer="answer"
                        :isLastAnswer="answers.indexOf(answer) === 0"
                        :stateShowDeleted="showDeletedMessages"
                        @confirmed-deleted-answer="confirmedDeletedAnswer"/>
                    
                </div>    

            </div>
        </div>

        <button class="load-more-button secondary" v-show="next" 
            @click.prevent="getQuestionAnswers(next)"  
            title="Load more answers">Load older answers</button>
        </div>

    </section>
</template>

<script>
import AdminAnswerPanel from "../views/AdminFeatures/ForumAdminAnswerTools.vue";
import AnswerCreateView from "../views/ForumAnswerCreate.vue";
import AnswerView from "../views/Answer.vue";
import QuestionDeleteConfirmation from "../views/DeleteConfirmation.vue";
import {axios} from "../common/api.service.js";
import {mapState} from "vuex";


export default {
    name: "QuestionDetail",
    title() {
        return this.question? "Forum: question-detail" : "Forum: 404 page not found"
    }, 
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    computed: {
        ...mapState(["is_staff", "user", "authModalShow"])   
    },
    components: {
        AnswerView, AnswerCreateView, QuestionDeleteConfirmation, AdminAnswerPanel
    },
    data() {
        return {
            question: " ",
            answers: [],
            next: null,
            loadingAnswers: false,
            showAnswers: true,
            addNewAnswer: false,
            showDeletedMessages: false,
            inactiveMessages: false,
            showQuestionConfirmDelete: false,
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
        async getQuestionAnswers(endpoint) {
            endpoint ? endpoint : endpoint = `/forum/api/questions/${this.slug}/answers/` 
            try {
                let responce = await axios.get(endpoint);
                this.next = responce.data.next
                this.answers.push(...responce.data.results)
            } catch (err) {
                console.log(err)
            }
        },
        toggleAnswerContainer() {
            this.showAnswers = !this.showAnswers
        },
        newPost(responce) {
            this.answers.unshift(responce)
            if (!this.question.answers_count){
                return this.question.answers_count++
            } 
        },
        toggleDeleted(state) {
            this.showDeletedMessages = state
        },
        confirmedQuestionDelete(question) {
            console.log( `${question.title} deleted`)
            this.$router.push({"name": "Forum"})
        },
        confirmedDeletedAnswer() {
            if (!this.question.answers_count)
                return this.question.answers_count = 0
            else 
                return this.question.answers_count --
        }
    },
    created() {
        this.getQuestionData()
        this.getQuestionAnswers()
    },
    watch: {
        question: function() {
            document.title = this.$options.title.call(this)
            if(document.title === "Forum: 404 page not found") {
                this.$refs["wrapper"].classList.contains("overflow") ? this.$refs["wrapper"].classList.remove("overflow") : ""
            } else {
                this.$refs["wrapper"].classList.contains("overflow") ? "" : this.$refs["wrapper"].classList.add("overflow")
            }
            if (this.question) {
                // Capitalize question content
                this.question.title = this.question.title[0].toUpperCase() + this.question.title.slice(1)
                if (this.question.content)
                    this.question.content = this.question.content[0].toUpperCase() + this.question.content.slice(1)
            }     
        },
        "answers.length": function (){
            this.answers.forEach(answer => {
                //capitalize answer body
                answer.body = answer.body[0].toUpperCase() + answer.body.slice(1)
            });
            
            let initialCheck = true
            let activeAnswers = this.answers.reduce((total, answer) => (answer.is_active === false? total: total+1), 0) 
            this.inactiveMessages = this.answers.length === activeAnswers? false : true  
            if (initialCheck && activeAnswers < 10 &&  this.next) {  
                //load automaticly answers for admin if there is hiden answers
                this.getQuestionAnswers(this.next)
            } else {
                initialCheck = false;
            }
        },
        addNewAnswer: function() {
            document.title = this.$options.title.call(this)
            if(!this.addNewAnswer)
                return this.showAnswers = true
        },
        authModalShow: function() {
            if(this.authModalShow == true)
            this.$router.back()
        },     
    },
}
</script>

<style scoped>

.wrapper {
    margin: 80px auto 0;
    max-height: 80vh;
}

.overflow {
    overflow-y: scroll;
}.card-body {
    font-family: Texturina;
}
.card-body div {
    display: flex;
    flex-wrap: wrap;
    position: relative;
    box-sizing: border-box;
}
.question-detail { 
    margin-right: 10px ;
    max-width: 1100px;
    padding:  2px 0 3px 1px;
}

.content-info {
    display: flex;
    justify-content: space-between;
}
.content-info div{
    flex-grow: 1;
}
a {
    border-bottom: unset;
}
.info-text {
    font-size: 15px;
    text-align: right;
    padding: 1px 5px;
}
.answer-added {
    color: green;  
}
.add-answer{
    color: orange;
    flex-grow: 1;
}
.fas {
    font-size: 15px;
}
.fa-pencil-alt {
    color: #040404ba;
}
.fa-chevron-circle-left {
    position: absolute;
    top: 15px;
    left: 15px;
    font-size: 20px;
}
.fa-plus-circle {
    position: absolute;
    top: 15px;
    right: 15px;
    font-size: 20px;
}
.fa-plus-circle:hover, 
.fa-pencil-alt:hover {
    color: #356a0c;
    filter: brightness(1.2);
}
.fa-plus-circle:active,
.fa-pencil-alt:active,
.fa-trash-alt:active  {
    color: #0b59a9;
    filter: brightness(1.2);
}
.fa-chevron-circle-left:hover {
    color: #dd715f;
    filter: brightness(1.2);
}
.fa-angle-up, .fa-angle-down {
    position: absolute;
    font-size: 20px;
    bottom: 0;
    left: 0;
    right: 0;
}

.fa-trash-alt:hover {
    color: #fc2600;
    filter: brightness(1.2);
}

.card {
    opacity: 0.85;
    box-shadow: var(--forum-card-shadow);
    width: 80vw;
    margin: auto;
    max-width: 1100px;
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

.load-more-button {
    margin: auto;
}
@media  screen and (max-width: 1000px) {
    .not-found h1 {
        font-size: 30px;
    }
}
@media  screen and (max-width: 800px) {
    .not-found img {
        width: 95vw;
        height: unset;
    }
    .card {
        width: 95vw;
    }
    .card-body div {
        align-self: center;
    }
    .info-text  {
        margin: auto;
    }
    .content-info{
        flex-direction: column;
    }
    .wrapper {
        max-height: 75vh;
    }
    .question-detail {
        margin-right: 5px;
    }
    .not-found h1 {
        font-size: 30px;
    }
    .fa-plus-circle {
        right: 0;
    }
    .fa-chevron-circle-left {
        left: 1px;
    }
    .fa-plus-circle, .fa-chevron-circle-left {
        top:3px;
    }
}


</style>