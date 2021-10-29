<template>
    <div class="question-create">
        <h1 class="mb-3">Create a new Question</h1>
        <form class="question-form">
            <input type="text" class="title" placeholder="What you want to ask">
            <textarea class="form-controll content" rows="4" placeholder="Question detail"></textarea>
        </form>
    </div>
</template>

<script>
import {axios} from "../common/api.service.js";
export default {
    name: "Create-Question",
    title() {
        return "Forum: create new question"
    },
    data() {
        return {

        }
    },
    methods: {
        async createNewQuestion() {
            let endpoint = `/forum/api/questions/`
            try {
                let responce = await axios.post(endpoint);
                this.next = responce.data.next
                this.answers.push(...responce.data.results)
            } catch (err) {
                console.log(err)
            }
        }
    }
}
</script>

<style scoped>
.question-create {

}
</style>