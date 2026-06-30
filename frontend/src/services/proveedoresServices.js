import api from './api'
export default {
  listar() { return api.get('/proveedores/') },
  crear(data) { return api.post('/proveedores/', data) },
  actualizar(id, data) { return api.put(`/proveedores/${id}`, data) },
  eliminar(id) { return api.delete(`/proveedores/${id}`) }
}