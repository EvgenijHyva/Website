<template>
    <div class="side-bar">
        <router-link :to="{'name': 'Forum-question-create-edit'}" tag="i" v-if="!$router.currentRoute.value.path.match(/^\/forum\/ask\//)">
            <i class="fas fa-plus-circle" title="Add new question"></i>
        </router-link>
        <i class="fas fa-chevron-circle-left" @click="$router.back()" v-else title="Return to previous"></i>
    </div>
</template>

<script>
export default {
    name: "side-bar"
}
</script>

<style scoped>
a {
    border: unset;
}
.side-bar {
    display: flex;
    flex-direction: column;
    position: fixed;
    left: 0;
    top: 50%;
    background: var(--forum-background);
    padding: 10px 5px;
    border-top-right-radius: 15px;
    border-bottom-right-radius: 15px;
}
.side-bar i {
    color: white;
    padding: 2px 0;
}
.side-bar i:hover {
    color: green;
}


@media  screen and (max-width: 800px) {
    .side-bar{
        flex-direction: row;
        bottom: 0;
        top: unset;
        padding: 10px;
        border-top-left-radius: 15px;
        border-bottom-right-radius: unset;
    }
    .fas {
        margin-right: unset;
    }
    .side-bar i {
        color: white;
        padding: 0 2px;
    }
}

</style>