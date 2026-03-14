<script>
  import Card from "./Card.svelte";
</script>

<div class="grid">
  <Card />
  <Card />
  <Card />
</div>

<style>
  .grid {
    display: flex;
    gap: 1rem;
    padding: 1rem;
  }
</style>
