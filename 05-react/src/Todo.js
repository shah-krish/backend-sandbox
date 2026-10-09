import React from 'react'


export default function Todo({todo}, toggleTodo) {
    function handleTodoClick() {
        toggleTodo(todo.id)
    }
  return (
    <div>
        <label>
            {todo.name}
            {/* The checked attribute is used to check the checkbox if the todo is completed */}
            <input type = "checkbox" checked = {todo.completed} onChange={handleTodoClick} />
        </label>
    
    </div>
  )
}
