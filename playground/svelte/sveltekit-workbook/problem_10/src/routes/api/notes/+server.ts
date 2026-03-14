import { json } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import { notesStore } from '$lib/notes';

export const GET: RequestHandler = () => {
  // TODO: return json of all notes
};

export const POST: RequestHandler = async ({ request }) => {
  // TODO: parse JSON body
  // TODO: validate title and content exist (return 400 if not)
  // TODO: create note and return json with status 201
};
