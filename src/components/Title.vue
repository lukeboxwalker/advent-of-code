<template>
  <div class="text-center">
    <div class="glow text-h2 ">
      {{ props.title }}
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
</template>

<script setup>
const props = defineProps({
  title: {
    type: String,
    required: true
  },
  year: {
    type: String,
    default: "0000"
  }
})
</script>

<style scoped>
.glow {
  color: green;
  text-shadow: 0 0 15px green;
}

.year-text {
  color: #235030;
}
</style>