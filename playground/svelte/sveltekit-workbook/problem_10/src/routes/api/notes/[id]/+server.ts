import type { RequestHandler } from './$types';
import { notesStore } from '$lib/notes';

export const DELETE: RequestHandler = ({ params }) => {
  // TODO: check note exists (return 404 if not)
  // TODO: delete note
  // TODO: return 204 No Content
};
