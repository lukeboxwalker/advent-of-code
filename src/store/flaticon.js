import {defineStore} from "pinia";
import {ref} from 'vue'

export const useFlatIconStore = defineStore('flatIcon', () => {

    const details = ref(null)

    return {
        details,
        set: (newDetails) => {
            details.value = newDetails
        },
    }
})
