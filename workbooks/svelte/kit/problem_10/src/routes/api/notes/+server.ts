import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { notesStore } from '$lib/notes';

export const GET: RequestHandler = () => {
  return json(notesStore.all())
};

export const POST: RequestHandler = async ({ request }) => {
  const { title, content } = await request.json()
  if (!title || !content) {
    return json({ error: 'Title and content required' }, { status: 400 })
  }

  const newNote = notesStore.create(title, content)
  return json(newNote, {status: 201})
  // TODO: parse JSON body
  // TODO: validate title and content exist (return 400 if not)
  // TODO: create note and return json with status 201
};
