<template>
  <div class="denied-wrapper">
    <div class="card-oscura error-box">
      <div class="shield-icon">🛡️</div>
      <h2>403 - Acceso Restringido</h2>
      <p class="error-msg">
        Tu nivel de privilegios actual (Operador de Stock) no te permite visualizar ni operar sobre este módulo.
      </p>
      <div class="action-divider"></div>
      <router-link to="/productos" class="btn-back">
        Volver al Panel de Productos
      </router-link>
    </div>
  </div>
</template>

<script setup>
// Módulo meramente informativo y de redirección de seguridad controlada
</script>

<style scoped>
.denied-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 60vh;
}
.error-box {
  text-align: center;
  max-width: 450px;
  width: 100%;
  border: 1px solid rgba(207, 102, 121, 0.3);
}
.shield-icon {
  font-size: 3.5rem;
  margin-bottom: 1rem;
}
h2 {
  color: var(--color-peligro);
  margin-top: 0;
  font-size: 1.75rem;
}
.error-msg {
  color: var(--texto-secundario);
  line-height: 1.5;
  margin-bottom: 1.5rem;
}
.action-divider {
  height: 1px;
  background-color: var(--borde);
  margin-bottom: 1.5rem;
}
.btn-back {
  display: inline-block;
  background-color: var(--bg-input);
  color: var(--color-primario);
  border: 1px solid var(--color-primario);
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  text-decoration: none;
  font-weight: bold;
  transition: all 0.2s ease;
}
.btn-back:hover {
  background-color: var(--color-primario);
  color: #000000;
}
</style>