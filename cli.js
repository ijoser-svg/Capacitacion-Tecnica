// Captura los argumentos pasados por la terminal (ej: node cli.js Juan)
const argumentos = process.argv.slice(2);
const nombreUsuario = argumentos[0];

if (!nombreUsuario) {
    console.log('❌ Error: Por favor, proporciona un nombre. Ejemplo: node cli.js TuNombre');
    process.exit(1);
}

console.log(`🚀 ¡Hola, ${nombreUsuario}! Herramienta CLI de Node.js ejecutada correctamente.`);
console.log(`Fecha actual del sistema: ${new Date().toLocaleDateString()}`);