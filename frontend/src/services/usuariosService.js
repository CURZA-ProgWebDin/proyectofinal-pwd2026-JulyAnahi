import api from './api'

export default {
  listar() { 
    return api.get('/auth/usuarios') 
  },
  crear(data) { 
    return api.post('/auth/register', data) 
  },
  actualizar(id, data) { 
    return api.put(`/auth/usuarios/${id}`, data) 
  },
  eliminar(id) { 
    return api.delete(`/auth/usuarios/${id}`) 
  }
}