export type Note = { id: string; title: string; content: string; createdAt: string };

// In-memory store
let notes: Note[] = [];

export const notesStore = {
  all: () => notes,
  get: (id: string) => notes.find((n) => n.id === id),
  create: (title: string, content: string): Note => {
    const note: Note = { id: Date.now().toString(), title, content, createdAt: new Date().toISOString() };
    notes = [...notes, note];
    return note;
  },
  delete: (id: string) => {
    notes = notes.filter((n) => n.id !== id);
  },
};
