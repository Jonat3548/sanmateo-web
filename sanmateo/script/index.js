const namePokemon = document.getElementById('name-pokemon');
const imgPokemon = document.getElementById('img-pokemon');

const peticionApi = async () => {
    const peticionGet = await fetch('https://pokeapi.co/api/v2/pokemon/pikachu');
    const datosPokemon = await peticionGet.json();

    // Traemos el nombre
    const nombreBulbasaur = datosPokemon.species.name;
    namePokemon.textContent = nombreBulbasaur;

    // Traemos la imagen
    const imagenBulbasaur = datosPokemon.sprites.other.home.front_female;
    imgPokemon.src = imagenBulbasaur;
};

// Llamamos la función
peticionApi();
