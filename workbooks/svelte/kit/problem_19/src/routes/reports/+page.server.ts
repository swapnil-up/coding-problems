import type { PageServerLoad } from './$types';

// Simulates fast data (200ms)
async function fetchQuickStats() {
  await new Promise((r) => setTimeout(r, 200));
  return {
    totalUsers: 12_483,
    activeToday: 847,
    revenue: 48_291.50,
  };
}

// Simulates slow data (2 seconds — maybe a complex DB query or external API)
async function fetchFullReport() {
  await new Promise((r) => setTimeout(r, 2000));
  return {
    topPages: [
      { path: '/home', views: 4821 },
      { path: '/products', views: 2341 },
      { path: '/about', views: 891 },
    ],
    conversionRate: 3.2,
    avgSessionDuration: '4m 22s',
  };
}

export const load: PageServerLoad = async () => {
  return {
    // TODO: await quickStats (blocks — renders with initial HTML)
    quickStats: await fetchQuickStats(),

    // TODO: do NOT await fullReport — return the Promise directly so it streams
    // fullReport: fetchFullReport()  ← uncomment and remove the await
    fullReport: await fetchFullReport(), // ← change this line!
  };
};
