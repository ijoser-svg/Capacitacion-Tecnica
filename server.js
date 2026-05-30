const express = require('express');
const app = express();
app.use(express.json()); // Middleware para entender JSON

let tareas = [
    { id: 1, titulo: 'Aprender Node.js', completada: true },
    { id: 2, titulo: 'Subir proyecto a Git', completada: false }
];

// GET: Obtener todas las tareas
app.get('/api/tareas', (req, res) => {
    res.json(tareas);
});

// POST: Crear una nueva tarea
app.post('/api/tareas', (req, res) => {
    const nuevaTarea = {
        id: tareas.length + 1,
        titulo: req.body.titulo,
        completada: false
    };
    tareas.push(nuevaTarea);
    res.status(201).json(nuevaTarea);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Servidor API corriendo en el puerto ${PORT}`));