import React from 'react'


export default function Todo({todo}) {
  return (
    <div>
        <label>
            {todo.name}
            {/* The checked attribute is used to check the checkbox if the todo is completed */}
            <input type = "checkbox" checked = {todo.completed} />
        </label>
    
    </div>
  )
}
