<template>
  <div v-if="mostrar" class="modal-backdrop" @click.self="$emit('cerrar')">
    <div class="modal-content card-oscura">
      <header class="modal-header">
        <slot name="titulo"><h3>Formulario</h3></slot>
        <button class="btn-cerrar" @click="$emit('cerrar')">×</button>
      </header>
      <main class="modal-body">
        <slot></slot>
      </main>
    </div>
  </div>
</template>

<script setup>
defineProps({ mostrar: { type: Boolean, required: true } })
defineEmits(['cerrar'])
</script>

<style scoped>
.modal-backdrop {
  position: fixed; top: 0; left: 0; width: 100vw; height: 100vh;
  background: rgba(0, 0, 0, 0.8); display: flex; justify-content: center; align-items: center; z-index: 1000;
}
.modal-content { width: 100%; max-width: 500px; }
.modal-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--borde); padding-bottom: 0.5rem; margin-bottom: 1rem; }
.btn-cerrar { background: none; border: none; color: var(--texto-secundario); font-size: 1.5rem; cursor: pointer; }
</style>