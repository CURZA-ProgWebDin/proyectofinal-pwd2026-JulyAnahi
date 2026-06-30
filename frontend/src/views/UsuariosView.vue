<template>
  <div>
    <div class="header-section">
      <h2>Gestión de Usuarios del Sistema</h2>
      <button @click="abrirAlta" class="btn-primario">+ Agregar Nuevo Usuario</button>
    </div>

    <!-- Tabla Reactiva con Botones de Operación -->
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Nombre de Usuario</th>
          <th>Email</th>
          <th>Rol de Sistema</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in listaUsuarios" :key="user.id">
          <td>{{ user.id }}</td>
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td><span class="role-badge">{{ user.role }}</span></td>
          <td>
            <button @click="abrirEdicion(user)" class="btn-edit">Editar</button>
            <button @click="eliminar(user.id)" class="btn-danger">Eliminar</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal con Formulario para Altas y Modificaciones -->
    <BaseModal :mostrar="modalAbierto" @cerrar="modalAbierto = false">
      <template #titulo>
        <h3>{{ editando ? 'Modificar Parámetros de Usuario' : 'Registrar Nuevo Usuario' }}</h3>
      </template>
      
      <form @submit.prevent="guardar" class="form-layout">
        <label>Nombre de Usuario</label>
        <input v-model="form.username" type="text" required />

        <label>Correo Electrónico</label>
        <input v-model="form.email" type="email" required />

        <label v-if="!editando">Contraseña Inicial</label>
        <input v-if="!editando" v-model="form.password" type="password" required />

        <label>Rol Asignado</label>
        <select v-model="form.role_id" required>
          <option :value="1">Administrador (admin)</option>
          <option :value="2">Operador de Stock (operador)</option>
        </select>

        <button type="submit" class="btn-primario btn-block">
          {{ editando ? 'Aplicar Cambios' : 'Confirmar Registro' }}
        </button>
      </form>
    </BaseModal>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import usuariosService from '@/services/usuariosService'
import BaseModal from '@/components/BaseModal.vue'

const listaUsuarios = ref([])
const modalAbierto = ref(false)
const editando = ref(false)
const usuarioIdSeleccionado = ref(null)

const form = ref({ username: '', email: '', password: '', role_id: 2 })

async function cargarUsuarios() {
  const res = await usuariosService.listar()
  listaUsuarios.value = res.data
}

function abrirAlta() {
  editando.value = false
  form.value = { username: '', email: '', password: '', role_id: 2 }
  modalAbierto.value = true
}

function abrirEdicion(user) {
  editando.value = true
  usuarioIdSeleccionado.value = user.id
  form.value = { username: user.username, email: user.email, role_id: user.role === 'admin' ? 1 : 2 }
  modalAbierto.value = true
}

async function guardar() {
  try {
    if (editando.value) {
      await usuariosService.actualizar(usuarioIdSeleccionado.value, form.value)
    } else {
      await usuariosService.crear(form.value)
    }
    modalAbierto.value = false
    cargarUsuarios()
  } catch (err) {
    alert(err.response?.data?.msg || 'Error al guardar los datos')
  }
}

async function eliminar(id) {
  if (confirm('¿Desea dar de baja este usuario definitivamente?')) {
    try {
      await usuariosService.eliminar(id)
      cargarUsuarios()
    } catch (err) {
      alert(err.response?.data?.msg || 'Operación denegada')
    }
  }
}

onMounted(cargarUsuarios)
</script>

<style scoped>
.header-section { display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem; }
.form-layout { display: flex; flex-direction: column; gap: 0.8rem; }
.btn-block { width: 100%; margin-top: 1rem; }
.role-badge { background-color: #2b2b2b; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.85rem; border: 1px solid var(--borde); }
</style>
