<template>
  <div class="q-pa-xl">
    <Title title="Advent of Code"></Title>
    <div v-for="item in data">
      <q-card @click="direct(item)" class="q-ma-xl q-hoverable cursor-pointer">
        <q-card-section class="row">
          <div class="col-1">
            <q-img class="icon" :src="item.img"/>
          </div>
          <div class="col-11 flex flex-center">
            <div class="year-text text-h4 text-center">
              {:year <span class="glow"> {{ item.year }}</span>}
            </div>
          </div>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script>
import Title from "./Title.vue"
export default {
  components: {
    Title,
  }
}
</script>

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

useFlatIconStore().set([{
  creator: "Icons created by Freepik - Flaticon",
  url: "https://www.flaticon.com/free-icons/test",
  title: "test icons"
}])


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

.icon {
  width: 100px;
  height: 100px;
}

</style>
