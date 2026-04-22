# Sharding (Fragmentación Horizontal)

El **Sharding** es un método de distribución de datos a través de varios servidores (nodos) para permitir el escalado horizontal de una base de datos.

### Concepto Atómico
En lugar de escalar verticalmente aumentando los recursos de un solo servidor, el sharding divide una base de datos grande en partes más pequeñas y manejables llamadas **shards**. Cada shard se almacena en una instancia de servidor independiente.

### ¿Cómo funciona?
Los datos se distribuyen basándose en una **Shard Key** (clave de partición). Por ejemplo, si usamos el `ID_Usuario`:
*   Servidor 1: Usuarios con ID $1$ a $10,000$.
*   Servidor 2: Usuarios con ID $10,001$ a $20,000$.

### Ventajas
1.  **Escalabilidad casi ilimitada:** Permite manejar volúmenes de datos que no caben en un solo disco.
2.  **Rendimiento mejorado:** Las consultas se distribuyen entre múltiples CPUs y memorias.
3.  **Alta disponibilidad:** Si un shard falla, el resto del sistema puede seguir funcionando.

### Desafíos
*   **Complejidad:** Requiere lógica adicional para saber en qué nodo está cada dato.
*   **Joins entre shards:** Son extremadamente costosos y generalmente se evitan.
*   **Desequilibrio (Hotspots):** Una mala elección de la *shard key* puede saturar un servidor mientras otros están ociosos.

---
**Enlaces Relacionados:**
*   [Introducción a NoSQL](NoSQL-Introduction.md)
