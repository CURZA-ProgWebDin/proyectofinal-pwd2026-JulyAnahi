import api from './api'
export default {
  listarTodos() { return api.get('/movimientos/') },
  listarMisMovimientos() { return api.get('/movimientos/mis/') },
  registrar(data) { return api.post('/movimientos/', data) }
}