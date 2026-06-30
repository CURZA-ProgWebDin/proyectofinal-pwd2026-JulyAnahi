import api from './api'
export default {
  listar() { return api.get('/productos/') },
  crear(data) { return api.post('/productos/', data) },
  actualizar(id, data) { return api.put(`/productos/${id}`, data) },
  eliminar(id) { return api.delete(`/productos/${id}`) }
}