<script lang="ts">
  import type { Note } from '$lib/notes';

  let notes = $state<Note[]>([]);
  let title = $state('');
  let content = $state('');
  let error = $state('');

  async function loadNotes() {
    // TODO: fetch GET /api/notes and set notes
  }

  async function createNote() {
    // TODO: fetch POST /api/notes with JSON body { title, content }
    // On success: reload notes, clear title/content
    // On error: set error message
  }

  async function deleteNote(id: string) {
    // TODO: fetch DELETE /api/notes/{id}
    // On success: reload notes
  }

  $effect(() => { loadNotes(); });
</script>

<h1>Notes</h1>

{#if error}<p class="error">{error}</p>{/if}

<form onsubmit={(e) => { e.preventDefault(); createNote(); }}>
  <input bind:value={title} placeholder="Title" required />
  <textarea bind:value={content} placeholder="Content..." required></textarea>
  <button type="submit">Add Note</button>
</form>

<ul>
  {#each notes as note (note.id)}
    <li>
      <strong>{note.title}</strong>
      <p>{note.content}</p>
      <small>{note.createdAt}</small>
      <button onclick={() => deleteNote(note.id)}>Delete</button>
    </li>
  {/each}
</ul>
