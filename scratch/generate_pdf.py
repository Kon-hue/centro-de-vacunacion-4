import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "Sistema Nacional de Vacunación (SISNAV) — Arquitectura y Desarrollo Frontend")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
            
        # Footer
        footer_text = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(558, 36, footer_text)
        self.drawString(54, 36, "Confidencial / Guía Técnica de Ingeniería Web")
        self.setStrokeColor(colors.HexColor("#e2e8f0"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)
        self.restoreState()

def build_pdf():
    pdf_path = r"c:\Users\cp932\OneDrive\Documents\proyecto-sistema-de-vacunacion\Guia_Frontend_Sistema_Vacunacion.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=colors.HexColor('#0f172a'),
        alignment=1, # Center
        spaceAfter=8
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0284c7'),
        alignment=1,
        spaceAfter=15
    )

    h1_style = ParagraphStyle(
        'Heading1Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor('#0369a1'),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'Heading2Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=10,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor('#334155'),
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletCustom',
        parent=body_style,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        'CodeSnippet',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor('#f8fafc'),
        backColor=colors.HexColor('#0f172a'),
        borderPadding=6,
        spaceBefore=5,
        spaceAfter=7
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor('#0c4a6e')
    )

    story = []

    # Title & Header
    story.append(Spacer(1, 10))
    story.append(Paragraph("SISTEMA NACIONAL DE VACUNACIÓN (SISNAV)", title_style))
    story.append(Paragraph("Guía Técnica Completa de Desarrollo Frontend en React", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0284c7"), spaceAfter=15))

    # Resumen Ejecutivo
    story.append(Paragraph("1. Objetivo y Alcance del Frontend", h1_style))
    story.append(Paragraph(
        "Un <b>Sistema de Vacunación Nacional</b> es una plataforma de salud pública de alto impacto. "
        "En esta etapa, el desarrollo se enfoca 100% en el <b>Frontend</b> (la interfaz con la que interactúan los ciudadanos y los médicos). "
        "El objetivo es construir una experiencia fluida, accesible y confiable antes de conectarla a microservicios o bases de datos externas.",
        body_style
    ))

    # Tabla de Módulos
    table_data = [
        [Paragraph("<b>Módulo</b>", body_style), Paragraph("<b>Usuario Destino</b>", body_style), Paragraph("<b>Funcionalidad Clave</b>", body_style)],
        [
            Paragraph("<b>Consulta de Carnet</b>", body_style),
            Paragraph("Ciudadano General", body_style),
            Paragraph("Búsqueda por DNI/Cédula, vista de historial de vacunas, estado de esquema y código QR simulado.", body_style)
        ],
        [
            Paragraph("<b>Registro de Dosis</b>", body_style),
            Paragraph("Enfermero / Vacunador", body_style),
            Paragraph("Formulario clínico rápido para ingresar lote, fecha, biológico, centro médico y emitir constancia.", body_style)
        ],
        [
            Paragraph("<b>Agendamiento de Citas</b>", body_style),
            Paragraph("Población Prioritaria", body_style),
            Paragraph("Reserva de turno seleccionando centro hospitalario más cercano, fecha y tipo de vacuna.", body_style)
        ],
        [
            Paragraph("<b>Tablero / Dashboard</b>", body_style),
            Paragraph("Autoridades / Epidemiología", body_style),
            Paragraph("Métricas visuales: Total de dosis suministradas, porcentaje de población vacunada y alertas de stock.", body_style)
        ],
    ]
    t = Table(table_data, colWidths=[120, 110, 274])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#f1f5f9')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#0f172a')),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))

    # Arquitectura de Archivos
    story.append(Paragraph("2. Estructura Limpia de Carpetas (Arquitectura Modular)", h1_style))
    story.append(Paragraph(
        "Para mantener el código profesional, desacoplado y fácil de mantener, organizamos la carpeta <code>src/</code> en capas claras:",
        body_style
    ))
    
    folder_tree = """src/
├── components/          # Piezas reutilizables de UI (Botones, Tarjetas, Navbar)
│   ├── Navbar.jsx       # Navegación superior con selector de módulos
│   ├── StatCard.jsx     # Tarjeta de KPI para el Dashboard nacional
│   └── CarnetCard.jsx   # Credencial digital estilizada para el ciudadano
├── views/               # Vistas o pantallas completas
│   ├── DashboardView.jsx# Métricas, cobertura y gráficos de progreso
│   ├── ConsultaView.jsx # Buscador por DNI y despliegue del carnet
│   ├── CitasView.jsx    # Solicitud de turno de vacunación
│   └── RegistroView.jsx # Módulo del profesional sanitario (registro de lote/dosis)
├── data/
│   └── initialData.js   # Catálogo oficial de vacunas, centros y mock de prueba
├── App.css              # Sistema de diseño, paleta médica y estilos responsivos
├── App.js               # Orquestador: enrutamiento de pestañas y estado global
└── index.js             # Punto de entrada de React"""
    story.append(Paragraph(folder_tree.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))

    story.append(PageBreak())

    # Paso a Paso del Código
    story.append(Paragraph("3. Modelado de Datos (src/data/initialData.js)", h1_style))
    story.append(Paragraph(
        "<b>¿Por qué hacemos esto primero?</b> En el desarrollo de software profesional, la interfaz responde a la forma que tienen los datos. "
        "Definir el catálogo de biológicos y los centros de salud nos permite conectar los selectores y tablas inmediatamente sin depender de un servidor.",
        body_style
    ))

    data_code = """// src/data/initialData.js
export const CATALOGO_VACUNAS = [
  { id: 'VAC-01', nombre: 'COVID-19 (Bivalente)', dosisRequeridas: 2, fabricante: 'Pfizer-BioNTech' },
  { id: 'VAC-02', nombre: 'Influenza Estacional', dosisRequeridas: 1, fabricante: 'Sanofi Pasteur' },
  { id: 'VAC-03', nombre: 'Hepatitis B Adulto', dosisRequeridas: 3, fabricante: 'GSK' },
  { id: 'VAC-04', nombre: 'Fiebre Amarilla', dosisRequeridas: 1, fabricante: 'Bio-Manguinhos' }
];

export const CENTROS_SALUD = [
  { id: 'CS-01', nombre: 'Hospital Central Metropolitano', municipio: 'Distrito Capital' },
  { id: 'CS-02', nombre: 'Centro Clínico Norte', municipio: 'Zona Norte' },
  { id: 'CS-03', nombre: 'Puesto Sanitario Comunitario Sur', municipio: 'Zona Sur' }
];

export const REGISTROS_INICIALES = [
  {
    id: 'REG-101',
    dni: '12345678',
    paciente: 'Carlos Eduardo Mendoza',
    vacunaId: 'VAC-01',
    vacunaNombre: 'COVID-19 (Bivalente)',
    dosisNumero: 1,
    fechaAplicacion: '2026-02-15',
    lote: 'PFZ-2026-A9',
    centroSalud: 'Hospital Central Metropolitano',
    vacunador: 'Lic. Laura Peña'
  }
];"""
    story.append(Paragraph(data_code.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))

    # Explicación del Código de Consulta
    story.append(Paragraph("4. Módulo de Consulta Ciudadana (src/views/ConsultaView.jsx)", h1_style))
    story.append(Paragraph(
        "Este componente implementa el buscador por DNI y el renderizado condicional del carnet digital. "
        "A continuación se explica el funcionamiento de cada bloque lógico:",
        body_style
    ))

    story.append(Paragraph("<b>A. Estados Locales (useState):</b>", h2_style))
    story.append(Paragraph(
        "• <code>busquedaDni</code>: Guarda el texto escrito por el usuario en la caja de búsqueda en tiempo real.<br/>"
        "• <code>historialEncontrado</code>: Almacena el arreglo de dosis que coincidieron con el DNI buscado.<br/>"
        "• <code>haBuscado</code>: Un interruptor booleano (true/false) para no mostrar mensajes de 'no encontrado' antes de que el usuario presione el botón.",
        bullet_style
    ))

    story.append(Paragraph("<b>B. Filtrado con Array.prototype.filter:</b>", h2_style))
    story.append(Paragraph(
        "Cuando el usuario envía el formulario con <code>handleBuscar</code>, ejecutamos: "
        "<code>const resultados = registros.filter(r =&gt; r.dni === busquedaDni.trim());</code>. "
        "Esto examina toda la lista sin mutar los datos originales y extrae solo las dosis del paciente.",
        body_style
    ))

    consulta_code = """// Fragmento clave de src/views/ConsultaView.jsx
const handleBuscar = (e) => {
  e.preventDefault(); // Evita que la página recargue el navegador
  const dniLimpio = busquedaDni.trim();
  if (!dniLimpio) return;

  const resultados = registros.filter(r => r.dni === dniLimpio);
  setHistorialEncontrado(resultados);
  setHaBuscado(true);
};"""
    story.append(Paragraph(consulta_code.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))

    story.append(PageBreak())

    # Explicación del Módulo de Registro
    story.append(Paragraph("5. Módulo del Vacunador (src/views/RegistroView.jsx)", h1_style))
    story.append(Paragraph(
        "El personal de salud requiere registrar la aplicación en pocos segundos. "
        "Para lograrlo de manera limpia en React, usamos un <b>formulario controlado único</b> con objeto de estado:",
        body_style
    ))

    reg_code = """// src/views/RegistroView.jsx
import React, { useState } from 'react';

export default function RegistroView({ catalogoVacunas, centrosSalud, onRegistrarDosis }) {
  // ¿POR QUÉ UN OBJETO?: Agrupar todos los campos en un solo objeto evita declarar 8 useStates distintos
  const [form, setForm] = useState({
    dni: '',
    paciente: '',
    vacunaId: catalogoVacunas[0]?.id || '',
    dosisNumero: 1,
    fechaAplicacion: new Date().toISOString().split('T')[0],
    lote: '',
    centroSalud: centrosSalud[0]?.nombre || '',
    vacunador: ''
  });

  const [notificacion, setNotificacion] = useState('');

  // ¿POR QUÉ EL MANEJADOR GENÉRICO?: [name] aprovecha el atributo 'name' del input para actualizar la clave exacta
  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const vacunaObj = catalogoVacunas.find(v => v.id === form.vacunaId);
    
    // Generamos un ID único simulado con timestamp
    const nuevoRegistro = {
      ...form,
      id: 'REG-' + Date.now(),
      vacunaNombre: vacunaObj ? vacunaObj.nombre : form.vacunaId,
      dosisNumero: Number(form.dosisNumero)
    };

    onRegistrarDosis(nuevoRegistro);
    setNotificacion('¡Dosis registrada y certificada en el sistema nacional!');
    
    // Reseteamos campos críticos
    setForm(prev => ({ ...prev, dni: '', paciente: '', lote: '' }));
    setTimeout(() => setNotificacion(''), 4000);
  };

  // ... Render del formulario (inputs con value={form.campo} y onChange={handleChange})
}"""
    story.append(Paragraph(reg_code.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))

    # Persistencia y Estado Global
    story.append(Paragraph("6. Orquestación y Persistencia (src/App.js)", h1_style))
    story.append(Paragraph(
        "<b>El problema habitual:</b> Cuando el usuario recarga la página (F5), las variables de memoria de React se borran.<br/>"
        "<b>La solución:</b> Sincronizar el estado con <code>localStorage</code> utilizando <code>useEffect</code>. "
        "De este modo, cualquier dosis que se registre o cita agendada se mantiene guardada en el navegador:",
        body_style
    ))

    app_code = """// Fragmento de App.js con persistencia automática
function App() {
  // 1. Lazy Initial State: Solo lee localStorage en el primer arranque
  const [registros, setRegistros] = useState(() => {
    const guardado = localStorage.getItem('SISNAV_REGISTROS');
    return guardado ? JSON.parse(guardado) : REGISTROS_INICIALES;
  });

  // 2. useEffect: Se activa automáticamente cada vez que el arreglo 'registros' cambia
  useEffect(() => {
    localStorage.setItem('SISNAV_REGISTROS', JSON.stringify(registros));
  }, [registros]);

  // 3. Función inmutable: crea un nuevo arreglo agregando el registro al inicio
  const handleRegistrarDosis = (nuevo) => {
    setRegistros(prev => [nuevo, ...prev]);
  };
  
  // ...
}"""
    story.append(Paragraph(app_code.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style))

    story.append(PageBreak())

    # Hoja de ruta para el usuario
    story.append(Paragraph("7. Plan de Ejecución Inmediata", h1_style))
    story.append(Paragraph(
        "Para implementar este sistema en tu proyecto actual paso a paso, sigue esta secuencia:",
        body_style
    ))

    pasos = [
        "<b>Paso 1:</b> Crear la carpeta <code>src/data/</code> y colocar el archivo <code>initialData.js</code> con las vacunas y centros.",
        "<b>Paso 2:</b> Crear <code>src/components/Navbar.jsx</code> para tener la barra institucional y poder alternar entre pantallas.",
        "<b>Paso 3:</b> Crear las vistas en <code>src/views/</code>: primero <code>ConsultaView.jsx</code> (búsqueda de carnet) y luego <code>RegistroView.jsx</code> (ingreso de vacunas).",
        "<b>Paso 4:</b> Actualizar <code>src/App.js</code> para conectar el estado de <code>registros</code> y la persistencia en <code>localStorage</code>.",
        "<b>Paso 5:</b> Aplicar estilos en <code>src/App.css</code> con colores institucionales limpios (azul médico, verde éxito, tipografía legible)."
    ]
    for p in pasos:
        story.append(Paragraph(p, bullet_style))

    story.append(Spacer(1, 15))

    # Box informativo final
    box_data = [[
        Paragraph(
            "<b>✅ Conclusión Técnica:</b> Con esta arquitectura frontend, el sistema es 100% interactivo, permite registrar personas, consultar carnets al instante con DNI y agendar citas. Cuando decidas integrar un Backend (Node.js, Python, Java o bases de datos como PostgreSQL/MongoDB), solo tendrás que reemplazar las llamadas a <code>localStorage</code> por peticiones <code>fetch()</code> o <code>axios</code>, sin tener que rediseñar ninguna pantalla.",
            callout_style
        )
    ]]
    box_table = Table(box_data, colWidths=[504])
    box_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#e0f2fe')),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#0284c7')),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
    ]))
    story.append(box_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado exitosamente en: {pdf_path}")

if __name__ == '__main__':
    build_pdf()
