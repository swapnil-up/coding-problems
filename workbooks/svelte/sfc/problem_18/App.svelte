<script>
  import { fade, fly, slide, scale } from "svelte/transition";

  let messages = $state([]);
  let nextId = $state(1);

  function addMessage() {
    messages = [...messages, { id: nextId, text: `Message #${nextId}` }];
    nextId++;
  }

  function removeMessage(id) {
    messages = messages.filter((m) => m.id !== id);
  }
</script>

<button onclick={() => addMessage()}>Add Message</button>
{#each messages as msg (msg.id)}
  <div class="message" transition:fly={{ x: 200, duration: 0 }}>
    {msg.text}
    <button onclick={() => removeMessage(msg.id)}>×</button>
  </div>
{/each}
{#if messages.length === 0}
  <div class="banner" transition:fade={{duration:0}}>No messages! Add one above.</div>
{/if}

<style>
  .message {
    background: #eff6ff;
    border: 1px solid #bfdbfe;
    border-radius: 6px;
    padding: 0.75rem;
    margin: 0.5rem 0;
    display: flex;
    justify-content: space-between;
  }
  .banner {
    color: #9ca3af;
    font-style: italic;
    margin-top: 1rem;
  }
</style>
