import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig(({command, mode}) => {
  return{
    plugins: [vue(),],
    build: {
      emptyOutDir: true,
      outDir: '../static/auctions/vue',
    },
    base: (mode == 'development') ? 'https://localhost:5173' : '/static/auctions/vue/',
  }
})
