import React, {useState} from "react";
import TodoList from "./TodoList";
function App() {
  // React re-renders everytime it loads. So to save our to-do list we use useState
  const [todos, setTodos] = useState([{id: 1, name: "Todo 1", completed: false}]);
  return (
    // We create blank element so that it treats both as one fragment. A function can return only one thing so this is a workaround
    <>
    {/* We pass the todos state to the TodoList component as a prop */}
    <TodoList todos = {todos} />
    <input type = "text" />
    <button>Add Todo</button>
    <button>Clear Todo</button>
    <div>0 left to do</div>
    </>
  );
}

export default App;
