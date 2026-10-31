export const catalogo_vacunas = [
  { id: 'VAC-01', nombre: 'COVID-19 (Bivalente)', dosisRequeridas: 2, fabricante: 'Pfizer-BioNTech' },
  { id: 'VAC-02', nombre: 'Influenza Estacional', dosisRequeridas: 1, fabricante: 'Sanofi Pasteur' },
  { id: 'VAC-03', nombre: 'Hepatitis B Adulto', dosisRequeridas: 3, fabricante: 'GSK' },
  { id: 'VAC-04', nombre: 'Fiebre Amarilla', dosisRequeridas: 1, fabricante: 'Bio-Manguinhos' }
];
export const centros_salud = [
  { id: 'CS-01', nombre: 'Policlínica San Juan S.A.', municipio: 'Maracaibo' },
  { id: 'CS-02', nombre: 'Clínica Bella Vista', municipio: 'Maracaibo' },
  { id: 'CS-03', nombre: 'Hospital Coromoto', municipio: 'Maracaibo' }
];
export const registros_iniciales = [
  {
    id: 'REG-101',
    dni: '12345678',
    paciente: 'Carlos Eduardo Mendoza',
    vacunaId: 'VAC-01',
    vacunaNombre: 'COVID-19 (Bivalente)',
    dosisNumero: 1,
    fechaAplicacion: '2026-02-15',
    lote: 'PFZ-2026-A9',
    centroSalud: 'Policlínica San Juan S.A.',
    vacunador: 'Lic. Laura Peña'
  }
];