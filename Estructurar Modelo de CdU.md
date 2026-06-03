---
materia: Ingeniería de Software
---
# Estructurar Modelo de CdU

Estructurar el modelo consiste en refinar los casos de uso identificados para reducir la redundancia y mejorar la organización del sistema mediante relaciones de reutilización.

---

## ¿Cómo organizamos el modelo para evitar que colapse bajo su propia repetición?
A medida que el sistema crece, es común encontrar comportamientos que se repiten en múltiples funcionalidades. La estructuración nos permite gestionar esa complejidad.

### ¿En qué se diferencian las piezas concretas de las abstractas?
- **Casos de Uso Concretos**: Son aquellos iniciados directamente por un actor. Representan una secuencia completa y autónoma de acciones con valor.
- **Casos de Uso Abstractos**: No pueden ejecutarse por sí solos. Existen únicamente para encapsular lógica que será reutilizada por otros CdU.

### ¿Qué mecanismos de conexión permiten la reutilización de lógica?
Existen tres formas fundamentales de conectar los Casos de Uso para optimizar el modelo:

1.  **Inclusión (Include)**: Una relación obligatoria. El CdU base **necesita** el comportamiento del incluido para completarse (ej. "Realizar Compra" siempre incluye "Validar Stock").
2.  **Extensión (Extend)**: Una relación opcional y condicional. El CdU base **puede** sumar el comportamiento del extendido solo si se cumple una condición (ej. "Realizar Pedido" se extiende con "Aplicar Descuento" solo si el cupón es válido).
3.  **Generalización**: Relación de herencia donde un CdU "hijo" especializa el comportamiento de un "padre" (ej. "Pagar" es el padre de "Pagar con Cripto").

---

## ¿Cuándo es el momento adecuado para refactorizar el modelo?
La estructuración es una herramienta poderosa, pero su uso prematuro puede oscurecer el entendimiento del negocio.

### ¿Cómo decidimos el nivel de granularidad y abstracción necesario?
¡OJO! No estructures demasiado pronto. Primero identifica los casos de uso reales del negocio desde el punto de vista del usuario. La estructuración es una técnica de **refactorización** posterior que busca:
- Evitar la duplicidad de texto en las especificaciones.
- Manejar la complejidad de flujos opcionales que harían el flujo principal ilegible.

```mermaid
useCaseDiagram
    usecase "Realizar Compra" as UC1
    usecase "Validar Usuario" as UC2
    usecase "Enviar Notificación SMS" as UC3
    usecase "Realizar Pago con Tarjeta" as UC4
    usecase "Realizar Pago" as UC5
    
    UC1 ..> UC2 : <<include>>
    UC3 ..> UC1 : <<extend>>
    UC4 --|> UC5 : generalización
```

### ¿En qué se distinguen las distintas formas de asociación?

| Relación | ¿Es obligatoria? | ¿Quién conoce a quién? |
| :--- | :--- | :--- |
| **Inclusión** | Sí | El caso base conoce al caso incluido. |
| **Extensión** | No (Condicional) | El caso extendido conoce al caso base —mediante el punto de extensión—. |
| **Generalización** | Sí (Herencia) | El hijo conoce al padre. |

---

## Referencias
1. **Mmasias**. *idsw1: Temario de la asignatura de Ingeniería de Software*. [GitHub](https://github.com/mmasias/idsw1) / [[500 Biblioteca/idsw1/README.md|Copia Local]].
