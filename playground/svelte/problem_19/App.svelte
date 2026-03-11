<script>
  // TODO: import fly from 'svelte/transition'

  const words = ['Svelte', 'Reactive', 'Compiled', 'Elegant', 'Fast'];

  // TODO: declare `index` as $state(0)
  // TODO: declare `word` as $derived(words[index])

  function prev() {
    // TODO: decrement index, but not below 0
  }

  function next() {
    // TODO: increment index, but not above words.length - 1
  }
</script>

<div class="container">
  <!-- TODO: wrap the h2 in {#key word} so the transition re-fires on each change -->
  <!-- <h2 transition:fly={{ y: -30, duration: 400 }}>{word}</h2> -->

  <div class="controls">
    <!-- TODO: Previous button (calls prev()) -->
    <!-- TODO: Next button (calls next()) -->
  </div>

  <!-- TODO: <p data-testid="info">{index + 1} / {words.length}</p> -->
</div>

<style>
  .container { text-align: center; padding: 2rem; }
  .controls { display: flex; gap: 1rem; justify-content: center; margin-top: 1rem; }
  h2 { font-size: 3rem; color: #6366f1; }
</style>
