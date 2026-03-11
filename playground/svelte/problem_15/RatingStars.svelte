<script>
  // TODO: destructure props: value (current rating 0-5) and onRate (callback)
  // let { value, onRate } = $props();
</script>

<!-- TODO: render 5 star buttons in a div.stars
     {#each [1,2,3,4,5] as star}
       <button ...>★</button>
     {/each}
     
     Each button should:
     - call onRate(star) when clicked
     - have class "active" if star <= value
-->

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
