# Normalización: Objetivos

La **Normalización** es el proceso de organizar los datos para reducir la **redundancia** y mejorar la **integridad**.

## Objetivos Principales
1.  **Eliminar Redundancia**: Guardar cada dato una sola vez.
2.  **Evitar Anomalías**:
    *   **Inserción**: No poder insertar datos por falta de otros.
    *   **Actualización**: Tener que actualizar múltiples filas para un solo cambio.
    *   **Borrado**: Perder información no deseada al borrar una fila.

## Proceso
Se aplican reglas sucesivas llamadas **Formas Normales** ([[Primera_Forma_Normal_1FN]], [[Segunda_Forma_Normal_2FN]], etc.).


## Contexto en el Diseño
La normalización es una parte crítica de la **Fase Lógica** en las [[Fases_del_Diseño_BD]]. Se aplica después de transformar el [[Modelo_Entidad_Relacion]] al [[Modelo_Relacional_Conceptos]].

---
[[00_MOC_Normalizacion]]
