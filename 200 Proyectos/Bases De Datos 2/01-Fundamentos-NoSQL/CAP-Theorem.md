# Teorema CAP

El **Teorema CAP** (también conocido como Teorema de Brewer) establece que es imposible para un sistema de datos distribuido garantizar simultáneamente más de dos de las siguientes tres propiedades:

### Propiedades CAP

1.  **Consistencia (Consistency):** Todos los nodos ven los mismos datos al mismo tiempo tras una escritura.
2.  **Disponibilidad (Availability):** Cada petición recibe una respuesta (éxito o fallo), sin garantía de que contenga la versión más reciente.
3.  **Tolerancia a Particiones (Partition Tolerance):** El sistema sigue funcionando a pesar de fallos en la comunicación entre nodos (particiones de red).

### El Dilema del Sistema Distribuido

En un entorno distribuido, las particiones de red son inevitables. Por tanto, el sistema debe elegir entre:

*   **CP (Consistencia y Tolerancia):** Se bloquea la respuesta hasta que los datos se sincronicen. Se sacrifica disponibilidad.
*   **AP (Disponibilidad y Tolerancia):** Se responde con los datos locales aunque no estén actualizados. Se sacrifica consistencia inmediata ([Propiedades BASE](ACID-vs-BASE.md)).

> [!IMPORTANT]
> No existe un sistema **CA** en redes distribuidas reales, ya que un fallo de red (P) obligaría a sacrificar C o A. El dilema entre consistencia fuerte ([ACID](ACID-vs-BASE.md)) y disponibilidad masiva se explica en la [Introducción a NoSQL](NoSQL-Introduction.md).
