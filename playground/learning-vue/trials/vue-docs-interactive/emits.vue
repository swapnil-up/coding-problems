<script>
import ChildComp from '/home/swap/github/learning-vue/trials/ChildComponent3.vue'

export default {
  components: {
    ChildComp
  },
  data() {
    return {
      childMsg: 'No child msg yet'
    }
  }
}
</script>

<template>
  <ChildComp childMsg @response="(msg)=> childMsg=msg"/>
  <p>{{ childMsg }}</p>
</template>