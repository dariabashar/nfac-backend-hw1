import { useState } from 'react';
import axios from 'axios';

type Props = {
    onTaskCreated: () => void;
};

function TaskForm({ onTaskCreated }: Props) {
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');

    const createTask = async () => {
        await axios.post('http://localhost:8000/tasks/', {
            title,
            description,
            deadline: null,
        });
        setTitle('');
        setDescription('');
        onTaskCreated();
    };

    return (
        <div className="mb-4">
            <input className="border p-1 mr-2" placeholder = "Title" value={title} onChange={(e) => setTitle(e.target.value)} />
            <input className="border p-1 mr-2" placeholder="Description" value={description} onChange={(e) => setDescription(e.target.value)} />
            <button className="bg-blue-500 text-white px-2 py-1" onClick={createTask}> Add Task </button>
        </div>
    );
}

export default TaskForm;
