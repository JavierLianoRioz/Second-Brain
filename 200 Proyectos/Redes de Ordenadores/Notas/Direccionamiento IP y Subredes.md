# Direccionamiento IP y Subredes

Organización jerárquica de las direcciones para facilitar el enrutamiento.

## CIDR (Classless Inter-Domain Routing)
Sustituyó al antiguo sistema de clases (A, B, C). Permite máscaras de longitud variable (**VLSM**).
- **Formato**: `IP/Prefijo` (ej. `192.168.1.0/24`).
## Máscara de Red
- *Analogía*: Un filtro que separa el código postal (Red) del número de casa (Host).
- **Subnetting (Subredes)**:
  - *Analogía*: Tienes un edificio entero (Red) y lo divides en pisos o departamentos (Subredes) para que el tráfico no se mezcle.
- **Dirección de Red**: Es el nombre de la calle (ej. Calle Mayor). No vive nadie ahí.
- **Dirección de Broadcast**: Un megáfono que oyen todos los vecinos de esa calle. (Todo unos en la parte de host).

## Agregación de Rutas (Summarization)
Permite anunciar múltiples redes contiguas como una sola (ej. `2.2.2.0/24` y `2.2.3.0/24` $\to$ `2.2.2.0/23`). Reduce el tamaño de las tablas de enrutamiento.

---
**Relacionado**: [[Ejercicios - Interconexión de Redes]]
**Fuente**: [[52_Tema5.pdf]]
