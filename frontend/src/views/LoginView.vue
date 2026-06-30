<template>
  <div class="login-wrapper">
    <div class="card-oscura login-box">
      <h2>Iniciar Sesión</h2>
      <form @submit.prevent="handleLogin" class="login-form">
        <div class="form-group">
          <label>Usuario</label>
          <input v-model="username" type="text" required />
        </div>
        <div class="form-group">
          <label>Contraseña</label>
          <input v-model="password" type="password" required />
        </div>
        <button type="submit" class="btn-primario">Ingresar al Sistema</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const username = ref('')
const password = ref('')

async function handleLogin() {
  try {
    await authStore.login(username.value, password.value)
  } catch (err) {
    alert('Credenciales incorrectas o error de conexión al servidor')
  }
}
</script>

<style scoped>
.login-wrapper { display: flex; justify-content: center; align-items: center; height: 70vh; }
.login-box { width: 100%; max-width: 400px; }
.login-form { display: flex; flex-direction: column; gap: 1rem; }
.form-group { display: flex; flex-direction: column; }
</style>