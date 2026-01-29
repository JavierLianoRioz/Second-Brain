# Arquitectura SGBD

La arquitectura de un [SGBD Definicion](SGBD_Definicion.md) define cómo procesa las consultas y gestiona los datos.

```mermaid
graph TD
    User[Usuario / Aplicación] -->|SQL| SGBD[Motor SGBD]
    subgraph SGBD_Internals [SGBD Internals]
        Parser[Analizador SQL]
        Optimizer[Optimizador de Consultas]
        Executor[Ejecutor]
    end
    SGBD --> SGBD_Internals
    SGBD_Internals -->|Lee/Escribe| DataFiles[(Archivos de Datos)]
    SGBD_Internals -->|Consulta| Dictionary[(Diccionario de Datos)]
```

## Componentes Clave
*   **Parser**: Verifica la sintaxis de la consulta.
*   **Optimizador**: Decide la mejor estrategia de ejecución (índices, orden de joins).
*   **Ejecutor**: Realiza las operaciones físicas sobre los datos.
*   **Diccionario de Datos**: Metadatos sobre la estructura de la BD (tablas, columnas, usuarios).

---
[00 MOC Introduccion](00_MOC_Introduccion.md)
