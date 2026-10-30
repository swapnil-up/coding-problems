<script>
export default {
  mounted(){
    this.$refs.pElementRef.innerHTML= 'hehe';
  }
}
</script>

<template>
  <p ref="pElementRef">Hello</p>
</template>