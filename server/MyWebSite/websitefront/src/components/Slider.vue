<template>
    <section>
        <h1>Slider</h1>
        
        <ul>
            <transition-group  name="fade">
            <li v-for="(number, index) in numbers" :key="number" @click="addItem(index)" >
                {{ number }}
            </li>
            </transition-group>
        </ul>
    </section>
</template>

<script>
//https://www.w3schools.com/howto/howto_js_slideshow_gallery.asp
//https://animate.style/
export default {
    name: "Slider",
    data() {
        return { 
            numbers: [1, 2, 3, 4, 5],
        }
    },
    methods: {
        addItem(ind) {
        this.numbers.splice(ind, 1)
        const num = Math.floor(Math.random()*100+1)
        const index = Math.floor(Math.random()*this.numbers.length)
        this.numbers.splice(index,0, num)
        }
    }
}
</script>

<style>
li {
    font-size: 22px;
    color: green;
    cursor: pointer;
    border: 1px solid yellow;
    width: 30px;
}
.fade-enter-from {
  opacity: 0;
}
.fade-enter-active {
  transition: all 1s linear;
}
.fade-enter-to {
  opacity: 1;
}
.fade-leave-from {
  opacity: 1;
}
.fade-leave-active {
    position: absolute;
}
.fade-leave-to {
  opacity: 0;
}
.fade-move {
    transition: all 2s linear;
}

</style>