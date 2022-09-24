<template>
  <div class="text-center q-pa-xl">
    <div>
      <div class="glow text-h2 ">
        Advent of Code
      </div>
      <div class="text-h6">
        <span class="year-text">
          0x{{ year }}{:/^
        </span>
        <span class="glow">
          my soltuions</span>
        <span
            class="year-text">$/}
        </span>
      </div>
    </div>
    <div v-for="day in 24">
      <q-card @click="direct(day)" class="animation q-ma-xl q-hoverable cursor-pointer ">
        <q-card-section class="row">
          <div class="col-1">
            <img width="155" height="155" :src="'days/day' + day + '.png'" alt="Title Image">
          </div>
          <div class="col-11">
            <div class="text-h4 text-center">
              Day {{ day }}
            </div>
          </div>
        </q-card-section>
      </q-card>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import {useFlatIconStore} from "../store/flaticon";
import {onMounted} from "vue";
import router from "../router";

useFlatIconStore().set({
  creator: "Time and date icons created by rizal2109 - Flaticon",
  url: "https://www.flaticon.com/free-icons/time-and-date",
  title: "time and date icons"
})

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // It's visible. Add the animation class here!
      entry.target.classList.add("fade-animation")
    }
  });
});

onMounted(() => {
  document.querySelectorAll(".animation").forEach(elem => {
    const position = elem.getBoundingClientRect();
    if(position.top < window.innerHeight && position.bottom >= 0) {
      return
    }
    observer.observe(elem)
  })

})

const route = useRoute()
const year = route.path.split("/")[1]

function direct(day) {
  let formattedNumber = day.toLocaleString('en-US', {
    minimumIntegerDigits: 2,
    useGrouping: false
  })
  router.push(route.path + "/" + formattedNumber)
}

</script>

<style scoped>
.fade-animation {
  animation: fadeInLeft;
  animation-duration: 1s;
}
.glow {
  color: green;
  text-shadow: 0 0 15px green;
}

.year-text {
  color: #235030;
}
</style>