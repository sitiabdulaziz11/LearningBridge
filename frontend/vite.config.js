import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  assetsInclude: ['**/*.png', '**/*.PNG'],  // Add this line to include PNG files
  server: {
    proxy: {
      '/api/v1/': {
        target: 'http://127.0.0.1:5000',  // Replace with your Flask backend's address
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/v1/, ''),  // Adjust the regex to match your prefix
      },
    },
  },
});


