export async function getTasks() {
    const res = await fetch("http://localhost:8000/tasks");
    return res.json();
}