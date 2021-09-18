<template>
    <section v-if="user !== 'Anonymous'">
        <h1>{{message}}</h1>
    </section>
</template>

<script>
export default {
    name: "EditForm",
    props: ["user"],
    title () {
        return "Profile editing"
    },
    data() {
        return {
            message: "Edit form is under construction"
        }
    },
    methods: {

    }
}
</script>

<style scoped>

</style>