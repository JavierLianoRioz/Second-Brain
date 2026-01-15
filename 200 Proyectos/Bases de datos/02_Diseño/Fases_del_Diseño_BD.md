# Fases del Diseño de Bases de Datos

El diseño de una base de datos es un proceso estructurado que permite transformar los requerimientos de información en un esquema funcional.

## Las 4 Fases

```mermaid
graph LR
    Req[Requerimientos] --> Conc[Diseño Conceptual]
    Conc --> Log[Diseño Lógico]
    Log --> Fis[Diseño Físico]
```

1.  **Recolección y Análisis de Requerimientos**: Entender qué datos necesita el sistema.
2.  **Diseño Conceptual**: Crear un esquema independiente del SGBD. Herramienta principal: [Modelo Entidad Relacion](Modelo_Entidad_Relacion.md).
3.  **Diseño Lógico**: Transformar el esquema conceptual a un modelo de datos específico. Herramienta principal: [Modelo Relacional Conceptos](Modelo_Relacional_Conceptos.md).
4.  **Diseño Físico**: Implementar el esquema en un [SGBD Definicion](../01_Introduccion/SGBD_Definicion.md) concreto (MySQL, Oracle).

---
[00 MOC Diseño](00_MOC_Dise%C3%B1o.md)
