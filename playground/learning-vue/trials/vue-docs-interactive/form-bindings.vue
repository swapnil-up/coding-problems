<script>
export default {
  data() {
    return {
      text: ''
    }
  },
  methods: {
    onInput(e) {
      this.text = e.target.value //target returns the element where event occurs
    }
  }
}
</script>

<template>
  <input v-model=text placeholder="Type here">
  <p>{{ text }}</p>
</template>