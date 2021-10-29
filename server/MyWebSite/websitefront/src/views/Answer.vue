<template>
    <div>
        <transition appear name="Animate_answer" appear-active-class="animate__animated animate__zoomIn">
            <div class="text-muted" v-if="answer.is_active || stateShowDeleted"
                :class="{'deleted hidden-box' : !answer.is_active}" 
                :title="!answer.is_active ? 'Answer was deleted': 'Author: ' + answer.author">
                <div>
                    <div class="answer-body" > <div v-if="!answer.is_active">Deleted:&nbsp;</div>{{answer.body}}</div> 
                    <div class="tools">
                        <i class="fas fa-pencil-alt" v-if="answer.author.split(' ').join('') === user && answer.is_active"></i>&nbsp; 
                        <i class="fas fa-trash-alt" @click="deleteAnswer(answer)" v-show="answer.author.split(' ').join('') === user && answer.is_active"></i>&nbsp;
                        <i class="fas fa-thumbs-up" v-if="answer.user_has_liked_answer">&nbsp;{{answer.likes_count}}</i>
                        <i class="far fa-thumbs-up" v-else>&nbsp;{{answer.likes_count}}</i>
                    </div>
                        <i class="fas fa-angle-down" 
                            v-show="!answer.is_active" 
                            v-if="!showDeletedInfo" 
                            @click="toggleDeletedAnswer"
                            key="down"></i> 
                    <i class="fas fa-angle-up"  v-else @click="toggleDeletedAnswer" key="up"></i>
                </div>
                    <hr>    
                <div>
                    <strong> <p>{{answer.author}}</p></strong>
                    <p class="date"> {{answer.created_at}} </p>
                </div>  
                <delete-confirm 
                    v-if="showDeleteAnswer" 
                    @close-confirmation-module="
                        showDeleteAnswer=false; 
                        answerToDelete=null"
                    @deleted-modul="showMessage"
                    :answer="answerToDelete" />   
            </div>
        </transition>
    <transition tag="div" mode="out-in" 
        enter-active-class="animate__animated animate__zoomIn"
        leave-to-class="animate__animated animate__zoomOut">
        <div class="delete-confirmed" v-if="deleteInfo">
            <h2>{{message}}</h2>
        </div>
    </transition>
    </div>
</template>

<script>
import DeleteConfirm from "../views/DeleteConfirmation.vue";

import {mapState} from "vuex";

export default {
    name: "Answer",
    components: {
        DeleteConfirm
    },
    props: {
        answer: {
            type:Object,
            required: true
        },
        stateShowDeleted: {
            type:Boolean,
            required: false
        }
    },
    computed: {
      ...mapState(["user",])
    },
    data() {
        return {
            showDeleteAnswer: false,
            answerToDelete: null,
            deleteInfo: false,
            message: "",
            showDeletedInfo: false,
        }
    },
    methods: {
        deleteAnswer(answerObject) {
            this.answerToDelete = answerObject
            this.showDeleteAnswer = true
        },
        showMessage(message) {
            this.message = message
            this.deleteInfo = true
        },
        toggleDeletedAnswer(event) {
            let mainContainer = event.currentTarget.parentElement.parentElement;
            if (!this.showDeletedInfo) {
                mainContainer.classList.remove("hidden-box")
            } else {
                mainContainer.classList.add("hidden-box")

            }
            this.showDeletedInfo = !this.showDeletedInfo
        }
    },
    watch: {
        deleteInfo: function () {
            // For info message disappear from page
            if (this.deleteInfo) {
                setTimeout(() => {
                this.deleteInfo = false; 
            }, 3000)
            }
        }   
    }
}
</script>

<style scoped>
.animate__animated{
    animation-duration: 1.5s;
}
.deleted {
    background: #ff0047c9 !important; 
    overflow: hidden;
    position: relative;
    transition: 1s;
}
.hidden-box {
    height: 0;
    border-radius: 50px !important;
}

.hidden-box *, .hidden-box .answer-body div {
    color: transparent;
}

.text-muted {
    box-shadow: var(--forum-card-shadow);
    background: var(--forum-comment-background);
    border-radius: 5px 10px 15px 20px;
    padding: 10px;
}
.fa-thumbs-up, .fa-trash-alt, .fa-pencil-alt{
    font-size: 15px;
}
.fa-trash-alt:hover {
    color: red;
}
.fa-pencil-alt:hover {
    color: black;
}
.fas+.fa-thumbs-up:hover {
    color:rgb(240, 87, 60);
}
.fa-thumbs-up:hover {
    color: darkgreen;
}
.fa-angle-up, .fa-angle-down {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    color: #f5f502;
    opacity: 0.7;
    font-size: 20px;
}
.text-muted div {
   display: flex;
   justify-content: space-between;
}
.answer-body div {
    color: rgb(186, 186, 41);
    opacity: 0.5; 
    margin: 0;
}
.answer-body {
    white-space: pre-wrap;
    text-align: left;
    max-width: 75%;
}
.date {
    font-weight: 100;
}
.tools {
    text-align: right; 
    padding : 5px;
    align-items: center;
}
.delete-confirmed {
    background: #253c50b8;
    padding: 3px 16px;
    border-radius: 10px;
    box-shadow: 5px 6px 11px 0 rgb(0 0 0 / 50%);
    transition: 0.3s;
    position: fixed;
    bottom: 25px;
    left: 50px;
    font-family: 'Markazi Text', sans-serif;
}
.delete-confirmed h2 {
    margin: auto;
    color: var(--forum-delete-info);
}
hr {
    margin: 1px 0;
    opacity: .5;
}
@media screen and (max-width: 800px){
    .delete-confirmed {
        left: unset;
        top: 20px;
        bottom:unset;
    }
    .tools {
        height: 5vh;
        display: contents;
    }
}

</style>
