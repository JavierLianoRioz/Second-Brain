---
materia: Ingeniería de Software
---
# Complejidad del Software

El desarrollo de software es considerado por muchos —como Frederick Brooks— como el trabajo más complejo que jamás haya emprendido la humanidad. Esta complejidad no es accidental, sino inherente a la naturaleza del software, donde un sistema mediano puede contener cientos de miles de líneas de código y miles de entidades interconectadas.

---

## ¿Qué hace que un sistema sea intrínsecamente complejo?
Un sistema de software no es solo código; es un conjunto de clases, módulos y paquetes que se relacionan mediante herencia, composición y paso de mensajes. Según Grady Booch, los sistemas complejos comparten características fundamentales que definen su estructura y comportamiento:

### ¿Cuáles son las leyes que rigen la estructura del software?
- **Estructura Jerárquica**: Los sistemas se componen de subsistemas interrelacionados, que a su vez se dividen hasta alcanzar [[Elementos Primitivos]].
- **Separación de Asuntos**: Las conexiones internas de un componente son más fuertes que sus conexiones con el exterior —cohesión frente a acoplamiento—.
- **Patrones Comunes**: Existen mecanismos compartidos que unifican la jerarquía del sistema.
- **Evolución desde lo Simple**: ==Un sistema complejo que funciona siempre ha evolucionado a partir de un sistema sencillo que funcionaba== (Ley de Gall).

### ¿Qué herramientas conceptuales nos permiten vencer la entropía?
Para gestionar esta complejidad, la ingeniería de software se apoya en cuatro pilares conceptuales que actúan como defensas ante el caos:

1.  **Abstracción**: Proceso de extraer las características esenciales de un objeto ignorando los detalles superfluos. Proporciona límites conceptuales claros.
2.  **Encapsulación**: Oculta los detalles de implementación de una abstracción. Permite cambiar el "cómo" sin afectar a quienes usan el "qué" —la interfaz—.
3.  **Modularidad**: Descomposición de un sistema en piezas poco acopladas y muy cohesivas. Permite entender y refinar partes del sistema de forma independiente (*divide et impera*).
4.  **Jerarquía**: Ordenamiento de las abstracciones, ya sea por clasificación (herencia) o por composición.

**La regla de oro:** ==El principal enemigo de la fiabilidad y la calidad del software es la complejidad. Todo aquello que no sea necesario dar a conocer, **no se debe dar a conocer**.==

---

## ¿Cómo podemos dimensionar el reto al que nos enfrentamos?
Para entender la magnitud de lo que construimos, resulta útil comparar un proyecto de software mediano con hitos de la creación humana en otros ámbitos —como la literatura clásica—.

### ¿Es el software más complejo que la literatura clásica?

| Métrica | Don Quijote | Proyecto Software (Mediano) |
| :--- | :--- | :--- |
| **Extensión** | ~300.000 palabras | ~100.000 líneas (~300.000 palabras) |
| **Entidades** | Decenas (personajes) | Centenares (identificadores/clases) |
| **Autoría** | 1 autor (Cervantes) | Equipo de 6-8 personas |
| **Interconectividad** | Lineal/Narrativa | Alta (grafos de dependencias) |
| **Coste/Ámbito** | "Gratis" / Personal | Miles de € / Definido por terceros |

**Conclusión:** El software de una aplicación media excede con creces la capacidad intelectual humana individual.

## Referencias
1. **Mmasias**. *idsw2: Temario de la asignatura de Ingeniería de Software II*. [GitHub Repository](https://github.com/mmasias/idsw2) y en copia local: [[500 Biblioteca/idsw2/temario/00-introduccion/software.md|Software y Complejidad]].
ario de la asignatura de Ingeniería de Software II*. [GitHub Repository](https://github.com/mmasias/idsw2) y en copia local: [[500 Biblioteca/idsw2/temario/00-introduccion/software.md|Software y Complejidad]].
