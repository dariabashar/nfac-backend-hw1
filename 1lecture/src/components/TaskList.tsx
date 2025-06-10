import axios from 'axios';
import TaskForm from './TaskForm';
import { useState } from 'react';
import { useEffect } from 'react';

type Task = {
    id: number;
    title: string;
    description: string;
    completed: boolean;
};

function TaskList() {
    const [tasks, setTasks] = useState<Task[]>([]);

    const fetchTasks = async () => {
        const res = await axios.get<Task[]>('http://localhost:8000/tasks/');
        setTasks(res.data);
      }; 

    const deleteTask = async (id: number) => {
        await axios.delete(`http://localhost:8000/tasks/${id}`);
        fetchTasks();
      };
      
    const toggleCompleted = async (id: number, completed: boolean) => {
        await axios.put(`http://localhost:8000/tasks/${id}`, {
          completed: !completed,
        });
        fetchTasks();
      };
      
    useEffect( () => {
        fetchTasks();
    }, []);

    return (
        <div>
            <TaskForm onTaskCreated={fetchTasks} />
            <ul className="space-y-2">
  {tasks.map((task) => (
    <li key={task.id} className="border p-2 rounded flex justify-between items-center">
      <div>
      <div className={task.completed ? "line-through text-gray-500" : ""}>
  <strong>{task.title}</strong> – {task.description}
</div>

        {task.completed && <span className="text-green-500 ml-2">✔</span>}
      </div>
      <div className="flex gap-2">
        <button onClick={() => toggleCompleted(task.id, task.completed)} className="text-sm text-blue-600">
        {task.completed ? "↩ Esc" : "✔ Done"} </button>
        <button onClick={() => deleteTask(task.id)} className="text-sm text-red-500"> Delete </button>
      </div>
    </li>
  ))}
</ul>
</div>
);
}
export default TaskList;