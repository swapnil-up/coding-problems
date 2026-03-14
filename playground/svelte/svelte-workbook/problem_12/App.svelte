<script>
  let tasks = $state([
    { id: 1, title: "Design mockup", priority: "high" },
    { id: 2, title: "Write tests", priority: "medium" },
    { id: 3, title: "Deploy app", priority: "low" },
    { id: 4, title: "Review PR", priority: "high" },
  ]);

  function shuffle() {
    tasks = [...tasks].sort(() => Math.random() - 0.5);
  }
</script>

<button onclick={shuffle}>Shuffle</button>

{#each tasks as task, i (task.id)}
  <div class="task">
    <span class="title">{task.title}</span>
    <span class="priority">{task.priority}</span>
    <span class="index">{i+1}</span>
  </div>
{/each}
