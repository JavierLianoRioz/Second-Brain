# Normalización: Objetivos

La **Normalización** es el proceso de organizar los datos para reducir la **redundancia** y mejorar la **integridad**.

## Objetivos Principales
1.  **Eliminar Redundancia**: Guardar cada dato una sola vez.
2.  **Evitar Anomalías**:
    *   **Inserción**: No poder insertar datos por falta de otros.
    *   **Actualización**: Tener que actualizar múltiples filas para un solo cambio.
    *   **Borrado**: Perder información no deseada al borrar una fila.

## Proceso
Se aplican reglas sucesivas llamadas **Formas Normales** ([Primera Forma Normal 1FN](Primera_Forma_Normal_1FN.md), [Segunda Forma Normal 2FN](Segunda_Forma_Normal_2FN.md), etc.).


## Contexto en el Diseño
La normalización es una parte crítica de la **Fase Lógica** en las [Fases del Diseño BD](../02_Dise%C3%B1o/Fases_del_Dise%C3%B1o_BD.md). Se aplica después de transformar el [Modelo Entidad Relacion](../02_Dise%C3%B1o/Modelo_Entidad_Relacion.md) al [Modelo Relacional Conceptos](../02_Dise%C3%B1o/Modelo_Relacional_Conceptos.md).

---
[00 MOC Normalizacion](00_MOC_Normalizacion.md)
