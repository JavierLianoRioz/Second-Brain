# Ejercicio — Clasificación de Escenarios (SQL vs NoSQL)

> **🎯 Objetivo:** Desarrollar el criterio para elegir la tecnología de BD adecuada según el problema real.

## 🧠 Antes de mirar las respuestas

Para cada escenario, pregúntate:
1. ¿Los datos tienen **estructura fija** o cambiante?
2. ¿Necesito **transacciones ACID** (todo-o-nada)?
3. ¿El valor está en los **datos** o en las **relaciones** entre ellos?
4. ¿Cuál es la **escala** (miles, millones, billones de registros)?

---

## 📋 Escenarios

| # | Escenario | Contexto clave |
|---|-----------|---------------|
| 1 | **Universidad** | Gestión de matrículas y actas. Consistencia fuerte, transacciones seguras. |
| 2 | **Tokens de Sesión** | Almacenamiento temporal de preferencias. Acceso inmediato por ID. |
| 3 | **Sensores Industriales** | Millones de registros diarios. Análisis histórico y patrones globales. |
| 4 | **Gestor de Contenidos** | Artículos con campos variables y cambios frecuentes de modelo. |
| 5 | **Transferencias Bancarias** | Registro crítico. No se puede perder dinero bajo ningún concepto. |
| 6 | **Detección de Fraude** | Análisis de conexiones indirectas y caminos entre entidades. |
| 7 | **Similitud Semántica** | Buscador que encuentra documentos por significado, no por palabras clave. |

> [!TIP]
> Intenta clasificar cada escenario **antes** de ver la tabla de respuestas. Escribir tu razonamiento te ayuda a recordar.

---

## ✅ Respuestas y Justificación

| # | Tecnología | ¿Por qué? |
|---|-----------|-----------|
| 1 | **SQL (Relacional)** | Relaciones estables entre entidades (alumno ↔ matrícula ↔ asignatura). Necesita ACID. |
| 2 | **NoSQL (Clave-Valor)** | Solo necesita `GET/SET` por ID. Sin relaciones. Datos efímeros → Redis. |
| 3 | **NoSQL (Columnar)** | Lecturas analíticas masivas (promedios, tendencias). Escritura append-only → Cassandra. |
| 4 | **NoSQL (Documental)** | Cada artículo puede tener campos distintos. Esquema flexible → MongoDB. |
| 5 | **SQL (Relacional)** | Atomicidad obligatoria. Una transferencia afecta 2 cuentas → necesita transacción ACID. |
| 6 | **NoSQL (Grafos)** | El valor está en **recorrer conexiones** (¿quién conoce a quién?) → Neo4j. |
| 7 | **NoSQL (Vectorial)** | Búsqueda por proximidad matemática (embeddings) → Pinecone, Milvus. |

### 💡 Regla de oro para recordar

```
¿Datos tabulares + consistencia? → SQL
¿Velocidad por clave?            → Clave-Valor
¿Documentos flexibles?           → Documental  
¿Análisis masivo de columnas?    → Columnar
¿Relaciones complejas?           → Grafos
¿Similitud semántica?            → Vectorial
```

Este ejercicio ayuda a discernir cuándo aplicar NoSQL según la [Introducción a NoSQL](../01-Fundamentos-NoSQL/NoSQL-Introduction.md) y los diferentes [Tipos de NoSQL](../01-Fundamentos-NoSQL/NoSQL-Types-Overview.md) disponibles en el mercado.
