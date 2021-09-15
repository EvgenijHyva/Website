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

import { apiService } from "../common/api.service";
const pageContentEndpoint = "/api/page_content/";

export default {
    name: "Mainpage",
    title() {
      return "Main page"
    },
    components: {
        Home, About, Projects, Contacts,
    }, 
    methods: {
        getPageContent() {
            apiService(pageContentEndpoint)
            .then(content => this.pageContent = content)
        }
    }, 
    data() {
        return {
            pageContent: null,
        }
    }, 
    created: function() {
        this.getPageContent()
    },
    beforeUnmount: function () {
        console.log("unmount MainPage")
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
@media screen and (max-width: 600px) {
    footer .text {
        margin: 3vh;
        padding: 3vw;
    }
}
</style>