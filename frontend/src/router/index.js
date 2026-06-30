import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

// Importaciones de las Vistas Reales del Sistema
import LoginView from '@/views/LoginView.vue'
import ProductosView from '@/views/ProductosView.vue'
import MovimientosView from '@/views/MovimientosView.vue'
import CategoriasView from '@/views/CategoriasView.vue'
import ProveedoresView from '@/views/ProveedoresView.vue'
import UsuariosView from '@/views/UsuariosView.vue'
import AccesoDenegadoView from '@/views/AccesoDenegadoView.vue'

const routes = [
  { path: '/', redirect: '/productos' },
  { path: '/login', component: LoginView, meta: { publica: true } },
  { path: '/denegado', component: AccesoDenegadoView, meta: { publica: true } },
  { path: '/productos', component: ProductosView },
  { path: '/movimientos', component: MovimientosView },
  { path: '/categorias', component: CategoriasView, meta: { requiereAdmin: true } },
  { path: '/proveedores', component: ProveedoresView, meta: { requiereAdmin: true } },
  { path: '/usuarios', component: UsuariosView, meta: { requiereAdmin: true } }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Navigation Guards para restringir accesos según Token y Rol
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore()

  if (!to.meta.publica && !authStore.estaAutenticado) {
    return next('/login')
  }
  if (to.meta.requiereAdmin && !authStore.esAdmin) {
    return next('/denegado')
  }
  next()
})

export default router