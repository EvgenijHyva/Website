<template>
    <section>
        <transition appear 
            appear-active-class="animate__animated animate__fadeIn"
            leave-active-class="animate__animated animate__fadeOut">
            <div class="message">
                <h2> Are you sure you want delete your {{ answer ? 'answer' : 'question' }}? </h2>
                <div>
                    <button class="outline secondary" @click=" answer ? deleteAnswer(answer) : deleteQuestion(question) ">Yes</button>
                    <button class="outline secondary" @click="close">No</button>
                </div>
            </div>
        </transition>
    </section>
</template>

<script>
import {axios} from "../common/api.service.js";

export default {
    name: "Delete Confirm",
    emits: ["close-confirmation-module", "deleted-modul", "deleted-question"],
    props:{ 
        answer: {
            type: Object,
            required: false
        },
        question: {
            type:Object,
            required: false
        }
    },
    methods: {
        async deleteAnswer(answer) {
            const endpoint = `/forum/api/answers/${answer.uuid}/`
            let message = ""
            try {
                let responce = await axios.delete(endpoint);
                if (responce.status === 204) {
                    answer.is_active = false
                    message = "Deleted succefully"
                }
            } catch (err) {
                console.log(err)
                message = "Error occured"
            }
            this.$emit("deleted-modul", message)
            this.close()
        },
        async deleteQuestion(question) {
            const endpoint = `/forum/api/questions/${question.slug}/`
            try {
                let responce = await axios.delete(endpoint);
                if (responce.status === 204) {
                    this.$emit("deleted-question", question)
                } else {
                    alert("Error occured")
                }
            } catch (err) {
                console.log(err)
            }
            this.close()
        },
        close () {
            this.$emit("close-confirmation-module")
        }
    }
}
</script>

<style scoped>
.animate__animated {
    animation-duration: 1.5s;
}
section {
    font-family: Lora;
    position: fixed;
    background: #000000bf;
    width: 100vw;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    z-index: 5;
}
.message h2 {
   color: white;
}
@media screen and (max-width: 800px) {
    .message h2 {
        font-size: 20px;
    }
    
}

</style>