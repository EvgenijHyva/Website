<template>
    <section>

        <sidebar />

        <div class="question-create container">
            <h2 class="mb-3">Create a new question</h2>
            <form class="question-form">
                <input type="text" class="title mb-2" placeholder="What you want to ask?" v-model="questionTitle">
                <textarea class="form-controll content mb-2" v-model="questionBody"
                    rows="4" placeholder="Question details"></textarea>
                <p class="error mb-2" v-if="errors">{{ errors }}</p>
                <div class="form-buttons">
                    <button class="btn btn-primary" @click.prevent="sendQuestion">Submit</button>
                    <button type="reset" class="btn btn-warning" @click="errors = null">Clear all</button>
                </div>
            </form>
        </div>
    </section>
</template>

<script>
import { mapState } from "vuex";
import {axios} from "../common/api.service.js";

import Sidebar from "../views/SideBar.vue";

export default {
    name: "Create-Question",
    title() {
        return "Forum: question editor"
    },
    components: {
        Sidebar
    },
    props: {
        slug: {
            type: String,
            required: false
        }
    },
    computed: {
      ...mapState(["authModalShow",])
    },
    data() {
        return {
            questionTitle: null,
            questionBody: "",
            errors: null,
        }
    },
    methods: {
        async createOrUpdateNewQuestion() {
            let endpoint = `/forum/api/questions/`;
            let method = "POST";
            if(this.slug) {
                endpoint += `${this.slug}/`;
                method = "PUT";
            }
            try {
                let responce = await axios({
                    method: method,
                    url:endpoint,
                    data: { 
                        title: this.questionTitle, 
                        content: this.questionBody
                    }
                });
                if(responce.status === 201 || responce.status === 200) {
                    this.$router.push({name: "Forum-question-detail", params: {slug: responce.data.slug}})
                }
            } catch (err) {
                console.log(err)
            }
        },
        sendQuestion() {
            if (!this.questionTitle) {
                this.errors = "You can't send an empty question!"
                return
            } else if (this.questionTitle.length > 50) {
                this.errors = "Max title length is 50 characters. You can write addition information in question detail area."
            } else {
                if(this.errors) this.errors = null
                this.createOrUpdateNewQuestion()
            }
        },
    },
    async beforeRouteEnter(to, from, next) {
        if (to.params.slug && to.params.slug) {
            const endpoint = `/forum/api/questions/${to.params.slug}/`
            try {
                const responce = await axios.get(endpoint)
                return next(vm => {
                    vm.questionTitle = responce.data.title
                    vm.questionBody = responce.data.content
                })
            } catch (error) {
                console.log(error)
            }
        } else 
            return next();
    },   
    watch: {
        authModalShow: function() {
            if(this.authModalShow == true)
            this.$router.push("/auth/login/")
        }
    }
}
</script>

<style scoped>
input, textarea, .error{
    padding: 5px;
    border-radius: 20px;
}

.question-create,form {
    display: flex;
    flex-direction: column;
}
.question-create h2 {
    font-family: Comfortaa;
    color: var(--forum-h2); 
}
.question-create {
    background:  var(--forum-background); 
    padding: 15px 10px;
    border-radius: 10px;
    overflow: hidden ;
}
.form-buttons {
    display: flex;
    justify-content: space-between;
}
.form-buttons *{
    margin-right: unset;
}
.error{
    color: var(--forum-h2);
    background: #fb363680;
    font-size: 20px;
    font-weight: bold;
    font-family: Comfortaa;
    letter-spacing: 0.1rem;
}
@media screen and (max-width:800px) {
    .form-buttons {
        overflow: hidden;
        border-radius:  10px 10px;
    }
    .btn {
        margin: unset;
        flex-grow: 1;
        border-radius: unset;
    }
    .question-create {
        max-width: 97vw
    }
}

</style>