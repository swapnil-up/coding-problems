<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();

  // Hardcoded for this page — no server load needed
  const notifications = [
    { id: 1, message: 'Alice commented on your post', read: false },
    { id: 2, message: 'Bob liked your photo', read: true },
    { id: 3, message: 'New follower: Carol', read: false },
  ];
</script>

<h1>{data.user.name}</h1>
{#each notifications as noti}
  <div style:font-weight={noti.read?'bold':'normal'}>
    {noti.message}
  </div>
{/each}
<!-- TODO: h1 with user's name -->
<!-- TODO: list notifications, showing unread ones differently (bold, or a dot) -->
