<script>
  import { page } from '$app/state';
  import { pushState, goto } from '$app/navigation';

  // 1. Static: Captured once on mount, won't update
  let staticParam = page.params.id;

  // 2. Reactive with $derived: Updates when page changes
  let reactiveParam = $derived(page.params.id);

  // 3. page.state: What pushState actually updates (shallow routing)
  let shallowState = $derived(page.state);
  $effect(()=>{
  console.log(shallowState);
})

  function triggerPushState() {
    const newId = Math.floor(Math.random() * 1000);
    // pushState(url, state) — updates page.state only, NOT page.params
    pushState(`/test/${newId}`, { customId: newId });
  }

  function triggerGoto() {
    const newId = Math.floor(Math.random() * 1000);
    // goto does a real navigation — updates params, url, everything
    goto(`/test/${newId}`, { replaceState: true, noScroll: true });
  }
</script>

<h2>SvelteKit Reactivity Test</h2>
<div style="border: 1px solid #ccc; padding: 1rem; line-height: 2;">
  <p><strong>URL in Address Bar:</strong> {page.url.pathname}</p>
  <hr />
  <p>❌ <strong>Static Variable:</strong> {staticParam} <small>(Won't change)</small></p>
  <p>✅ <strong>Reactive ($derived):</strong> {reactiveParam} <small>(Updates with goto, not pushState)</small></p>
  <p>✅ <strong>page.state (pushState target):</strong> {JSON.stringify(shallowState)} <small>(Updates with pushState)</small></p>
</div>

<button onclick={triggerPushState}>Test pushState (Shallow — updates state only)</button>
<button onclick={triggerGoto}>Test goto (Full nav — updates params + URL)</button>

<style>
  button { margin-top: 10px; display: block; padding: 10px; cursor: pointer; }
</style>