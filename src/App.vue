<template>
  <div id="app">
    <q-layout>
      <router-view/>
      <Footer/>
    </q-layout>
  </div>
</template>

<script>
import Footer from "./components/Footer.vue";

export default {
  components: {
    Footer
  },
}
</script>

<script setup>
import {useQuasar} from "quasar";

const $q = useQuasar()
$q.dark.set(true)
</script>

<style>
#app {
  font-family: "Source Code Pro", monospace;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}


</style>
