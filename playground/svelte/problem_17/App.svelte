<script>
  // TODO: declare notifications with the 3 objects from the problem description
</script>

<!-- TODO: render each notification as a div.notification with:
     - class:success, class:error, class:info based on type
     - class:dismissed based on dismissed
     - style:opacity based on dismissed
     - message text
     - a "Dismiss" button that sets dismissed = true for this notification
-->

<!-- TODO: a "Reset All" button that sets all notifications' dismissed back to false -->

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
  .success { background: #d1fae5; border-color: #10b981; }
  .error   { background: #fee2e2; border-color: #ef4444; }
  .info    { background: #dbeafe; border-color: #3b82f6; }
  .dismissed { text-decoration: line-through; }
</style>
