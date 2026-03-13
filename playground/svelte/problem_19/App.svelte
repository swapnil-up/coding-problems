<script>
import {fly} from 'svelte/transition'

  const words = ['Svelte', 'Reactive', 'Compiled', 'Elegant', 'Fast'];

  let index =$state(0)
  let word= $derived(words[index])

  function prev() {
    if (index<1) return;
    index--
  }

  function next() {
    if (index>=words.length - 1) return;
    index++
  }
</script>

<div class="container">
{#key word}
  <h2 transition:fly={{y:-30, duration: 0}}>{word}</h2>
{/key}
  <div class="controls">
    <button onclick={()=>prev()}>Previous</button>
    <button onclick={()=>next()}>Next</button>
  </div>

  <p data-testid="info">{index + 1} / {words.length}</p>
</div>

<style>
  .container { text-align: center; padding: 2rem; }
  .controls { display: flex; gap: 1rem; justify-content: center; margin-top: 1rem; }
  h2 { font-size: 3rem; color: #6366f1; }
</style>
