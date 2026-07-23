import type { RequestHandler } from './$types';
import { notesStore } from '$lib/notes';

export const DELETE: RequestHandler = ({ params }) => {
  const note = notesStore.get(params.id);

  if (!note) {
    return new Response('Note not found', { status: 404 });
  }

  notesStore.delete(params.id);

  return new Response(null, { status: 204 });
  // TODO: check note exists (return 404 if not)
  // TODO: delete note
  // TODO: return 204 No Content
};
