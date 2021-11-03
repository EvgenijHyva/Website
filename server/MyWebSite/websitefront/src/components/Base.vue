<template>
    <div>
        <transition name="change" mode="out-in">
            <component :is="activeProject"></component>
        </transition>
    </div>
</template>

<script>
import Mainpage from "./MainPage.vue";
import Bookmarks from "./Bookmarks.vue";
import Slider from "./Slider.vue";
import Calculator from "./Calculator.vue";
import QuoteGenerator from "./QuoteGenerator.vue";
import SpockRockGame from "./SpockRockGame.vue";
import Backgrounds from "./Backgrounds.vue";
import Kanban from "./Kanban.vue";
import MathSprint from "./MathSprint.vue";
import NasaApod from "./NasaApod.vue";

import { mapState } from "vuex";

export default {
    name: "Base",
    components: {
        Bookmarks, Slider, Calculator, 
        QuoteGenerator, SpockRockGame, Backgrounds, Kanban, MathSprint,
        NasaApod, Mainpage
    },
    computed: {
      ...mapState(["activeProject",]),
    },
    beforeMount: function () {
    if (localStorage.Project)
      this.$store.state.activeProject = localStorage.Project
  },
}
</script>

<style>

</style>