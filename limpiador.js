const fs = require('fs');
const path = require('path');

// Ruta simulada de registros
const rutaLogs = path.join(__dirname, 'logs');

// Crear la carpeta si no existe (para la prueba)
if (!fs.existsSync(rutaLogs)) {
    fs.mkdirSync(rutaLogs);
    fs.writeFileSync(path.join(rutaLogs, 'antiguo.log'), 'Registro viejo...');
    fs.writeFileSync(path.join(rutaLogs, 'nuevo.log'), 'Registro actual...');
}

// Script de automatización
fs.readdir(rutaLogs, (err, archivos) => {
    if (err) return console.error('Error al leer la carpeta:', err);

    archivos.forEach(archivo => {
        // Ejemplo: Eliminamos cualquier archivo que se llame 'antiguo.log'
        if (archivo.includes('antiguo')) {
            fs.unlink(path.join(rutaLogs, archivo), (err) => {
                if (err) throw err;
                console.log(`🧹 Automatización: Archivo ${archivo} eliminado con éxito.`);
            });
        }
    });
});