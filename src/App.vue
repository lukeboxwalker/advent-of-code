<template>
  <div id="app">
    <Overview></Overview>
  </div>
</template>

<script>
import Overview from './components/Overview.vue'

export default {
  components: {
    Overview
  },
  name: 'App',
}
</script>

<style>
#app {
  font-family: "Source Code Pro", monospace;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #aaaaaa;
  margin-top: 60px;
}

body {
  background: #0f0f23;
}
</style>
