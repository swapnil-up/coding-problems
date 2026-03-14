<script>
  let { value, onRate } = $props();
</script>
<div class="stars">
  {#each [1, 2, 3, 4, 5] as star}
    <button
      onclick={()=>onRate(star)}
      class:active={star <= value}
      class="button">*</button
    >
  {/each}
</div>

<style>
  .stars button {
    font-size: 1.5rem;
    background: none;
    border: none;
    cursor: pointer;
    color: #ccc;
  }
  .stars button.active {
    color: gold;
  }
</style>
