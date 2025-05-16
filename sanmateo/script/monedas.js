window.addEventListener("DOMContentLoaded", () => {

        // Tu clave de API personal (reemplázala por la real)
        const apiKey = "a7462791ad90f57ca88540de";
    
        // URL base para obtener los datos desde la API de ExchangeRate
        const url = `https://v6.exchangerate-api.com/v6/${apiKey}/latest`;
    
        // Lista de las monedas que queremos consultar frente al peso colombiano (COP)
        const monedas = ["USD", "EUR", "GBP", "JPY", "BRL"];
    
        // Recorremos cada moneda de la lista
        monedas.forEach(moneda => {
    
        // Hacemos una solicitud a la API para cada moneda individual, con `base = moneda`
        fetch(`${url}/${moneda}`)
            .then(res => res.json()) // Convertimos la respuesta a formato JSON
            .then(data => {
            // Verificamos si la respuesta fue exitosa
            if (data.result === "success") {
                // Extraemos el valor de COP frente a la moneda base (ej. 1 USD = X COP)
                const cop = data.conversion_rates.COP;
    
                // Mostramos el valor en el elemento correspondiente del HTML (ej. <span id="usd">)
                document.getElementById(moneda.toLowerCase()).textContent = cop.toFixed(3) + " Colombian Peso";
    
                // También actualizamos el mensaje con la fecha y hora de la última actualización
                document.getElementById("fecha").textContent = "Última actualización · " + 
                    new Date(data.time_last_update_utc).toLocaleString() + " UTC";
            } else {
                // Si la API respondió con error, mostramos un mensaje alternativo
                document.getElementById(moneda.toLowerCase()).textContent = "No disponible";
            }
            })
            .catch(err => {
            // Si hubo un error en la conexión o la solicitud falló, mostramos un error en consola
            console.error("Error:", err);
    
            // Y también mostramos un mensaje de error en el HTML
            document.getElementById(moneda.toLowerCase()).textContent = "Error al cargar";
            });
    
        }); // Fin del bucle forEach
    
    }); // Fin del event listener
    
