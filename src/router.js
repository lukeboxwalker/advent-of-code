import {createRouter, createWebHistory} from "vue-router";
import YearOverview from "./components/YearOverview.vue";
import DayOverview from "./components/DayOverview.vue";
import Day from "./components/Day.vue";

const years = [
    "2020",
    "2021"
].join("|")

const days = Array(24).fill()
    .map((x, i) => (i + 1).toLocaleString('en-US', {
        minimumIntegerDigits: 2,
        useGrouping: false
    })).join("|")

const routes = [
    {
        path: '/',
        component: YearOverview
    },
    {
        path: '/:year(' + years + ')',
        component: DayOverview,
    },
    {
        path: '/:year(' + years + ')/:day(' + days + ')',
        component: Day,
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


import {useFlatIconStore} from "./store/flaticon";

router.beforeEach((to) => {
    useFlatIconStore().set(null)
})

export default router