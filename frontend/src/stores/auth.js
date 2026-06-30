import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import api from '@/services/api'
import router from '@/router'

export const useAuthStore = defineStore('auth', () => {
  const token = ref(localStorage.getItem('token') || null)
  const usuario = ref(JSON.parse(localStorage.getItem('usuario')) || null)

  const estaAutenticado = computed(() => !!token.value)
  const esAdmin = computed(() => {
    const rolActual = usuario.value?.rol
    return rolActual === 'admin' || rolActual === 'administrador'
  })

  async function login(username, password) {
    try {
      const res = await api.post('/auth/login', { username, password })
      token.value = res.data.access_token
      localStorage.setItem('token', token.value)
      await obtenerPerfil()
      router.push('/productos')
    } catch (error) {
      console.error(error)
      throw error
    }
  }

  async function obtenerPerfil() {
    try {
      const res = await api.get('/auth/me')
      usuario.value = res.data
      localStorage.setItem('usuario', JSON.stringify(res.data))
    } catch (error) {
      console.error(error)
      logout()
    }
  }

  function logout() {
    token.value = null
    usuario.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('usuario')
    router.push('/login')
  }

  return { token, usuario, estaAutenticado, esAdmin, login, logout, obtenerPerfil }
})