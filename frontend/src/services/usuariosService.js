import api from './api'

export default {
  listar() { return api.get('/auth/users/') },
  crear(data) { return api.post('/auth/register/', data) },
  actualizar(id, data) { return api.put(`/auth/users/${id}/`, data) },
  eliminar(id) { return api.delete(`/auth/users/${id}/`) }
}