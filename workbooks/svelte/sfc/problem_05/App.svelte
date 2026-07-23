<script>
  let count = $state(0)
</script>
<p data-testid="count">Count: {count}</p>
<button class="Increment" onclick={()=>count+=1}>Increment</button>
<button class="Decrement" onclick={()=>count-=1}>Decrement</button>
<button class="Reset" onclick={()=>count=0}>Reset</button>