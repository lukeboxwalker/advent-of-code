<template>
    <div class="q-mb-xl">
        <div class="row justify-center">
            <q-separator class="col q-ml-xl q-mr-xl"/>
        </div>
        <div class="row justify-center">
            <router-link to="/" class=" text-h5 q-ma-lg">
                <q-avatar >
                    <q-icon  :name="fabGithub"/>
                </q-avatar>
                Github
            </router-link>

            <router-link to="/" class=" text-h5 q-ma-lg">
                <q-avatar>
                    <q-icon s :name="fabDiscord"/>
                </q-avatar>
                Discord
            </router-link>

            <router-link to="/" class="text-h5 q-ma-lg">
                <q-avatar>
                    <q-icon dark  name="mail"/>
                </q-avatar>
                Contact
            </router-link>
        </div>

        <div v-if="flatIcon.details" class="row justify-center">
            <a class="text-h6" :href="flatIcon.details.url" title="test icons">
                {{flatIcon.details.creator}}
                <q-icon name="launch"/>
            </a>
        </div>
    </div>
</template>

<script>
export default {
    name: "Footer"
}
</script>

<script setup>
import {fabGithub, fabDiscord} from '@quasar/extras/fontawesome-v6'
import {useFlatIconStore} from "../store/flaticon";

const flatIcon = useFlatIconStore()

console.log(flatIcon.details)

</script>

<style scoped>
a:link {
    text-decoration: none;
}

a:visited {
    text-decoration: none;
}

a:hover {
    text-decoration: none;
}

a:active {
    text-decoration: none;
}

a, a:hover, a:visited, a:active {
    color: inherit;
    text-decoration: none;
}
</style>
