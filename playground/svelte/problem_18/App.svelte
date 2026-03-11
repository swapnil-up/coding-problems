<script>
  // TODO: import fade and fly from 'svelte/transition'

  // TODO: declare messages as $state([])
  // TODO: declare nextId as $state(1)

  function addMessage() {
    // TODO: push { id: nextId, text: `Message #${nextId}` } to messages
    // TODO: increment nextId
  }

  function removeMessage(id) {
    // TODO: filter out the message with this id
  }
</script>

<!-- TODO: "Add Message" button -->

<!-- TODO: {#each messages as msg (msg.id)}
     <div class="message" transition:fly={{ x: 200, duration: 300 }}>
       {msg.text}
       <button onclick={() => removeMessage(msg.id)}>×</button>
     </div>
     {/each}
-->

<!-- TODO: {#if messages.length === 0}
     <div class="banner" transition:fade>No messages! Add one above.</div>
     {/if}
-->

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
