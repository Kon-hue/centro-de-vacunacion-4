import React, { useState } from 'react';

export default function LoginView({ onLogin }) {
  const [modo, setModo] = useState('staff');

 
  const [usuario, setUsuario] = useState('');
  const [password, setPassword] = useState('');
  const [errorStaff, setErrorStaff] = useState('');


  const [cedula, setCedula] = useState('');
  const [nombre, setNombre] = useState('');
  const [errorPaciente, setErrorPaciente] = useState('');

  
  const handleLoginStaff = (e) => {
    e.preventDefault();
    const user = usuario.trim().toLowerCase();
    const pass = password.trim();

    if (user === 'registrador' && pass === '1234') {
      onLogin('Registrador', { usuario: 'Registrador Clínico' });
    } else if (user === 'admin' && pass === 'admin123') {
      onLogin('Admin', { usuario: 'Administrador Master' });
    } else {
      setErrorStaff('Usuario o contraseña incorrectos.');
    }
  };

  
  const handleLoginPaciente = (e) => {
    e.preventDefault();
    const doc = cedula.trim();
    const nom = nombre.trim();

    if (!doc || !nom) {
      setErrorPaciente('Por favor completa todos los campos.');
      return;
    }

    onLogin('Paciente', { dni: doc, nombre: nom });
  };

  return (
    <div className="login-overlay">
      <div className="login-card">
        <div className="login-header">
          <div className="login-icon">💉</div>
          <h2 className="login-title">SISNAV</h2>
          <p className="login-subtitle">Sistema Nacional de Información de Vacunación</p>
        </div>

        
        <div className="login-tabs">
          <button
            type="button"
            className={`login-tab-btn ${modo === 'staff' ? 'active' : ''}`}
            onClick={() => {
              setModo('staff');
              setErrorStaff('');
            }}
          >
            🛡️ Personal Médico / Admin
          </button>
          <button
            type="button"
            className={`login-tab-btn ${modo === 'paciente' ? 'active' : ''}`}
            onClick={() => {
              setModo('paciente');
              setErrorPaciente('');
            }}
          >
            👤 Consulta de Paciente
          </button>
        </div>


        {modo === 'staff' && (
          <form onSubmit={handleLoginStaff} className="login-form">
            {errorStaff && <div className="login-alert-error">{errorStaff}</div>}

            <div className="login-field">
              <label>Usuario</label>
              <input
                type="text"
                placeholder="Ej: registrador o admin"
                value={usuario}
                onChange={(e) => setUsuario(e.target.value)}
                required
              />
            </div>

            <div className="login-field">
              <label>Contraseña</label>
              <input
                type="password"
                placeholder="••••••••"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            <button type="submit" className="login-submit-btn">
              Iniciar Sesión
            </button>

        
            <div className="login-demo-box">
              <p className="login-demo-title">ℹ️ Credenciales de prueba:</p>
              <p>👤 <strong>Registrador:</strong> <code>registrador</code> / pass: <code>1234</code></p>
              <p>👑 <strong>Admin:</strong> <code>admin</code> / pass: <code>admin123</code></p>
            </div>
          </form>
        )}


        {modo === 'paciente' && (
          <form onSubmit={handleLoginPaciente} className="login-form">
            {errorPaciente && <div className="login-alert-error">{errorPaciente}</div>}

            <div className="login-field">
              <label>Nº de Cédula / DNI *</label>
              <input
                type="text"
                placeholder="Ej: 12345678"
                value={cedula}
                onChange={(e) => setCedula(e.target.value)}
                required
              />
            </div>

            <div className="login-field">
              <label>Nombre Completo *</label>
              <input
                type="text"
                placeholder="Ej: Carlos Mendoza"
                value={nombre}
                onChange={(e) => setNombre(e.target.value)}
                required
              />
            </div>

            <button type="submit" className="login-submit-btn">
              Consultar mi Carnet Digital
            </button>

            <div className="login-demo-box">
              <p className="login-demo-title">💡 Nota para ciudadanos:</p>
              <p>No necesitas contraseña. Solo ingresa tu documento para consultar tus dosis registradas.</p>
            </div>
          </form>
        )}
      </div>
    </div>
  );
}
