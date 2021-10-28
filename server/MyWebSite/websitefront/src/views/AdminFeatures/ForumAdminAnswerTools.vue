<template>
    <div class="admin-panel">
        <i class="fas fa-folder-minus" v-if="showDeleted" title="Hide Deleted" @click="toggleDeleted" ></i>
        <i class="fas fa-folder-plus" v-else title="Show Deleted" @click="toggleDeleted" :class="{ 'hidden-detected':hidenMessages }"></i>
    </div>
</template>

<script>
export default {
    name:"AdminAnswerTool",
    data() {
        return {
            showDeleted: false,
        }
    },
    props: ["hidenMessages"],
    emits: ["toggle-deleted"],
    methods: {
        toggleDeleted() {
            this.showDeleted = !this.showDeleted
            this.$emit("toggle-deleted", this.showDeleted)
        }
    }
}
</script>

<style scoped>
.admin-panel {
    display: flex;
    flex-direction: column;
    position: fixed;
    right: 0;
    top: 50%;
    background: var(--forum-background);
    padding: 10px 5px;
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
}

.admin-panel i {
    color: white;
}
.admin-panel i:hover {
    color: green;
}
.hidden-detected {
    color: #d34573 !important;
}
@media  screen and (max-width: 800px) {
    .admin-panel{
        bottom: 0;
        top: unset;
        left: 0;
        right: 0;
        padding: 10px;
        border-top-left-radius: 15px;
        border-bottom-right-radius: unset;
    }
    .fas {
        margin-right: unset;
    }
}


</style>