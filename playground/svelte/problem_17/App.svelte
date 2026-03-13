<script>
  let notifications = $state([
    { id: 1, type: "success", message: "File saved!", dismissed: false },
    { id: 2, type: "error", message: "Upload failed.", dismissed: false },
    {
      id: 3,
      type: "info",
      message: "New version available.",
      dismissed: false,
    },
  ]);
</script>

{#each notifications as notification}
  <div
    class="notification"
    class:success={notification.type === "success"}
    class:error={notification.type === "error"}
    class:info={notification.type === "info"}
    class:dismissed={notification.dismissed}
    style:opacity={notification.dismissed ? "0.4" : "1"}
  >
    {notification.message}
    <button onclick={() => (notification.dismissed = true)}>Dismiss </button>
  </div>
{/each}

<button onclick={() => notifications.forEach((n) => (n.dismissed = false))}
  >Reset All</button
>

<style>
  .notification {
    padding: 0.75rem 1rem;
    margin: 0.5rem 0;
    border-radius: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 2px solid transparent;
  }
  .success {
    background: #d1fae5;
    border-color: #10b981;
  }
  .error {
    background: #fee2e2;
    border-color: #ef4444;
  }
  .info {
    background: #dbeafe;
    border-color: #3b82f6;
  }
  .dismissed {
    text-decoration: line-through;
  }
</style>
