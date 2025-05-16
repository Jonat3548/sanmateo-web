window.addEventListener('load', () => {
    // CLIMA - OpenWeatherMap
    const temperaturaValor = document.getElementById('temperatura-valor');
    const temperaturaDescripcion = document.getElementById('temperatura-descripcion');
    const ubicacion = document.getElementById('ubicacion');
    const iconoAnimado = document.getElementById('iconoAnimado');

    const weatherApiKey = "f040c4d3a2cd3042e6c67bcb241797ed";
    const weatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=Bogota&appid=${weatherApiKey}&lang=es&units=metric`;

    fetch(weatherUrl)
        .then(response => response.json())
        .then(data => {
            temperaturaValor.textContent = `${Math.round(data.main.temp)}°C`;
            temperaturaDescripcion.textContent = data.weather[0].description.toUpperCase();
            ubicacion.textContent = data.name;
            const iconCode = data.weather[0].icon;
            iconoAnimado.src = `https://openweathermap.org/img/wn/${iconCode}@2x.png`;
        })
        .catch(error => {
            console.error("Error al obtener los datos del clima:", error);
            temperaturaDescripcion.textContent = "No se pudo cargar el clima.";
        });

    // SLIDER DE IMÁGENES
    const imagenes = [
        'recursos/imagenes/7.jpg',
        'recursos/imagenes/8.jpg',
        'recursos/imagenes/slide2.jpeg',
        'recursos/imagenes/slide3.jpg',
        'recursos/imagenes/slide1.jpeg'
    ];

    let indice = 0;
    const slide = document.getElementById('slider');

    function cambiarImagen() {
        if (!slide) return; // sale si no hay slider
        indice = (indice + 1) % imagenes.length;
        slide.src = imagenes[indice];
    }

    setInterval(cambiarImagen, 5000); // Cambia cada 5 segundos

    // CARRUSEL CATÁLOGO
    let desplazamientoCatalogo = 0;
    const catalogoCarrusel = document.getElementById('catalogoCarrusel');

    window.moverCatalogo = function(direccion) {
        const anchoTarjeta = catalogoCarrusel.querySelector('.programa').offsetWidth + 20;
        desplazamientoCatalogo += direccion * anchoTarjeta;
        const maxDesplazamiento = catalogoCarrusel.scrollWidth - catalogoCarrusel.offsetWidth;

        if (desplazamientoCatalogo < 0) desplazamientoCatalogo = 0;
        if (desplazamientoCatalogo > maxDesplazamiento) desplazamientoCatalogo = maxDesplazamiento;

        catalogoCarrusel.style.transform = `translateX(-${desplazamientoCatalogo}px)`;
    };

    // CAMBIO DE SECCIONES
    window.mostrarContenido = function(seccion) {
        const contenido = document.getElementById("contenido");
        const botones = document.querySelectorAll(".botonera button");

        botones.forEach(btn => btn.classList.remove("activo"));
        event.target.classList.add("activo");

        let html = "";
        switch (seccion) {
            case 'prensa':
            case 'quienes':
                html = '<p>La oficina de egresados es el área encargada de promover la interacción con los egresados...</p>';
                break;
            case 'educacion':
            case 'politica':
                html = '<p>La institución monitorea de manera periódica el impacto de los programas de formación mediante el vínculo con los egresados...</p>';
                break;
            case 'ingsis':
                html = ' listo ';
                break;
            case 'editorial':
                html = `
                    <div class="moneda"><div class="subtitulo">1 US Dollar =</div><div class="precio" id="usd">...</div></div>
                    <div class="moneda"><div class="subtitulo">1 Euro =</div><div class="precio" id="eur">...</div></div>
                    <div class="moneda"><div class="subtitulo">1 Libra Esterlina =</div><div class="precio" id="gbp">...</div></div>
                    <div class="moneda"><div class="subtitulo">1 Yen Japonés =</div><div class="precio" id="jpy">...</div></div>
                    <div class="moneda"><div class="subtitulo">1 Real Brasileño =</div><div class="precio" id="brl">...</div></div>
                    <div class="actualizacion" id="fecha"></div>`;
                obtenerMonedas();
                break;
            case 'pagos':
                html = '<p>Consulta aquí los métodos de pago, calendarios y soporte financiero para estudiantes.</p>';
                break;
            case 'juridico':
                html = '<p>El Consultorio Jurídico ofrece asesoría legal gratuita a la comunidad. Infórmate aquí.</p>';
                break;
        }

        contenido.innerHTML = html;
    };

    // MONEDAS - ExchangeRate-API
    window.obtenerMonedas = function() {
        const apiKey = "a7462791ad90f57ca88540de"; // ← reemplaza por tu clave real de ExchangeRate-API
        const url = `https://v6.exchangerate-api.com/v6/${apiKey}/latest`;
        const monedas = ["USD", "EUR", "GBP", "JPY", "BRL"];

        monedas.forEach(moneda => {
            fetch(`${url}/${moneda}`)
                .then(res => res.json())
                .then(data => {
                    if (data.result === "success") {
                        const cop = data.conversion_rates.COP;
                        document.getElementById(moneda.toLowerCase()).textContent = cop.toFixed(3) + " Colombian Peso";
                        document.getElementById("fecha").textContent = "Última actualización · " + 
                            new Date(data.time_last_update_utc).toLocaleString() + " UTC";
                    }
                })
                .catch(err => {
                    console.error("Error:", err);
                });
        });
    };

    async function obtenerValorDolar() {
        try {
            const respuesta = await fetch('https://api.exchangerate-api.com/v4/latest/USD');
            const datos = await respuesta.json();
            const tasaCOP = datos.rates.COP;
            document.getElementById('valorDolar').innerText = tasaCOP.toLocaleString('es-CO', { minimumFractionDigits: 2 });
        } catch (error) {
            console.error('Error al obtener el valor del dólar:', error);
            document.getElementById('valorDolar').innerText = 'No disponible';
        }
    }

    obtenerValorDolar();

    function mostrarAsignaturas(index, nombreCarrera, asignaturas) {
        const contenido = document.getElementById("contenido");
        let html = `<h2>${nombreCarrera}</h2><ul>`;
        asignaturas.forEach(asignatura => {
            html += `<li>${asignatura}</li>`;
        });
        html += `</ul>`;
        contenido.innerHTML = html;
    }

    async function mostrarNombreUniversidad() {
        try {
            const respuesta = await fetch('https://8dd34a19-e6c7-4d53-9286-3fc1bb6ad547-00-3tkkzfux4q507.kirk.replit.dev:3000/api/programas');
            const datos = await respuesta.json();

            document.getElementById('nombreUniversidad').innerText = datos.provider;
            
            const botones = [
                { id: 'mat1', programa: datos.programas[0] },
                { id: 'mat2', programa: datos.programas[1] },
                { id: 'mat3', programa: datos.programas[2] }
            ];

            botones.forEach((btn, index) => {
                const boton = document.getElementById(btn.id);
                boton.innerText = btn.programa.nombre;
                boton.onclick = () => mostrarAsignaturas(index, btn.programa.nombre, btn.programa.asignaturas);
            });

        } catch (error) {
            console.error('Error al obtener los datos:', error);
        }
    }

    mostrarNombreUniversidad();

    async function mostrarNombreUniversidad2() {
        try {
            const respuesta = await fetch('https://8dd34a19-e6c7-4d53-9286-3fc1bb6ad547-00-3tkkzfux4q507.kirk.replit.dev:3000/api/clase/jonathan%20sanchez');
            const datos = await respuesta.json();
            document.getElementById('listo').innerText = datos.nombre;
            document.getElementById('listo2').innerText = datos.mensaje;
        } catch (error) {
            console.error('Error al obtener los datos:', error);
        }
    }

    mostrarNombreUniversidad2();

    async function mostrarNombreUniversidad3() {
        try {
            const respuesta = await fetch('https://8dd34a19-e6c7-4d53-9286-3fc1bb6ad547-00-3tkkzfux4q507.kirk.replit.dev:3000/api/salario/carlos%20sanchez/20500');
            const datos = await respuesta.json();
            
            document.getElementById('listo3').innerText = "El nombre es: " + datos.nombre;
            document.getElementById('listo4').innerText = "El salario mensual es: $" + datos.salario_mensual;
            document.getElementById('listo5').innerText = "El salario anual es: $" + datos.salario_anual;
            document.getElementById('listo6').innerText = "Paga en pensión: $" + datos.pension_mensual;
        } catch (error) {
            console.error('Error al obtener los datos:', error);
        }
    }
    mostrarNombreUniversidad3();

        document.getElementById('exportarExcel').addEventListener('click', async () => {
            try {
            const response = await fetch('https://8dd34a19-e6c7-4d53-9286-3fc1bb6ad547-00-3tkkzfux4q507.kirk.replit.dev:3000/api/programas');
            const data = await response.json();
            const programas = data.programas;
        
            // Preparamos los datos para Excel (una fila por asignatura con su programa)
            const datosParaExcel = [];
            programas.forEach(programa => {
                programa.asignaturas.forEach(asignatura => {
                datosParaExcel.push({
                    Programa: programa.nombre,
                    Asignatura: asignatura
                });
                });
            });
        
            // Convertir a hoja de cálculo
            const worksheet = XLSX.utils.json_to_sheet(datosParaExcel);
            const workbook = XLSX.utils.book_new();
            XLSX.utils.book_append_sheet(workbook, worksheet, "Asignaturas");
        
            // Descargar el archivo
            XLSX.writeFile(workbook, "asignaturas_universidad_san_mateo.xlsx");
            } catch (error) {
            console.error("Error al exportar a Excel:", error);
            }
        });

    async function mostrarpoke() {
    try {
        const respuesta = await fetch('https://pokeapi.co/api/v2/pokemon/pikachu');
        const datos = await respuesta.json();

        // Mostrar nombre
        document.getElementById('poke').innerText = "El nombre es: " + datos.name;

        // Mostrar imagen (con fallback)
        const imagen = datos.sprites.other['official-artwork'].front_default || datos.sprites.front_default;
        document.getElementById('img-pokemon1').src = imagen;

    } catch (error) {
        console.error('Error al cargar el Pokémon', error);
        document.getElementById('poke').innerText = "No se pudo cargar el Pokémon";
    }
}

window.addEventListener('load', () => {
    mostrarpoke(); // Esto ejecuta tu función cuando carga la página
});

});
