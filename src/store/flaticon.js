import {defineStore} from "pinia";
import {ref} from 'vue'

export const useFlatIconStore = defineStore('flatIcon', () => {

    const refList = ref([])

    return {
        refList,
        set: (newRefList) => {
            refList.value = newRefList
        },
    }
})
