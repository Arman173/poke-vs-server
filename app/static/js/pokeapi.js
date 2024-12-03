const API_URL = 'https://pokeapi.co/api/v2/pokemon?limit=700'; // Cambia el límite si quieres más Pokémon
const pokemon1Select = document.getElementById('pokemon1');
const pokemon2Select = document.getElementById('pokemon2');
const battleForm = document.getElementById('battleForm');
let pokemons = {}; // Esta variable almacenará los Pokémon de la API local

// Función para cargar los Pokémon desde tu API local
async function cargarPokemons() {
  try {
    // Realizar la solicitud GET a la API
    const response = await fetch('/pokemon'); // Cambia esta URL a la de tu API real

    if (!response.ok) {
      throw new Error('Error en la carga de datos');
    }

    // Parsear la respuesta JSON
    pokemons = await response.json();

    // Ahora 'pokemons' contiene los datos de los Pokémon que puedes usar
    console.log(pokemons);

    return pokemons;
  } catch (error) {
    console.error('Hubo un problema con la solicitud Fetch:', error);
  }
}

// Llamar a la función para cargar los Pokémon
cargarPokemons();

// Función para obtener los datos del Pokémon (incluyendo imagen y estadísticas)
async function obtenerDatosPokemon(pokemonName) {
  const response = await fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`);
  const data = await response.json();
  return data;
}

// Cargar la lista de Pokémon en los selectores
async function loadPokemon(onSuccess) {
  try {
    const response = await fetch(API_URL);
    const data = await response.json();
    data.results.forEach(pokemon => {
      const option1 = document.createElement('option');
      const option2 = document.createElement('option');
      option1.value = pokemon.name;
      option1.textContent = pokemon.name;
      option2.value = pokemon.name;
      option2.textContent = pokemon.name;
      pokemon1Select.appendChild(option1);
      pokemon2Select.appendChild(option2);
    });
    onSuccess();
  } catch (error) {
    console.error('Error al cargar la lista de Pokémon:', error);
  }
}

// Función para enviar los datos al endpoint
battleForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  
  const pkm1 = pokemon1Select.value;
  const pkm2 = pokemon2Select.value;

  if (pkm1 === pkm2) {
    alert('Por favor, selecciona dos Pokémon diferentes.');
    return;
  }

  const payload = { pkm1, pkm2 };
  console.log('Enviando datos:', payload);

  try {
    const response = await fetch('/combat', { // Cambia esta URL por tu endpoint real
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    if (response.ok) {
      const responseData = await response.json(); // Leer el JSON de la respuesta
      console.log('Respuesta recibida:', responseData);

      const winnerName = responseData.received_data.winner;
      console.log('Ganador:', winnerName);

      // Obtener los detalles del ganador
      const winnerData = await obtenerDatosPokemon(winnerName);
      mostrarGanador(winnerName, winnerData);
    } else {
      const errorMessage = await response.text();
      console.error('Error en la respuesta del servidor:', errorMessage);
      alert('Error al procesar la solicitud en el servidor.');
    }
  } catch (error) {
    console.error('Error al enviar los datos:', error);
    alert('Hubo un problema al conectar con el servidor.');
  }
});

// Función para mostrar el ganador en la interfaz
function mostrarGanador(winner, winnerData) {
  // Mostrar la sección del ganador
  document.getElementById('winner-info').style.display = 'block';

  // Actualizar el nombre del ganador
  document.getElementById('winner-name').textContent = winner;

  // Actualizar la imagen del ganador
  document.getElementById('winner-image').src = winnerData.sprites.front_default;

  // Actualizar las estadísticas
  document.getElementById('winner-hp').textContent = winnerData.stats[0].base_stat;
  document.getElementById('winner-attack').textContent = winnerData.stats[1].base_stat;
  document.getElementById('winner-defense').textContent = winnerData.stats[2].base_stat;
  document.getElementById('winner-spatk').textContent = winnerData.stats[3].base_stat;
  document.getElementById('winner-spdef').textContent = winnerData.stats[4].base_stat;
  document.getElementById('winner-speed').textContent = winnerData.stats[5].base_stat;
}

// Función para manejar el cambio de selección de Pokémon
function onPokemonSelectedChange(event) {
  console.log(event.target, event.target.value);
}

function onListLoaded() {
  console.log("lists loaded!");
  pokemon1Select.addEventListener('change', onPokemonSelectedChange);
  pokemon2Select.addEventListener('change', onPokemonSelectedChange);
}

// Llamar a la función para cargar Pokémon
loadPokemon(onListLoaded);
