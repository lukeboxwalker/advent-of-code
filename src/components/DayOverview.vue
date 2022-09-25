<template>
  <div class="q-pa-xl">
    <Title title="Advent of Code" :year="year"></Title>
    <div v-for="(solution, day) in dayStore.days">
      <q-card @click="direct(day + 1)" class="q-ma-xl q-hoverable cursor-pointer ">
        <q-card-section class="row">
          <div class="col-1 ">
            <q-img class="day" :src="'days/day' + (day + 1) + '.png'">

            </q-img>
          </div>
          <div class="col-10 flex flex-center">
            <div :style="styleForDay(solution.solved)" class="text-h4 text-center">
              {{solution.title}}
            </div>
          </div>
          <div class="col-1">
            <q-img v-if="solution.part1 !== '0'" class="star1" src="/star/star.png">
              <q-tooltip>
                Part 1 solved
              </q-tooltip>
            </q-img>
            <q-img v-if="solution.part2 !== '0'" class="star2" src="/star/star.png">
              <q-tooltip>
                Part 2 solved
              </q-tooltip>
            </q-img>
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
import {useRoute} from 'vue-router';
import {useFlatIconStore} from "../store/flaticon";
import {useDayStore} from "../store/day";
import {ref, onMounted} from "vue";
import router from "../router";

useFlatIconStore().set([
  {
    creator: "Time and date icons created by rizal2109 - Flaticon",
    url: "https://www.flaticon.com/free-icons/time-and-date",
    title: "time and date icons"
  },
  {
    creator: "Star icons created by Freepik - Flaticon",
    url: "https://www.flaticon.com/free-icons/star",
    title: "star icons"
  }
])

const route = useRoute()
const year = route.path.split("/")[1]

function direct(day) {
  let formattedNumber = day.toLocaleString('en-US', {
    minimumIntegerDigits: 2,
    useGrouping: false
  })
  router.push(route.path + "/" + formattedNumber)
}

const dayStore = useDayStore()
dayStore.setDays(year)

console.log(dayStore.days)

function styleForDay(solved) {
  if (solved) {
    return {
      "color": "green",
      "text-shadow": "0 0 15px green"
    }
  }
  return {
    "color": "red",
    "text-shadow": "0 0 15px red"
  }
}

</script>

<style scoped>

.day {
  width: 100px;
  height: 100px;
}
.star1 {
  width: 25px;
  height: 25px;
  background: transparent;
  margin: 5px;

}
.star2 {
  width: 25px;
  height: 25px;
  background: transparent;

}
</style>