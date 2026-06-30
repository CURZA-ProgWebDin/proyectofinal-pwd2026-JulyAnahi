// import { defineConfig } from 'vite'
// import vue from '@vitejs/plugin-vue'
// import { fileURLToPath, URL } from 'node:url' // <-- OBLIGATORIO

// export default defineConfig({
//   plugins: [vue()],
//   resolve: {
//     alias: {
//       // Le enseña a Vite que '@' es la ruta absoluta hacia la carpeta 'src'
//       '@': fileURLToPath(new URL('./src', import.meta.url)) 
//     }
//   },
//   server: {
//     port: 5173,
//     proxy: {
//       '/api': {
//         target: 'http://localhost:5000',
//         changeOrigin: true,
//         rewrite: (path) => path.replace(/^\/api/, '')
//       }
//     }
//   }
// })
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})