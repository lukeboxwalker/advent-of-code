<template>
  <div class="q-pa-xl">
    <div class="text-center">
      <div class="glow text-h2 ">
        Advent of Code
      </div>
      <div class="text-h6">
        <span class="year-text">
          0x0000{:/^
        </span>
        <span class="glow">
          my soltuions</span>
        <span
            class="year-text">$/}
        </span>
      </div>
    </div>
    <div v-for="(item, index) in data">
      <q-card @click="direct(item)" :style="createAnimation(index)" class="q-ma-xl q-hoverable cursor-pointer">
        <q-card-section class="row">
          <div class="col-1">
            <img width="155" height="155" :src="item.img" alt="Title Image">
          </div>
          <div class="col-11">
            <div class="year-text text-center">
              {:year <span class="glow"> {{ item.year }}</span>}
            </div>
          </div>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script setup>
import {ref} from "vue";
import router from "../router";

import {useFlatIconStore} from "../store/flaticon";

const data = ref([
  {
    year: 2021,
    img: "christmas-candle.png"
  },
  {
    year: 2020,
    img: "presents.png"
  },
])

useFlatIconStore().set({
  creator: "Icons created by Freepik - Flaticon",
  url: "https://www.flaticon.com/free-icons/test",
  title: "test icons"
})



function createAnimation(index) {
  return {
    "animation": "fadeInLeft",
    "animation-duration": index + 2 + "s"
  }
}

function direct(entry) {
  router.push("/" + entry.year)
}
</script>

<style scoped>

.year-text {
  color: #235030;
}

.glow {
  color: green;
  text-shadow: 0 0 15px green;
}

.image {
  height: 10rem;
  width: 10rem;
}

.image-box {
  width: 15em;
  text-align: center;
}
</style>
