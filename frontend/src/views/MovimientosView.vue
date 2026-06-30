<template>
  <div class="card-oscura">
    <h3>Registrar Operación sobre Inventario</h3>
    <form @submit.prevent="procesar" class="form-box">
      <label>Seleccionar Producto</label>
      <select v-model="form.producto_id" required>
        <option v-for="p in prodStore.productos" :key="p.id" :value="p.id">
          {{ p.nombre }} (Stock: {{ p.stock_actual }})
        </option>
      </select>

      <label>Tipo de Operación</label>
      <select v-model="form.tipo" required>
        <option value="entrada">Entrada (Sumar Mercadería)</option>
        <option value="salida">Salida (Despachar Mercadería)</option>
      </select>

      <label>Cantidad</label>
      <input v-model.number="form.cantidad" type="number" min="1" required />

      <!-- Anticipación Preventiva UI demandada -->
      <div v-if="alertaStockInsuficiente" class="warning-banner">
        ❌ Error: No es posible despachar esa cantidad. Supera el stock real disponible.
      </div>

      <button type="submit" :disabled="alertaStockInsuficiente" class="btn-primario">
        Asentar Movimiento
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useProductosStore } from '@/stores/productos'
import movimientosService from '@/services/movimientosService'

const prodStore = useProductosStore()
const form = ref({ producto_id: '', tipo: 'entrada', cantidad: 1, motivo: 'Gestión Interna' })

onMounted(() => prodStore.cargarProductos())

const alertaStockInsuficiente = computed(() => {
  if (form.value.tipo !== 'salida' || !form.value.producto_id) return false
  const p = prodStore.productos.find(prod => prod.id === form.value.producto_id)
  return p ? form.value.cantidad > p.stock_actual : false
})

async function procesar() {
  try {
    await movimientosService.registrar(form.value)
    prodStore.actualizarStockLocal(form.value.producto_id, form.value.tipo, form.value.cantidad)
    alert('Movimiento procesado y stock sincronizado localmente.')
    form.value = { producto_id: '', tipo: 'entrada', cantidad: 1, motivo: 'Gestión Interna' }
  } catch (err) {
    alert(err.response?.data?.msg || 'Error transaccional')
  }
}
</script>

<style scoped>
.form-box { display: flex; flex-direction: column; gap: 1rem; max-width: 500px; }
.warning-banner { background-color: rgba(207, 102, 121, 0.15); color: var(--color-peligro); padding: 1rem; border-radius: 4px; border: 1px solid var(--color-peligro); font-weight: bold; }
</style>