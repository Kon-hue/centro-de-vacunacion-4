import './estilos/App.css';
import {registros_iniciales} from './data/data-inicial';
import RegistroView from './vistas/registro-view';
import ConsultaView from './vistas/consulta-view';
import LoginView from './vistas/login-view';

import React, {useState, useEffect} from 'react';

function App() {
  const [usuarioActual, setUsuarioActual] = useState(null);
  const [vistaactual, setvistaactual] = useState('consulta');

  const [registros, setregistros] = useState(() => {
    const guardado = localStorage.getItem('SISNAV_REGISTROS');
    return guardado ? JSON.parse(guardado) : registros_iniciales;
  });

  useEffect(() => {
    localStorage.setItem('SISNAV_REGISTROS', JSON.stringify(registros));
  }, [registros]);

  const handleregistrardosis = (nuevo) => {
    setregistros((prev) => [nuevo, ...prev]);
    setvistaactual('consulta');
  };

  const handleLogin = (rol, datos) => {
    setUsuarioActual({ rol, datos });
    if (rol === 'Paciente') {
      setvistaactual('consulta');
    } else {
      setvistaactual('registro');
    }
  };

  const handleLogout = () => {
    if (window.confirm('¿Seguro que deseas cerrar la sesión actual?')) {
      setUsuarioActual(null);
    }
  };

  // Si no hay usuario conectado, se muestra la pantalla de Login
  if (!usuarioActual) {
    return <LoginView onLogin={handleLogin} />;
  }

  return (
    <div className="App">
      <header className="app-header">
        <div className="app-brand">
          <span className="app-brand-icon">🏛️</span>
          <div>
            <h1 className="app-title">SISNAV</h1>
            <span className="app-subtitle">Sistema Nacional de Vacunación</span>
          </div>
        </div>

        <nav className="app-nav">
          <button
            className={`nav-btn ${vistaactual === 'consulta' ? 'active' : ''}`}
            onClick={() => setvistaactual('consulta')}
          >
            🔍 Consulta de Carnet
          </button>

          {/* Solo el personal médico o admin puede registrar dosis */}
          {usuarioActual.rol !== 'Paciente' && (
            <button
              className={`nav-btn ${vistaactual === 'registro' ? 'active' : ''}`}
              onClick={() => setvistaactual('registro')}
            >
              💉 Nuevo Registro
            </button>
          )}
        </nav>

        {/* Indicador de usuario conectado y botón salir */}
        <div className="user-badge">
          <div className="user-badge-info">
            <div className="user-badge-role">
              {usuarioActual.rol === 'Admin' && '👑 Administrador'}
              {usuarioActual.rol === 'Registrador' && '🩺 Registrador'}
              {usuarioActual.rol === 'Paciente' && '👤 Paciente'}
            </div>
            <div className="user-badge-sub">
              {usuarioActual.datos?.usuario || usuarioActual.datos?.nombre || 'Sesión Activa'}
            </div>
          </div>
          <button className="btn-logout" onClick={handleLogout} title="Cerrar sesión">
            Salir
          </button>
        </div>
      </header>

      <main className="app-main">
        {vistaactual === 'registro' && usuarioActual.rol !== 'Paciente' && (
          <RegistroView onregistrocreado={handleregistrardosis} />
        )}

        {vistaactual === 'consulta' && (
          <ConsultaView registros={registros} />
        )}
      </main>
    </div>
  );
}

export default App;
