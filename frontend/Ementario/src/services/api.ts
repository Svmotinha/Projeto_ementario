import axios from 'axios';

const api = axios.create({
  // Ao usar apenas '/api', o Vite faz o proxy para o Django automaticamente
  baseURL: '/api',
});

export default api;
