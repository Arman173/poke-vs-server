const API_URL = 'https://pokeapi.co/api/v2/pokemon?limit=151'; // Cambia el límite si quieres más Pokémon
const pokemon1Select = document.getElementById('pokemon1');
const pokemon2Select = document.getElementById('pokemon2');
const battleForm = document.getElementById('battleForm');

// Cargar la lista de Pokémon
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

// Enviar los datos al endpoint
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
      updateWinner(responseData.received_data.winner)

      // Muestra el resultado de la batalla en la interfaz
      // alert(`Ganador: ${responseData}`);
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

function updateWinner(name) {
  console.log(name);
}

function onPokemonSelectedChange() {}

function onListLoaded() {
  console.log("lists loaded!");
  pokemon1Select.addEventListener('change')
  pokemon2Select.addEventListener('change')
}

// Llamar a la función para cargar Pokémon
loadPokemon(onListLoaded);