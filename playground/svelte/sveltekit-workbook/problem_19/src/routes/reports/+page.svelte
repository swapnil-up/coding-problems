<script lang="ts">
  import type { PageData } from './$types';
  let { data }: { data: PageData } = $props();
</script>

<h1>Reports Dashboard</h1>

<!-- Quick stats are available immediately — just render them -->
<section class="quick-stats">
  <h2>Quick Stats</h2>
  <!-- TODO: show data.quickStats.totalUsers, activeToday, revenue -->
</section>

<!-- Full report is a Promise — use {#await} to handle the three states -->
<section class="full-report">
  <h2>Full Report</h2>
  <!-- TODO: {#await data.fullReport}
         <div class="skeleton">Loading report...</div>
       {:then report}
         show report.topPages, report.conversionRate, report.avgSessionDuration
       {:catch error}
         <p>Failed to load report: {error.message}</p>
       {/await}
  -->
</section>

<style>
  .quick-stats, .full-report { background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:1.5rem; margin:1rem 0; }
  .skeleton { background: linear-gradient(90deg, #e2e8f0 25%, #f1f5f9 50%, #e2e8f0 75%); background-size: 200%; animation: shimmer 1.5s infinite; padding:2rem; border-radius:4px; }
  @keyframes shimmer { 0%{background-position:200%} 100%{background-position:-200%} }
</style>
