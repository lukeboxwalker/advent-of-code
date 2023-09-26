import {defineStore} from "pinia";
import {ref} from 'vue'
import axios from "axios";
import {marked} from "marked";

export const useDayStore = defineStore('day', () => {

    const days = ref([])

    function base(year, day) {
        let formattedDay = day.toLocaleString('en-US', {
            minimumIntegerDigits: 2,
            useGrouping: false
        })
        return "https://raw.githubusercontent.com/lukeboxwalker/advent-of-code/master/year_" + year + "/day_" + formattedDay + "/"
    }


    async function getSolution(year, day) {
        try {
            const res = await axios.get(base(year, day) + "solution.txt")
            const readme = await axios.get(base(year, day) + "README.md")
            const element = document.createElement('div');
            element.innerHTML = marked(readme.data)

            const data = res.data.split("\n")
            return {
                solved: true,
                part1: data[0].replace("Part 1: ", ""),
                part2: data[1].replace("Part 2: ", ""),
                title: element.querySelector('h1').innerHTML
            }
        } catch (err) {
            return {
                solved: false,
                part1: "0",
                part2: "0",
                title: "Day " + day + ": Not solved ❌"
            }
        }
    }

    async function getSolutions(year) {
        for (let i = 1; i < 25; i++) {
            const res = await getSolution(year, i)
            days.value.push(res)
        }
    }

    return {
        days,
        setDays: (year) => {
            days.value = []
            for (let i = 1; i < 25; i++) {
                let data = {
                    solved: false,
                    part1: "0",
                    part2: "0",
                    title: "Day " + i + ": Loading..."
                }
                days.value.push(data);
                getSolution(year, i).then(res => {
                    data.solved = res.solved;
                    data.part1 = res.part1;
                    data.part2 = res.part2;
                    data.title = res.title;
                })
            }
        },
    }
})
