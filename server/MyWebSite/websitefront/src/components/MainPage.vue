<template>
    <div>
        <home :content="this.pageContent" />
        <about :content="this.pageContent" />
        <projects />
        <contacts v-if="!this.$store.state.authModalShow" />
    </div>
</template>

<script>
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Projects from "../views/Projects.vue";
import Contacts from "../views/Contacts.vue";

import { axios } from "../common/api.service";

export default {
    name: "Mainpage",
    title() {
      return "Mainpage"
    },
    components: {
        Home, About, Projects, Contacts,
    }, 
    methods: {
        async getPageContent() {
            const endpoint = "/api/page_content/"
            try {
                let response = await axios.get(endpoint)
                if (response.status === 200) {
                    this.pageContent = response.data
                    this.$store.state.meta_choices = response.data.meta_choices
                }
            } catch (error) {
                console.log(error)   
            }
        }
    }, 
    data() {
        return {
            pageContent: null,
        }
    }, 
    created: async function() {
        await this.getPageContent()
    }
}
</script>

<style>
footer {
    padding: 3vh;
    background: linear-gradient(360deg, #0000007a, transparent);
}
footer .text {
    text-align: center;
    color: var(--title-alt);
}
.fa-calendar-week, .fa-calendar-day {
    font-size: 20px;
    margin-right: 3px;
}
@media screen and (max-width: 800px) {
    footer .text {
        margin: 3vh;
        padding: 3vw;
    }
}
</style>