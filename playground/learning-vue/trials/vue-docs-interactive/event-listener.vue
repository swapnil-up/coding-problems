<script>
export default {
  data() {
    return {
      count: 0
    }
  },
  methods:{
    increment(){
      this.count++
    }
  }
}
</script>

<template>
  <!-- make this button work -->
  <button v-on:click="increment">Count is: {{ count }}</button>
</template>