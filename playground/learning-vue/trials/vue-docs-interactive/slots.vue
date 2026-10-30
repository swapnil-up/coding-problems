<script>
import ChildComp from '/home/swap/github/learning-vue/trials/ChildComponent4.vue'

export default {
  components: {
    ChildComp
  },
  data() {
    return {
      msg: 'from parent'
    }
  }
}
</script>

<template>
  <ChildComp>
  	{{msg}}
  </ChildComp>
</template>