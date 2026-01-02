# Las 12 Reglas de Codd

Edgar F. Codd definió estas reglas en 1985 para determinar si un [[SGBD_Definicion]] es verdaderamente **Relacional**.

> [!IMPORTANT]
> **Regla 0 (Fundacional)**: El sistema debe gestionar la base de datos **exclusivamente** a través de sus capacidades relacionales.

## Reglas Principales
1.  **Información**: Todo dato debe representarse como un valor en una tabla.
2.  **Acceso Garantizado**: Todo dato es accesible mediante `NombreTabla + ClavePrimaria + NombreColumna`.
3.  **Tratamiento de Nulos**: El sistema debe soportar el valor `NULL` sistemáticamente.
4.  **Catálogo Dinámico**: La estructura de la BD se almacena en tablas del sistema.
5.  **Sublenguaje Completo**: Debe existir un lenguaje (como SQL) para todo (DDL, DML, seguridad).
6.  **Actualización de Vistas**: Las vistas actualizables deben ser gestionadas por el sistema.
7.  **Operaciones de Alto Nivel**: Insert, Update, Delete sobre conjuntos de registros.
8.  **Independencia Física**: Cambios en almacenamiento no afectan aplicaciones.
9.  **Independencia Lógica**: Cambios en esquema no afectan aplicaciones.
10. **Independencia de Integridad**: Restricciones definidas en la BD, no en la app.
11. **Independencia de Distribución**: Transparencia de ubicación de datos.
12. **No Subversión**: No saltarse la integridad por vías de bajo nivel.

---
[[00_MOC_Introduccion]]
