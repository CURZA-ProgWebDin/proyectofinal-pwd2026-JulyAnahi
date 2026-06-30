<template>
  <div>
    <div class="header-section">
      <h2>Gestión de Categorías de Productos</h2>
      <button @click="abrirAlta" class="btn-primario">+ Crear Nueva Categoría</button>
    </div>

    <!-- Buscador en tiempo real usando Propiedad Computada -->
    <div class="search-container">
      <input v-model="filtro" type="text" placeholder="Filtrar categorías por nombre..." class="search-input" />
    </div>

    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre de Categoría</th>
          <th>Descripción</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="cat in categoriasFiltradas" :key="cat.id">
          <td>{{ cat.id }}</td>
          <td class="cat-name">{{ cat.nombre }}</td>
          <td class="cat-desc">{{ cat.descripcion || 'Sin descripción' }}</td>
          <td>
            <button @click="abrirEdicion(cat)" class="btn-edit">Editar</button>
            <button @click="eliminar(cat.id)" class="btn-danger">Eliminar</button>
          </td>
        </tr>
        <tr v-if="categoriasFiltradas.length === 0">
          <td colspan="4" style="text-align: center; color: var(--texto-secundario);">
            No se encontraron categorías.
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal Reutilizable con Formulario Incorporado -->
    <BaseModal :mostrar="modalAbierto" @cerrar="modalAbierto = false">
      <template #titulo>
        <h3>{{ editando ? 'Modificar Categoría' : 'Registrar Nueva Categoría' }}</h3>
      </template>
      
      <form @submit.prevent="guardar" class="form-layout">
        <label>Nombre de la Categoría</label>
        <input v-model="form.nombre" type="text" required placeholder="Ej. Almacén, Limpieza..." />

        <label>Descripción (Opcional)</label>
        <textarea v-model="form.descripcion" rows="4" placeholder="Breve descripción del tipo de productos..."></textarea>

        <button type="submit" class="btn-primario btn-block">
          {{ editando ? 'Guardar Cambios' : 'Crear Categoría' }}
        </button>
      </form>
    </BaseModal>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import BaseModal from '../components/BaseModal.vue'

// Importación corregida a nivel relativo y con el nombre real físico del servicio
import categoriasService from '../services/categoriasServices.js'

// Estados reactivos
const listaCategorias = ref([])
const filtro = ref('')
const modalAbierto = ref(false)
const editando = ref(false)
const categoriaIdSeleccionada = ref(null)

const form = ref({ nombre: '', descripcion: '' })

// Lógica de carga de datos desde la API
async function cargarCategorias() {
  try {
    const res = await categoriasService.listar()
    listaCategorias.value = res.data
  } catch (err) {
    alert('Error al conectar con el servidor para listar categorías.')
  }
}

// Propiedad Computada para buscar interactivamente
const categoriasFiltradas = computed(() => {
  return listaCategorias.value.filter(cat =>
    cat.nombre.toLowerCase().includes(filtro.value.toLowerCase())
  )
})

// Control de apertura del Modal
function abrirAlta() {
  editando.value = false
  form.value = { nombre: '', descripcion: '' }
  modalAbierto.value = true
}

function abrirEdicion(cat) {
  editando.value = true
  categoriaIdSeleccionada.value = cat.id
  form.value = { nombre: cat.nombre, descripcion: cat.descripcion }
  modalAbierto.value = true
}

// Envío de datos (Altas y Modificaciones)
async function guardar() {
  try {
    if (editando.value) {
      await categoriasService.actualizar(categoriaIdSeleccionada.value, form.value)
    } else {
      await categoriasService.crear(form.value)
    }
    modalAbierto.value = false
    cargarCategorias()
  } catch (err) {
    alert(err.response?.data?.msg || 'Error al procesar la categoría. Verifique que el nombre no esté duplicado.')
  }
}

// Eliminación y captura obligatoria del error 409 Conflict
async function eliminar(id) {
  if (confirm('¿Está seguro de eliminar esta categoría? Esta acción no se puede deshacer.')) {
    try {
      await categoriasService.eliminar(id)
      cargarCategorias()
    } catch (err) {
      if (err.response && err.response.status === 409) {
        alert('⚠️ Error 409 Conflict:\nNo se puede eliminar la categoría porque tiene productos asociados en el inventario.')
      } else {
        alert(err.response?.data?.msg || 'No se pudo completar la operación de borrado.')
      }
    }
  }
}

onMounted(cargarCategorias)
</script>

<style scoped>
.header-section {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}
.search-container {
  margin-bottom: 1rem;
}
.search-input {
  width: 100%;
  box-sizing: border-box;
}
.form-layout {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}
textarea {
  background-color: var(--bg-input);
  color: var(--texto-principal);
  border: 1px solid var(--borde);
  padding: 0.75rem;
  border-radius: 4px;
  font-family: inherit;
  font-size: 1rem;
  resize: vertical;
}
textarea:focus {
  outline: 2px solid var(--color-primario);
}
.btn-block {
  width: 100%;
  margin-top: 1rem;
}
.cat-name {
  font-weight: 600;
  color: var(--color-primario);
}
.cat-desc {
  color: var(--texto-secundario);
  font-size: 0.95rem;
}
</style>