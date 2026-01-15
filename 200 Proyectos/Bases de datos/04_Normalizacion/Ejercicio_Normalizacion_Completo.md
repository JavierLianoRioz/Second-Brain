# Ejercicio Práctico: Normalización Completa (De UNF a 3FN)

## Escenario: Taller Mecánico
Tenemos una hoja de cálculo donde registramos las reparaciones de vehículos. Contiene datos redundantes y grupos repetitivos.

**Tabla Original (No Normalizada - UNF)**
`REPARACIONES (NumOrden, Fecha, ID_Cliente, NombreCliente, CiudadCliente, Matricula, Marca, Modelo, {ID_Repuesto, DescripcionRepuesto, Cantidad, PrecioUnitario})`

*   **Nota:** Lo que está entre `{}` es un grupo repetitivo (varios repuestos por orden).
*   **Datos de ejemplo:**
    *   Orden 100: Cliente Juan (Madrid), Coche Ford Fiesta. Repuestos: Aceite (20€), Filtro (10€).
    *   Orden 101: Cliente Ana (Valencia), Coche Seat Ibiza. Repuestos: Rueda (50€).

---

## Paso 1: Primera Forma Normal (1FN)
**Objetivo:** Eliminar grupos repetitivos.
**Acción:** Creamos una fila por cada repuesto, repitiendo los datos de la cabecera (Orden, Cliente, Coche). Elegimos una Clave Primaria (PK) compuesta.

**Tabla Resultante (1FN)**
`REPARACIONES_1FN (NumOrden, ID_Repuesto, Fecha, ID_Cliente, NombreCliente, CiudadCliente, Matricula, Marca, Modelo, DescripcionRepuesto, Cantidad, PrecioUnitario)`
*   **PK:** `(NumOrden, ID_Repuesto)`

---

## Paso 2: Segunda Forma Normal (2FN)
**Objetivo:** Eliminar Dependencias Parciales.
**Análisis:**
*   La PK es `(NumOrden, ID_Repuesto)`.
*   ¿Qué depende SOLO de `NumOrden`? -> Fecha, Cliente, Coche.
*   ¿Qué depende SOLO de `ID_Repuesto`? -> DescripcionRepuesto, PrecioUnitario.
*   ¿Qué depende de AMBOS? -> Cantidad (la cantidad de ESE repuesto en ESA orden).

**Acción:** Separamos en tres tablas.

**Tabla A: ORDENES (Datos de la cabecera)**
`ORDENES (NumOrden, Fecha, ID_Cliente, NombreCliente, CiudadCliente, Matricula, Marca, Modelo)`
*   **PK:** `NumOrden`

**Tabla B: REPUESTOS (Catálogo)**
`REPUESTOS (ID_Repuesto, DescripcionRepuesto, PrecioUnitario)`
*   **PK:** `ID_Repuesto`

**Tabla C: DETALLE_ORDEN (La relación)**
`DETALLE_ORDEN (NumOrden, ID_Repuesto, Cantidad)`
*   **PK:** `(NumOrden, ID_Repuesto)`
*   **FK:** `NumOrden` -> ORDENES, `ID_Repuesto` -> REPUESTOS

---

## Paso 3: Tercera Forma Normal (3FN)
**Objetivo:** Eliminar Dependencias Transitivas.
**Análisis:**
Miramos la tabla `ORDENES` que creamos en el paso anterior:
`ORDENES (NumOrden, Fecha, ID_Cliente, NombreCliente, CiudadCliente, Matricula, Marca, Modelo)`

*   **Dependencia Transitiva 1 (Cliente):**
    `NumOrden -> ID_Cliente -> (NombreCliente, CiudadCliente)`
    Los datos del cliente dependen del ID del cliente, no de la orden directamente.
*   **Dependencia Transitiva 2 (Vehículo):**
    `NumOrden -> Matricula -> (Marca, Modelo)`
    Los datos del coche dependen de la matrícula.

**Acción:** Extraemos Clientes y Vehículos a sus propias tablas.

**Tabla 1: CLIENTES**
`CLIENTES (ID_Cliente, NombreCliente, CiudadCliente)`
*   **PK:** `ID_Cliente`

**Tabla 2: VEHICULOS**
`VEHICULOS (Matricula, Marca, Modelo)`
*   **PK:** `Matricula`

**Tabla 3: ORDENES (Refinada)**
`ORDENES (NumOrden, Fecha, ID_Cliente, Matricula)`
*   **PK:** `NumOrden`
*   **FK:** `ID_Cliente` -> CLIENTES, `Matricula` -> VEHICULOS

---

## Resultado Final (Esquema Normalizado)

1.  **CLIENTES** `(ID_Cliente, Nombre, Ciudad)`
2.  **VEHICULOS** `(Matricula, Marca, Modelo)`
3.  **REPUESTOS** `(ID_Repuesto, Descripcion, Precio)`
4.  **ORDENES** `(NumOrden, Fecha, #ID_Cliente, #Matricula)`
5.  **DETALLES_ORDEN** `(#NumOrden, #ID_Repuesto, Cantidad)`

Este diseño elimina redundancias (si Juan cambia de ciudad, solo toco la tabla CLIENTES) y anomalías.

---
[00 MOC Normalizacion](00_MOC_Normalizacion.md)
