# Conceptos de Enrutamiento

El enrutamiento es el proceso de construir tablas de rutas para que los paquetes lleguen a su destino.

## Tipos de Enrutamiento
- **Estático**: Configurado manualmente por el administrador. Simple pero no escala ni tolera fallos.
- **Dinámico**: Los routers se intercambian información mediante protocolos para adaptarse a cambios.

## Algoritmos Dinámicos
1. **Vector-Distancia (ej. RIP)**:
   - *Analogía*: Conducir siguiendo señales en cada cruce que dicen "Madrid -> 50km". No tienes un mapa, solo sabes lo que te dice el poste. Si el poste miente, te pierdes.
2. **Estado del Enlace (ej. OSPF)**:
   - *Analogía*: Usar Google Maps. Tienes el mapa completo de todas las carreteras y calculas tú mismo la mejor ruta. Es mucho más fiable pero consume más batería (procesador).

## Clasificación por Ámbito
- **IGP (Interior Gateway Protocol)**: Dentro de un mismo Sistema Autónomo (AS). Ej: RIP, OSPF.
- **EGP (Exterior Gateway Protocol)**: Entre diferentes AS. Ej: BGP (el protocolo de Internet).

---
**Relacionado**: [[Principios de la Capa de Red]]
**Fuente**: [[52_Tema5.pdf]]
