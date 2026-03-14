// Simple in-memory store — resets on server restart (that's fine for practice)
export type Todo = { id: string; text: string; done: boolean };

let todos: Todo[] = [
  { id: '1', text: 'Learn SvelteKit routing', done: true },
  { id: '2', text: 'Master form actions', done: false },
  { id: '3', text: 'Build something real', done: false },
];

export const todosStore = {
  all: () => todos,
  add: (text: string) => {
    todos = [...todos, { id: Date.now().toString(), text, done: false }];
  },
  remove: (id: string) => {
    todos = todos.filter((t) => t.id !== id);
  },
  toggle: (id: string) => {
    todos = todos.map((t) => (t.id === id ? { ...t, done: !t.done } : t));
  },
};
