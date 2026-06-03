---
materia: Ingeniería de Software
---
# Principios de Diseño OO (SOLID)

Los principios **SOLID** son un conjunto de cinco reglas de diseño orientado a objetos que, aplicadas en conjunto, permiten crear sistemas más fáciles de mantener, escalar y entender. Son la base fundamental para combatir la rigidez y la fragilidad del software.

---

## ¿Qué pilares sostienen un diseño orientado a objetos profesional?
En el desarrollo de software, el cambio es la única constante. Los principios SOLID actúan como un escudo contra el caos que genera el crecimiento descontrolado del código.

### ¿De qué manera estas cinco reglas combaten la rigidez del software?
1.  **SRP: Responsabilidad Única** (Single Responsibility)
    - *Concepto:* Una clase debe tener una sola razón para cambiar —debe servir a un único actor—.
    - *Ejemplo (Biblioteca):* Una clase `Biblioteca` que busca libros, los presta y genera reportes rompe el SRP. Debe dividirse en `BuscadorDeLibros`, `GestorDePrestamos` y `GeneradorDeReportes`.
    - *Ejemplo (Empleado):* Separar la información personal del `Empleado` de la lógica de `CalculadoraSalario` evita que cambios en la política de bonos afecten al modelo de datos del empleado.

---

## ¿Cómo elegimos la estructura de relación adecuada?
La decisión entre herencia y composición marca la diferencia entre un sistema flexible y uno rígido.

### Herencia vs. Composición: ¿Cuándo usar cada una?

- **Herencia (Es-un)**: Ideal para jerarquías de clasificación puras donde el comportamiento se comparte y extiende de forma natural.
    - *Ejemplo:* Una jerarquía `Shape` -> `Circle`, `Rectangle`. Todos son formas y comparten `getArea()`. La herencia simplifica la reutilización.
- **Composición (Tiene-un)**: Preferible cuando queremos combinar comportamientos de forma dinámica y evitar la explosión de clases.
    - *Ejemplo:* Un `Vehículo` que tiene un `Engine` y una `Transmission`. Usar herencia para cada combinación (GasolinaManual, EléctricoAutomático) crearía una jerarquía inmanejable. La composición permite intercambiar motores y transmisiones en tiempo de ejecución.
    - *Ventaja:* Desacopla la lógica, permite cambios dinámicos y evita que los cambios en la clase base rompan colateralmente a las hijas (fragilidad).

### Doble Despacho (Double Dispatch)
Es una técnica para eliminar el uso de `instanceof` en jerarquías donde el comportamiento depende de dos tipos de objetos. Se basa en el **Patrón Visitor**:

1.  **Primer Despacho**: El objeto llama a `aceptar(visitante)`. Java resuelve el método según el tipo concreto del objeto (polimorfismo).
2.  **Segundo Despacho**: Dentro de `aceptar`, el objeto llama a `visitante.visitar(this)`. Como `this` es el tipo concreto, se resuelve la sobrecarga adecuada en el visitante.

*Compromiso:* El doble despacho desplaza la rigidez. Es fácil añadir nuevos visitantes (operaciones), pero es difícil añadir nuevos elementos a la jerarquía, ya que obliga a modificar todos los visitantes.

---

2.  **OCP: Abierto/Cerrado** (Open/Closed)
    - *Concepto:* El software debe estar **abierto para la extensión**, pero **cerrado para la modificación**.
    - *Solución:* Añade nuevas funcionalidades (ej. un nuevo tipo de descuento) creando código nuevo en lugar de alterar el que ya funciona.

3.  **LSP: Sustitución de Liskov** (Liskov Substitution)
    - *Concepto:* Las clases derivadas deben poder sustituir a sus clases base sin alterar el comportamiento esperado.
    - *Solución:* Garantiza que el polimorfismo sea seguro y predecible (evitando excepciones inesperadas en subclases).

4.  **ISP: Segregación de Interfaces** (Interface Segregation)
    - *Concepto:* Los clientes no deben ser forzados a depender de interfaces que no utilizan.
    - *Solución:* Prefiere muchas interfaces pequeñas y específicas antes que una "interfaz gorda" que obligue a implementar métodos vacíos.

5.  **DIP: Inversión de Dependencias** (Dependency Inversion)
    - *Concepto:* Depende de abstracciones (interfaces), no de implementaciones concretas.
    - *Solución:* Desacopla la lógica de negocio (alto nivel) de los detalles técnicos como la base de datos o la UI (bajo nivel).

**La regla de oro:** Estos principios no son leyes absolutas, sino guías pedagógicas. Su abuso puede llevar a una sobreingeniería innecesaria; aplícalos solo cuando la complejidad lo justifique.

---

## ¿Cómo aplicamos estos principios sin caer en la sobreingeniería?
La clave de SOLID no es seguirlos ciegamente, sino entender cómo se refuerzan mutuamente para mejorar el sistema.

### ¿Cómo interactúan los principios para crear una arquitectura robusta?
La aplicación de estos principios suele generar un efecto dominó positivo:
- Aplicar **ISP** crea interfaces pequeñas y específicas.
- Esto facilita enormemente la **DIP**, ya que dependemos de abstracciones estables.
- Al depender de abstracciones, el sistema se vuelve conforme a **OCP**, permitiendo extensiones sin tocar el núcleo probado.

### ¿Qué preguntas debemos hacernos para comprobar la salud de nuestro diseño?
- **Pregunta por los Actores (SRP):** ¿Quién podría pedir un cambio en esta clase? ¿Varios departamentos distintos? Si es así, divídela.
- **Evita el "instanceof" (LSP):** Si tienes que preguntar qué tipo de objeto es antes de actuar, tu diseño está rompiendo la sustituibilidad.
- **Inyecta, no Instancies (DIP):** ¿Estás usando `new` dentro de tu lógica de negocio para crear servicios? Deja que te los pasen por el constructor.

---

## Referencias
1. **Mmasias**. *idsw2: Diseño Orientado a Objetos*. [GitHub Repository](https://github.com/mmasias/idsw2) y en copia local: [[500 Biblioteca/idsw2/temario/03-diseñoOO/README.md|Temario Diseño OO]].
