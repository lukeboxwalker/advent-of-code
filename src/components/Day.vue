<template>
  <div class="q-pa-xl">
    <Title :title="text.title" :year="year"></Title>
    <div class="q-pa-sm">
      <highlightjs :code="code"/>
    </div>
  </div>
</template>

<script>
import hljsVuePlugin from "@highlightjs/vue-plugin";
import Title from "./Title.vue"

export default {
  name: "App",
  components: {
    highlight: hljsVuePlugin.component,
    Title
  },
};
</script>

<script setup>

import axios from "axios";
import {useRoute} from 'vue-router';
import {ref} from "vue";
import {marked} from 'marked';

const route = useRoute()
const year = route.path.split("/")[1]
const day = route.path.split("/")[2]
const code = ref("")
const text = ref({})

axios.get("https://raw.githubusercontent.com/lukeboxwalker/advent-of-code/master/year_" + year + "/day_" + day + "/puzzle.py").then(res => {
  code.value = res.data
})

axios.get("https://raw.githubusercontent.com/lukeboxwalker/advent-of-code/master/year_" + year + "/day_" + day + "/README.md").then(res => {
  const element = document.createElement('div');
  element.innerHTML = marked(res.data)
  text.value = {
    title: element.querySelector('h1').innerHTML
  }
})


</script>

<style scoped>
.glow {
  color: green;
  text-shadow: 0 0 15px green;
}

.year-text {
  color: #235030;
}
</style>