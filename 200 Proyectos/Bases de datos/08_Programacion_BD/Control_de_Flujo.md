---
tags: [concept, neuro-efficiency, db-programming]
moc: [[00_MOC_Programacion_BD]]
status: refactored
difficulty: intermediate
---

# Variables y Control de Flujo

---

## 🧠 Núcleo del Concepto
La programación en base de datos permite implementar lógica de negocio compleja directamente en el servidor, reduciendo el tráfico de red y mejorando la integridad.

*   **Variables:** Espacios de memoria temporales para almacenar cálculos intermedios (Locales con `DECLARE` o de Usuario con `@`).
*   **Decisión (IF):** Permite bifurcar la ejecución del código basándose en condiciones booleanas.
*   **Iteración (WHILE):** Automatiza tareas repetitivas mediante bucles controlados por una condición.

---

## 🗺️ Anclaje Visual (Dual Coding)
> [!abstract] Estructura de Decisión y Bucle
> ```mermaid
> graph TD
>     A[Inicio] --> B{¿Condición?}
>     B -- TRUE --> C[Acción Bucle]
>     C --> B
>     B -- FALSE --> D[Fin]
> ```

---

## 🔗 Conexiones y Contexto
*   **Se relaciona con:** [[Stored_Procedures_Sintaxis]] (donde se suele escribir este código) y [[Ejemplos_Programacion]] (aplicaciones prácticas).
*   **Diferencia clave con:** SQL Declarativo (SELECT/INSERT), que dice QUÉ hacer, mientras que el control de flujo dice CÓMO y en qué ORDEN.

---

## 💡 Aplicación Práctica: Poblado Masivo
> [!example] Generador de Datos
> ```sql
> WHILE i < total_objetivo DO
>     INSERT INTO tabla (columna) VALUES (CONCAT('dato_', i));
>     SET i = i + 1;
> END WHILE;
> ```

---

> [!tip] Idea Fuerza (Cierre)
> Las estructuras de control transforman una base de datos pasiva en un motor de reglas activo e inteligente.
