---
tags: [concept, neuro-efficiency, normalization]
moc: "[00_MOC_Normalizacion](00_MOC_Normalizacion.md)"
status: refined
difficulty: easy
---

# Normalización: Objetivos

---

## 🧠 Núcleo del Concepto

La **Normalización** es el proceso técnico de organizar las columnas y tablas de una base de datos relacional para minimizar la redundancia y maximizar la integridad de los datos.

*   **Eliminar Redundancia**: Evitar que el mismo dato se guarde en múltiples lugares, ahorrando espacio y evitando inconsistencias.
*   **Mitigar Anomalías**: Prevenir errores lors de la inserción, actualización o borrado de datos que podrían causar pérdida de información o estados inconsistentes.
*   **Estructura Lógica**: Transforma un diseño plano o ineficiente en un conjunto de tablas vinculadas por claves.

---

## 🗺️ Anclaje Visual (Dual Coding)

> [!abstract] El Proceso de Refinado
>
> ```mermaid
> graph LR
>     R[Datos Brutos / Redundantes] --> N{Normalización}
>     N --> T1[Tabla A]
>     N --> T2[Tabla B]
>     T1 --- T2
>     
>     style N fill:#f9f,stroke:#333
> ```

---

## 🔗 Conexiones y Contexto

*   **Ubicación**: Se aplica en la **Fase Lógica** del diseño ([Fases del Diseño BD](../02_Dise%C3%B1o/Fases_del_Dise%C3%B1o_BD.md)).
*   **Predecesor**: Transformación del [Modelo Entidad Relacion](../02_Dise%C3%B1o/Modelo_Entidad_Relacion.md).
*   **Herramientas**: Se basa en el estudio de las [Dependencia Funcional](Dependencia_Funcional.md).

---

> [!tip] Idea Fuerza (Cierre)
> La normalización es el arte de "dividir para vencer": separamos los conceptos para que cada dato tenga un único hogar verdadero.

---

## 🗺️ Mapa de Contenido
*   Volver a: [00 MOC Normalización](00_MOC_Normalizacion.md).
