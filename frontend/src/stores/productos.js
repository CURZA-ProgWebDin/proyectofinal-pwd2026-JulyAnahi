import { defineStore } from 'pinia'
import { ref } from 'vue'
import productosService from '@/services/productosService'

export const useProductosStore = defineStore('productos', () => {
  const productos = ref([])

  async function cargarProductos() {
    const res = await productosService.listar()
    productos.value = res.data
  }

  function actualizarStockLocal(productoId, tipo, cantidad) {
    const p = productos.value.find(prod => prod.id === productoId)
    if (p) {
      if (tipo === 'entrada') p.stock_actual += cantidad
      if (tipo === 'salida') p.stock_actual -= cantidad
    }
  }

  return { productos, cargarProductos, actualizarStockLocal }
})