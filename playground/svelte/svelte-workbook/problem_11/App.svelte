<script>
  let signal = $state("red")
</script>

<div class="light">
  {#if signal==='red'}
  <p data-testid="message" style="color: red;">Stop!</p>
  {:else if signal==="yellow"}
  <p data-testid="message" style="color: yellow;">Slow down!</p>
  {:else if signal==="green"}
  <p data-testid="message" style="color: green;">Go!</p>
  {:else}
  <p data-testid="message">Unknown Signal</p>
  {/if}

  <button onclick={()=>signal = 'red'}>Red</button>
  <button onclick={()=>signal = 'yellow'}>Yellow</button>
  <button onclick={()=>signal = 'green'}>Green</button>

  <span data-testid="signal">{signal}</span>
</div>