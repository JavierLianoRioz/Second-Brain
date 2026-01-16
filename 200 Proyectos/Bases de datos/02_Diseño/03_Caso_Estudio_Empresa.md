---
tags: [exercise, case-study, db-design]
topic: [[00_MOC_Diseño]]
level: intermediate
time_estimate: 20 min
---

# Caso de Estudio: Empresa de Servicios

## 📝 Escenario y Datos
> [!info] Requerimientos del Negocio (Proximidad)
> Una empresa de servicios necesita gestionar sus contratos con las siguientes reglas:
> *   **Clientes**: Pueden ser Personas o Empresas. Contratan uno o varios servicios mediante un contrato.
> *   **Servicios**: Tienen tipos y precios específicos.
> *   **Contratos**: Tienen fecha de inicio y fin. Relacionan un cliente con múltiples servicios.
> *   **Empleados**: Atienden los contratos. Pueden ser Técnicos o Administrativos.

---

## 🚀 El Reto
Diseña el **Modelo Entidad-Relación (ER)** y transfórmalo al **Modelo Relacional** final, asegurando que se gestionen correctamente las jerarquías de Clientes y Empleados, así como la relación N:M entre Contratos y Servicios.

---

## 💡 Solución (Andamiaje)
> [!success]- Mostrar Solución Paso a Paso
> ### Fase 1: Identificación de Entidades y Jerarquías
> *   **Jerarquías**: `Cliente` (Persona/Empresa) y `Empleado` (Técnico/Administrativo).
> *   **N:M**: `Contrato` y `Servicio` (Un contrato incluye varios servicios).
> 
> ### Fase 2: Diagrama ER
> ```mermaid
> erDiagram
>     CLIENTE ||--o{ CONTRATO : "firma"
>     EMPLEADO ||--o{ CONTRATO : "atiende"
>     CONTRATO }o--o{ SERVICIO : "incluye"
>     CLIENTE ||--|| PERSONA : "es"
>     CLIENTE ||--|| EMPRESA : "es"
> ```
> 
> ### Fase 3: Modelo Relacional (Tablas)
> 1.  **CLIENTE**: `id_cliente (PK)`, `direccion`, `telefono`, `tipo_cliente`, `dni_cif`. (Estrategia de Tabla Única para la jerarquía).
> 2.  **CONTRATO**: `id_contrato (PK)`, `fecha_inicio`, `fecha_fin`, `id_cliente (FK)`, `id_empleado (FK)`.
> 3.  **DETALLE_CONTRATO**: `id_contrato (FK)`, `id_servicio (FK)`, `cantidad`. (Resuelve N:M).

