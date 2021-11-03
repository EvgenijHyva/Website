<template>
    <section>
        <div class="container">
            <h2>{{message}}</h2>
        <video :src="link" loop autoplay controls class="video-background" type="video/mp4" onloadstart="this.volume=0.15"></video>
        <div class="link"><router-link :to="{name: 'Base'}"> Main page </router-link>  |  <a href="https://google.com">Google page</a></div>
    </div>
    </section>
</template>

<script>

export default {
    name: "PageNotFound",
    title() {
        return  "Erorr - 404 page not found"
    }, 
    data() {
        return {
            message: "404 - Page Not found",
            link: "/media/video/flamingo.mp4",
        }
    }
}
</script>

<style scoped>

</style>