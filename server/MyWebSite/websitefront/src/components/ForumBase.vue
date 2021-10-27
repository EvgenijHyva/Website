<template>
    <div class="forum-container-blok">
        <side-bar />
        <forum />
    </div>
</template>

<script>
import Forum from  "../components/Forum.vue"
import SideBar from "../views/SideBar.vue";
//import QuestionCreate from "@views/QuestionCreate.vue";
import { mapState } from "vuex";


export default {
    name: "ForumBase",
    components: {
        SideBar, Forum //QuestionCreate
    },
    computed: {
      ...mapState(["authModalShow",])
    },
    title()  {
        return "Forum"
    },
    data() {
        return {

        }
    },
    created() {
        if(this.authModalShow == true) {
            this.$router.push("/auth/login/")
        }
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

</style>