import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async () => {
  const feedItems = [
    { 
      id: '1', 
      title: 'Top Funny post', 
      author: 'User123', 
      timestamp: '2026-03-17T10:00:00Z' 
    },
    { 
      id: '2', 
      title: 'Mouse Micky found in server room', 
      author: 'TechLead', 
      timestamp: '2026-03-17T11:30:00Z' 
    },
    { 
      id: '3', 
      title: 'Monitor gets scolded for low brightness', 
      author: 'HardwareGuy', 
      timestamp: '2026-03-17T12:45:00Z' 
    },
  ];

  return {
    feedItems: feedItems
  };
  // TODO: return { feedItems: [...] } with at least 3 fake post objects
  // Each item should have: id, title, author, timestamp
};
