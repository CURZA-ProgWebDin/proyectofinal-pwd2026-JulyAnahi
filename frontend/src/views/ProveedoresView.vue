<template>
  <div>
    <div class="header-section">
      <h2>Gestión de Proveedores de Mercadería</h2>
      <button @click="abrirAlta" class="btn-primario">+ Registrar Proveedor</button>
    </div>

    <!-- Buscador Reactivo -->
    <div class="search-container">
      <input v-model="filtro" type="text" placeholder="Filtrar por nombre de empresa o empresa..." class="search-input" />
    </div>

    <!-- Tabla de Datos -->
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Razón Social / Nombre</th>
          <th>Contacto</th>
          <th>Teléfono</th>
          <th>Email</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="prov in proveedoresFiltrados" :key="prov.id">
          <td>{{ prov.id }}</td>
          <td class="prov-name">{{ prov.nombre }}</td>
          <td>{{ prov.contacto || 'No especificado' }}</td>
          <td>{{ prov.telefono || 'No especificado' }}</td>
          <td class="prov-email">{{ prov.email || 'No especificado' }}</td>
          <td>
            <button @click="abrirEdicion(prov)" class="btn-edit">Editar</button>
            <button @click="eliminar(prov.id)" class="btn-danger">Eliminar</button>
          </td>
        </tr>
        <tr v-if="proveedoresFiltrados.length === 0">
          <td colspan="6" style="text-align: center; color: var(--texto-secundario);">
            No se encontraron proveedores cargados en el sistema.
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal Reutilizable -->
    <BaseModal :mostrar="modalAbierto" @cerrar="modalAbierto = false">
      <template #titulo>
        <h3>{{ editando ? 'Actualizar Ficha de Proveedor' : 'Registrar Nuevo Proveedor' }}</h3>
      </template>
      
      <form @submit.prevent="guardar" class="form-layout">
        <label>Razón Social / Nombre Completo</label>
        <input v-model="form.nombre" type="text" required placeholder="Ej. Distribuidora Central S.A." />

        <label>Persona de Contacto</label>
        <input v-model="form.contacto" type="text" placeholder="Ej. Juan Pérez" />

        <label>Teléfono de Línea / Celular</label>
        <input v-model="form.telefono" type="text" placeholder="Ej. +54 11 2233-4455" />

        <label>Correo Electrónico</label>
        <input v-model="form.email" type="email" placeholder="Ej. contacto@empresa.com" />

        <button type="submit" class="btn-primario btn-block">
          {{ editando ? 'Guardar Cambios' : 'Confirmar Alta' }}
        </button>
      </form>
    </BaseModal>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import BaseModal from '../components/BaseModal.vue'

// Importaciones corregidas con rutas relativas limpias y el nombre físico exacto del archivo
import proveedoresService from '../services/proveedoresServices.js'

const listaProveedores = ref([])
const filtro = ref('')
const modalAbierto = ref(false)
const editando = ref(false)
const proveedorIdSeleccionado = ref(null)

const form = ref({ nombre: '', contacto: '', telefono: '', email: '' })

async function cargarProveedores() {
  try {
    const res = await proveedoresService.listar()
    listaProveedores.value = res.data
  } catch (err) {
    alert('Error de red al intentar listar los proveedores.')
  }
}

const proveedoresFiltrados = computed(() => {
  return listaProveedores.value.filter(p =>
    p.nombre.toLowerCase().includes(filtro.value.toLowerCase())
  )
})

function abrirAlta() {
  editando.value = false
  form.value = { nombre: '', contacto: '', telefono: '', email: '' }
  modalAbierto.value = true
}

function abrirEdicion(prov) {
  editando.value = true
  proveedorIdSeleccionado.value = prov.id
  form.value = { nombre: prov.nombre, contacto: prov.contacto, telefono: prov.telefono, email: prov.email }
  modalAbierto.value = true
}

async function guardar() {
  try {
    if (editando.value) {
      await proveedoresService.actualizar(proveedorIdSeleccionado.value, form.value)
    } else {
      await proveedoresService.crear(form.value)
    }
    modalAbierto.value = false
    cargarProveedores()
  } catch (err) {
    alert(err.response?.data?.msg || 'Error al guardar los datos del proveedor.')
  }
}

async function eliminar(id) {
  if (confirm('¿Desea eliminar este proveedor de los registros comerciales?')) {
    try {
      await proveedoresService.eliminar(id)
      cargarProveedores()
    } catch (err) {
      if (err.response && err.response.status === 409) {
        alert('⚠️ Error 409 Conflict:\nNo se puede eliminar este proveedor porque hay productos activos en el inventario vinculados a su firma.')
      } else {
        alert(err.response?.data?.msg || 'Operación de borrado rechazada.')
      }
    }
  }
}

onMounted(cargarProveedores)
</script>

<style scoped>
.header-section { display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem; }
.search-container { margin-bottom: 1rem; }
.search-input { width: 100%; box-sizing: border-box; }
.form-layout { display: flex; flex-direction: column; gap: 0.8rem; }
.btn-block { width: 100%; margin-top: 1rem; }
.prov-name { font-weight: 600; color: var(--color-primario); }
.prov-email { color: var(--texto-secundario); font-size: 0.95rem; }
</style>