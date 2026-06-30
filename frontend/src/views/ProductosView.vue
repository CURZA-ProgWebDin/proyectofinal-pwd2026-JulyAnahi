<template>
  <div>
    <h2>Inventario General de Productos</h2>
    <table>
      <thead>
        <tr>
          <th>Producto</th>
          <th>Categoría</th>
          <th>Proveedor</th>
          <th>Stock Actual</th>
          <th>Estado</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="p in prodStore.productos" :key="p.id" :class="{ 'critico': p.stock_actual <= p.stock_minimo }">
          <td>{{ p.nombre }}</td>
          <td>{{ p.categoria }}</td>
          <td>{{ p.proveedor }}</td>
          <td>{{ p.stock_actual }} / {{ p.stock_minimo }} (Mín)</td>
          <td>
            <span v-if="p.stock_actual <= p.stock_minimo" class="status-low">⚠️ Reponer</span>
            <span v-else class="status-ok">✔ Normal</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useProductosStore } from '@/stores/productos'

const prodStore = useProductosStore()
onMounted(() => prodStore.cargarProductos())
</script>

<style scoped>
.critico { background-color: rgba(207, 102, 121, 0.08); }
.status-low { color: var(--color-peligro); font-weight: bold; }
.status-ok { color: var(--color-exito); }
</style>