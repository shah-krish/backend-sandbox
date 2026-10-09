import React, {useState ,useRef, useEffect} from "react";
import TodoList from "./TodoList";
import { v4 as uuidv4 } from 'uuid'

function App() {
  // React re-renders everytime it loads. So to save our to-do list we use useState
  const [todos, setTodos] = useState([]);
  // useRef is used to get the value of the input field.
  const todoInputRef = useRef();
  const LOCAL_STORAGE_KEY = 'todoApp.todos'

  // useEffect is used to load the todos from local storage when the component is mounted. It runs only once as empty array is passed as the second argument. If we pass a state variable in the array, it will run everytime that state variable changes.
  useEffect(() => {
    const storedTodos = JSON.parse(localStorage.getItem(LOCAL_STORAGE_KEY))
    if (storedTodos) {
      setTodos(storedTodos)
    }
  }, [])

  // useEffect is used to save the todos in local storage so that they are not lost when the page is refreshed. It runs everytime the todos state changes.
  useEffect(() => {
    localStorage.setItem(LOCAL_STORAGE_KEY, JSON.stringify(todos))
  }, [todos])

  function toggleTodo(id) {
    // We create a new array of todos so that we do not directly modify the state.
    const newTodos = [...todos]
    const todo = newTodos.find(todo => todo.id === id)
    todo.completed = !todo.completed
    setTodos(newTodos)
  }

  function handleAddTodo(e) {
      const name = todoInputRef.current.value;
      if (name === "") return
      // ... copies all elements from the previous array and creates a new array with the new todo added to it. This is done because we cannot directly modify the state in React.
      setTodos(prevTodos => {
        return [...prevTodos, {id: uuidv4(), name: name, completed: false}]
      });
      // Setting the state to null so that the input field is cleared after adding a todo (looks nicer)
  }   todoInputRef.current.value = null;

  return (
    // We create blank element so that it treats both as one fragment. A function can return only one thing so this is a workaround
    <>
    {/* We pass the todos state to the TodoList component as a prop */}
    <TodoList todos = {todos} toggleTodo={toggleTodo} />
    <input ref = {todoInputRef} type = "text" />
    <button onClick={handleAddTodo}>Add Todo</button>
    <button>Clear Todo</button>
    <div>0 left to do</div>
    </>
  );
}

export default App;
