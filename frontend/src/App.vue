<template>
  <div class="app-layout">
    <nav v-if="authStore.estaAutenticado" class="navbar">
      <div class="nav-brand">📦 StockPro</div>
      <div class="nav-links">
        <router-link to="/productos">Productos</router-link>
        <router-link to="/movimientos">Movimientos</router-link>
        
        <!-- Enlaces Exclusivos de Administrador -->
        <router-link v-if="authStore.esAdmin" to="/categorias">Categorías</router-link>
        <router-link v-if="authStore.esAdmin" to="/proveedores">Proveedores</router-link>
        <router-link v-if="authStore.esAdmin" to="/usuarios">Usuarios</router-link>
        
        <button @click="authStore.logout" class="btn-logout">Salir</button>
      </div>
    </nav>

    <main class="main-content">
      <router-view v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </router-view>
    </main>
  </div>
</template>

<script setup>
import { useAuthStore } from '@/stores/auth'
const authStore = useAuthStore()
</script>

<style scoped>
.navbar {
  display: flex; justify-content: space-between; align-items: center;
  padding: 1rem 2rem; background-color: var(--bg-superficie); border-bottom: 1px solid var(--borde);
}
.nav-brand { font-weight: bold; font-size: 1.25rem; color: var(--color-primario); }
.nav-links a { color: var(--texto-secundario); text-decoration: none; margin-right: 1.5rem; font-weight: 500; transition: color 0.2s; }
.nav-links a.router-link-active { color: var(--color-primario); }
.nav-links a:hover { color: var(--texto-principal); }
.btn-logout { background: none; border: 1px solid var(--color-peligro); color: var(--color-peligro); padding: 0.4rem 1rem; border-radius: 4px; cursor: pointer; }
.btn-logout:hover { background-color: var(--color-peligro); color: #000; }
.main-content { padding: 2rem; max-width: 1200px; margin: 0 auto; }

.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>