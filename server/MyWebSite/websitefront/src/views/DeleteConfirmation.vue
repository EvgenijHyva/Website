<template>
    <section>
        <div class="message">
            <h2> Are you sure you want delete your answer? </h2>
            <div>
                <button class="outline secondary" @click="deleteAnswer(answer)">Yes</button>
                <button class="outline secondary" @click="close">No</button>
            </div>
        </div>
    </section>
</template>

<script>
import {axios} from "../common/api.service.js";

export default {
    name: "Delete Confirm",
    emits: ["close-confirmation-module", "deleted-modul"],
    props:{ 
        answer: {
            type: Object,
            required: true
        }
    },
    methods: {
        async deleteAnswer(answer) {
            const endpoint = `/forum/api/answers/${answer.uuid}/`
            let message = ""
            try {
                let responce = await axios.delete(endpoint);
                answer.is_active = false
                if (responce.status === 204)
                    message = "Deleted succefully"
            } catch (err) {
                console.log(err)
                message = "Error occured"
            }
            this.$emit("deleted-modul", message)
            this.close()
        },
        close () {
            this.$emit("close-confirmation-module")
        }
    }
}
</script>

<style scoped>
section {
    position: fixed;
    background: #000000bf;
    width: 100vw;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
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