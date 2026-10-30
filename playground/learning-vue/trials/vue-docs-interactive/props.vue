<script>
import ChildComp from '/home/swap/github/learning-vue/trials/ChildComponent2.vue'

export default {
  components: {
    ChildComp
  },
  data() {
    return {
      greeting: 'Hello from parent'
    }
  }
}
</script>

<template>
  <ChildComp v-bind:msg="greeting"/>
</template>