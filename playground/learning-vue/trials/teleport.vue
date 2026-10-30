<template>
  <h1>Teleport example</h1>
  <button @click="showModal = true">Show modal</button>

  <Teleport to="body">
    <div v-if="showModal" class="modal">
      <div class="modalContent">
        <h2>teleported content</h2>
        <button @click="showModal = false">Close</button>
      </div>
    </div>
  </Teleport>
</template>

<script setup>
import { ref } from "vue";
const showModal = ref(false);
</script>

<style>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
