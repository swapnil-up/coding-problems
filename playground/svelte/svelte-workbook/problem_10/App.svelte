<script>
  import Badge from "./Badge.svelte";
  let badges = [
    { label: "New", color: "green" },
    { label: "Hot", color: "red", size: "large" },
    { label: "Draft" },
  ];
</script>

{#each badges as badge}
  <Badge {...badge} />
{/each}
