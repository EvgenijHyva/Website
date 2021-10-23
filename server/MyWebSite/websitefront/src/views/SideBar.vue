<template>
    <div class="side-bar">
        <i class="fas fa-plus-circle" title="Add new question" @click="createNewQuestion"></i>
    </div>
</template>

<script>
export default {
    name: "side-bar",
    data() {
        return {

        }
    },
    methods: {
        createNewQuestion()  {

        }
    },
}
</script>

<style scoped>
.side-bar {
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
}
.side-bar i:hover {
    color: green;
}

</style>