<script>
  import RatingStars from "./RatingStars.svelte";
  let rating = $state(0);
</script>

<RatingStars onRate={(r) => (rating = r)} value={rating} />
<p data-testid="rating">
  {#if rating == 0}
    No rating yet
  {:else}
    Rating: {rating}/5
  {/if}
</p>
