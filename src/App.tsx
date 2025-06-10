import TaskList from './components/TaskList';
import './App.css';
import './index.css';

function App() {
  return (
    <div className='p-4 max-w-xl mx-auto'>
      <h1 className='text-2xl font bold mb-4'>My tasks for today:</h1>
      <TaskList />
    </div>
  );
}

export default App;
