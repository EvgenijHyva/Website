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

