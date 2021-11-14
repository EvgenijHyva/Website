<template>
    <section>
        <div class="container">
            <h2>{{message}}</h2>
        <video src="../assets/flamingo.mp4" loop autoplay controls muted class="video-fluid" type="video/mp4" onloadstart="this.volume=0.05"></video>
        <div class="link"><router-link :to="{name: 'Base'}"><button class="outline">Main page</button></router-link> <a href="https://google.com"> <button class="outline"> Google page </button></a></div>
    </div>
    </section>
</template>

<script>

export default {
    name: "PageNotFound",
    title() {
        return  "Error - 404 page not found"
    }, 
    data() {
        return {
            message: "404 - Page Not found",
        }
    }
}
</script>

<style scoped>
.video-fluid {
    border-radius: 5px;
    z-index: -1;
}
</style>