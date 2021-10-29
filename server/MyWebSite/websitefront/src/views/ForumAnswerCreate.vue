<template>
    <transition appear name="animate_answer_create" 
        appear-active-class="animate__animated animate__fadeIn"
        leave-to-class="animate__animated animate__zoomOut">
    <div class="answer-form">
        <form class="answer-form">
            <i class="fas fa-times" @click="close" title="Close"></i>
            <textarea class="form-control" placeholder="Write your answer here" rows="10" v-model="newAnswerBody"></textarea>
            <div class="error-container-block" v-if="errors">
                <hr>
                <p class="mb-3">{{errors}}</p>
            </div>
            <div class="form-buttons">
                <button class="btn btn-primary" @click.prevent="sendAnswer">Submit</button>
                <button type="reset" class="btn btn-warning" @click="errors = null">Clear all</button>
            </div>
        </form>
    </div>
    </transition>
</template>


<script>
import {mapState} from "vuex";
import { axios } from "../common/api.service.js";
export default {
    name: "ForumAnswerCreate",
    title() {
        return "Forum: create answer"
    },
    emits: ["close-form", "answer-submited"],
    props: {
        slug: {
            type: String,
            required: true
        },
        lastAnswer: {
            type: Object,
            required:false
        }

    },
    data() {
        return {
            newAnswerBody: "",
            errors: null,
        }
    },
    computed: {
      ...mapState(["user",])
    },
    methods: {
        close() {
            this.$emit('close-form')
        },
        async sendAnswer() {
            if (this.newAnswerBody && this.lastAnswer && this.lastAnswer.author.split(' ').join('') === this.user && this.lastAnswer.is_active) {
                this.errors = "You can submit your answer after another user has answered this question."
                return
            }
            if (!this.newAnswerBody) {
                this.errors = "You can't send a empty answer!"
                return
            } else {
                if (this.errors) this.errors = null;
                let endpoint = `/forum/api/questions/${this.slug}/answer/`;
                try {
                    let responce = await axios.post(endpoint, { body: this.newAnswerBody });
                    this.$emit("answer-submited", responce.data)
                    this.close()
                } catch (err) {
                    console.log(err)
                    this.errors = err.message ? err.message : err
                }
            }
        }
    }
}
</script>

<style scoped>
.answer-form {
    position: relative;
    background: var(--forum-comment-background);
    overflow: hidden;
    border-radius: 25px;
}
.form-buttons {
    display: flex;
    justify-content: space-between;
}
.fa-times {
    position: absolute;
    font-size: 15px;
    right: 15px;
    top:15px;
}  
.form-control{
    height: 75px;
}
.btn {
    margin-right: unset;
}
.error-container-block{
    background: #fb363680;
}
hr {
    margin: unset;
}
@media screen and (max-width:800px) {
    .btn {
        margin: unset;
        flex-grow: 1;
        border-radius: unset;
    }
    .answer-form {
        max-width: 95vw
    }
}
</style>