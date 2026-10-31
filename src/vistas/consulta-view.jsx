import React, { useState } from "react";

export default function ConsultaView({ registros = [] }) {
  const [busquedadni, setbusquedadni] = useState('');
  const [historialencontrado, sethistorialencontrado] = useState([]);
  const [habuscado, sethabuscado] = useState(false);

  const handlebuscar = (e) => {
    e.preventDefault();
    sethabuscado(true);

    const busqueda = busquedadni.trim();
    
    if (!busqueda) {
      sethistorialencontrado([]);
      return;
    }

    const resultados = registros.filter(
      (r) => r.dni === busqueda
    );
    sethistorialencontrado(resultados);
  };

  return (
    <div className="Consulta">
      <h2 className="Consulta-titulo">Consulta de Vacunación</h2>
      <form onSubmit={handlebuscar}>
        <input
        type="text"
        placeholder="Ingrese DNI"
        value={busquedadni}
        onChange={(e) => setbusquedadni(e.target.value)}
        />
        <button type="submit">Buscar Carnet</button>
      </form>
      {/* 1. Si buscó y SÍ encontró vacunas */}
      {habuscado && historialencontrado.length > 0 && (
        <div>
          <h3>Historial de Vacunación</h3>
          <ul>
            {historialencontrado.map((r) => (
              <li key={r.id}>
                <p><strong>DNI:</strong> {r.dni}</p>
                <p><strong>Paciente:</strong> {r.paciente}</p>
                <p><strong>Vacuna:</strong> {r.vacunaNombre || r.vacunaid}</p>
                <p><strong>Dosis:</strong> {r.dosisNumero || r.dosisnumero}</p>
                <p><strong>Fecha:</strong> {r.fechaAplicacion || r.fechaaplicacion}</p>
                <p><strong>Lote:</strong> {r.lote}</p>
                <p><strong>Centro de Salud:</strong> {r.centroSalud || r.centrosalud}</p>
                <p><strong>Vacunador:</strong> {r.vacunador}</p>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* 2. Si buscó y NO encontró nada */}
      {habuscado && historialencontrado.length === 0 && (
        <p>No se encontraron registros para el DNI: {busquedadni}</p>
      )}
    </div>
  );
}
