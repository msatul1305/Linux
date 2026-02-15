import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import { AgentProvider } from './context/AgentContext'
import { ErrorBoundary } from './components/ErrorBoundary'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ErrorBoundary>
      <AgentProvider>
        <App />
      </AgentProvider>
    </ErrorBoundary>
  </StrictMode>,
)
