import React, { useState, useEffect, useRef } from "react";
import { catalogo_vacunas } from "../data/data-inicial";
import { centros_salud } from "../data/data-inicial";

export default function RegistroView({ onregistrocreado }) {
  const [form, setform] = useState({
    dni: "",
    paciente: "",
    vacunaid: "",
    dosisnumero: "",
    fechaaplicacion: "",
    lote: "",
    centrosalud: "",
    vacunador: ""
  });

  const [errores, seterrores] = useState({});

  const [mostrarconfirmacion, setmostrarconfirmacion] = useState(false);

  const [resultadoguardado, setresultadoguardado] = useState(null);

  const [habilitadoregistro, sethabilitadoregistro] = useState(false);

  const inputdniref = useRef(null);

  useEffect(() => {
    if (inputdniref.current) {
      inputdniref.current.focus();
    }
  }, []);

  const handleinputchange = (e) => {
    const { name, value } = e.target;
    setform((prev) => ({
      ...prev,
      [name]: value
    }));
  };

  const validarformulario = () => {
    const errores = {};

    if (!form.dni.trim()) {
      errores.dni = "DNI es obligatorio";
    }

    if (!form.paciente.trim()) {
      errores.paciente = "Nombre del paciente es obligatorio";
    }

    if (!form.vacunaid) {
      errores.vacunaid = "Vacuna es obligatoria";
    }

    if (!form.fechaaplicacion) {
      errores.fechaaplicacion = "Fecha de aplicación es obligatoria";
    }

    if (!form.centrosalud) {
      errores.centrosalud = "Centro de salud es obligatorio";
    }

    seterrores(errores);
    return Object.keys(errores).length === 0;
  };

  const handleGuardar = () => {
    if (!validarformulario()) {
      return;
    }

    setmostrarconfirmacion(true);
  };

  const handleconfirmarguardado = () => {
    setmostrarconfirmacion(false);

    const nuevoregistro = {
      ...form,
      id: Date.now().toString()
    };

    onregistrocreado(nuevoregistro);

    setresultadoguardado({ 
      ok: true, 
      mensaje: "Registro guardado exitosamente",
      datos: nuevoregistro
    });

    setform({
      dni: "",
      paciente: "",
      vacunaid: "",
      dosisnumero: "",
      fechaaplicacion: "",
      lote: "",
      centrosalud: "",
      vacunador: ""
    });

    setTimeout(() => {
      setresultadoguardado(null);
    }, 5000);
  };

  const handlecancelarguardado = () => {
    setmostrarconfirmacion(false);
  };

  useEffect(() => {
    const habilitado = validarformulario() && !mostrarconfirmacion;
    sethabilitadoregistro(habilitado);
  }, [form, mostrarconfirmacion]);

  return (
    <div className="registro-view">
      <h2 className="registro-title">Registro de Vacunación</h2>

      <form onSubmit={(e) => e.preventDefault()} className="registro-form">
        <div className="registro-form-row">
          <label className="registro-label">DNI *</label>
          <input
            ref={inputdniref}
            type="text"
            name="dni"
            value={form.dni}
            onChange={handleinputchange}
            className={errores.dni ? "input-error" : ""}
          />
          {errores.dni && <p className="error-message">{errores.dni}</p>}
        </div>

        <div className="registro-form-row">
          <label className="registro-label">Paciente *</label>
          <input
            type="text"
            name="paciente"
            value={form.paciente}
            onChange={handleinputchange}
            className={errores.paciente ? "input-error" : ""}
          />
          {errores.paciente && <p className="error-message">{errores.paciente}</p>}
        </div>

        <div className="registro-form-row">
          <label className="registro-label">Vacuna *</label>
          <select
            name="vacunaid"
            value={form.vacunaid}
            onChange={handleinputchange}
            className={errores.vacunaid ? "input-error" : ""}
          >
            <option value="">Seleccionar Vacuna...</option>
            {catalogo_vacunas.map((v) => (
              <option key={v.id} value={v.nombre}>
                {v.nombre} ({v.fabricante})
              </option>
            ))}

          </select>
          {errores.vacunaid && <p className="error-message">{errores.vacunaid}</p>}
        </div>

        <div className="registro-form-row">
          <label className="registro-label">Dosis</label>
          <input
            type="number"
            name="dosisnumero"
            value={form.dosisnumero}
            onChange={handleinputchange}
            min="1"
            max="10"
          />
        </div>

        <div className="registro-form-row">
          <label className="registro-label">Fecha de Aplicación *</label>
          <input
            type="date"
            name="fechaaplicacion"
            value={form.fechaaplicacion}
            onChange={handleinputchange}
            className={errores.fechaaplicacion ? "input-error" : ""}
          />
          {errores.fechaaplicacion && <p className="error-message">{errores.fechaaplicacion}</p>}
        </div>

        <div className="registro-form-row">
          <label className="registro-label">Lote</label>
          <input
            type="text"
            name="lote"
            value={form.lote}
            onChange={handleinputchange}
          />
        </div>

        <div className="registro-form-row">
          <label className="registro-label">Centro de Salud *</label>
                    <select
            name="centrosalud"
            value={form.centrosalud}
            onChange={handleinputchange}
            className={errores.centrosalud ? "input-error" : ""}
          >
            <option value="">Seleccionar Centro de Salud...</option>
            {centros_salud.map((c) => (
              <option key={c.id} value={c.nombre}>
                {c.nombre} ({c.municipio})
              </option>
            ))}
          </select>
          {errores.centrosalud && <p className="error-message">{errores.centrosalud}</p>}
        </div>

        <div className="registro-form-row">
          <label className="registro-label">Vacunador</label>
          <input
            type="text"
            name="vacunador"
            value={form.vacunador}
            onChange={handleinputchange}
          />
        </div>

        <div className="registro-form-actions">
          <button
            type="button"
            onClick={handleGuardar}
            disabled={!habilitadoregistro}
            className="btn-guardar"
          >
            Guardar Registro
          </button>
        </div>
      </form>

      {mostrarconfirmacion && (
        <div className="registro-confirmacion">
          <p>¿Estás seguro de guardar este registro?</p>
          <div className="registro-confirmacion-actions">
            <button onClick={handleconfirmarguardado} className="btn-confirmar">
              Confirmar
            </button>
            <button onClick={handlecancelarguardado} className="btn-cancelar">
              Cancelar
            </button>
          </div>
        </div>
      )}

      {resultadoguardado && (
        <div className={resultadoguardado.ok ? "registro-exito" : "registro-error"}>
          <p>{resultadoguardado.mensaje}</p>
        </div>
      )}
    </div>
  );
}