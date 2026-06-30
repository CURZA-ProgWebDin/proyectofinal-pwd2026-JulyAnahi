import api from './api'
export default {
  listar() { return api.get('/categorias/') },
  crear(data) { return api.post('/categorias/', data) },
  actualizar(id, data) { return api.put(`/categorias/${id}`, data) },
  eliminar(id) { return api.delete(`/categorias/${id}`) }
}