import React from 'react'
import Todo from './Todo'

export default function TodoList({todos, toggleTodo}) {
  return (
    todos.map(todo => {
    // Key makes sure that only the changed element is re-rendered and not the whole list
        return <Todo key={todo.id} todo = {todo} toggleTodo={toggleTodo} />
    })
  )
}
