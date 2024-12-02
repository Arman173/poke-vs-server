function onSelectChange(event) {
    const selectedValue = event.target.value;
    console.log(`La opción seleccionada es: ${selectedValue}`);
    // Aquí puedes agregar cualquier otra lógica que necesites
  }
  
  // Asignar la función a un elemento <select> por su ID
  // const selectElement = document.getElementById('pokemon1'); // Cambia el ID según tu select
  // selectElement.addEventListener('change', onSelectChange);

console.log("DOM loaded");

const sel = document.getElementById("frutas")
sel.addEventListener('change', onSelectChange)