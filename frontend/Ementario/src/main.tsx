import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import './index.css'
import App from './App.tsx'

// Ponto de entrada do front-end: injeta o App e habilita roteamento client-side.
createRoot(document.getElementById('root')!).render(
  <StrictMode>
    {/* BrowserRouter habilita navegacao por URL real dentro do SPA */}
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </StrictMode>,
)
