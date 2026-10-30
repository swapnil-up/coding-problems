<script>
// give each todo a unique id
let id = 0

export default {
  data() {
    return {
      newTodo: '',
      todos: [
        { id: id++, text: 'Learn HTML' },
        { id: id++, text: 'Learn JavaScript' },
        { id: id++, text: 'Learn Vue' }
      ]
    }
  },
  methods: {
    addTodo() {
      var id=this.todos.length+1
      console.log(id)
      var text = document.getElementById("my-input").value
      const obj={id:id,text:text}
      this.todos.push(obj)
    },
    
    removeTodo(todo) {
      console.log(this.todos)
      this.todos=this.todos.filter(t=>t.id!==todo.id)
    }
  }
}
</script>

<template>
  <form @submit.prevent="addTodo">
    <input id="my-input" v-model="newTodo" required placeholder="new todo">
    <button>Add Todo</button>
  </form>
  <ul>
    <li v-for="todo in todos" :key="todo.id">
      {{ todo.text }}
      <button @click="removeTodo(todo)">X</button>
    </li>
  </ul>
</template>