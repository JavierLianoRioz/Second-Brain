# Direccionamiento IP y Subredes

Organización jerárquica de las direcciones para facilitar el enrutamiento.

## CIDR (Classless Inter-Domain Routing)
Sustituyó al antiguo sistema de clases (A, B, C). Permite máscaras de longitud variable (**VLSM**).
- **Formato**: `IP/Prefijo` (ej. `192.168.1.0/24`).
## Máscara de Red
- *Analogía*: Un filtro que separa el código postal (Red) del número de casa (Host).
- **Subnetting (Subredes)**:
  - *Analogía*: Tienes un edificio entero (Red) y lo divides en pisos o departamentos (Subredes) para que el tráfico no se mezcle.
- **Dirección de Red**: Es el nombre de la calle (ej. Calle Mayor). No vive nadie ahí. (Todo ceros en la parte de host).
- **Dirección de Broadcast**: Un megáfono que oyen todos los vecinos de esa calle. (Todo unos en la parte de host).

> [!IMPORTANT]
> **La Regla del +2**: Al calcular el número de IPs necesarias para dispositivos, siempre tenemos que sumar **2** al número de hosts deseados ($N+2$) porque estas dos direcciones (Red y Broadcast) están reservadas y **no se pueden asignar a ningún ordenador**.

## Agregación de Rutas (Summarization)
Permite anunciar múltiples redes contiguas como una sola (ej. `2.2.2.0/24` y `2.2.3.0/24` $\to$ `2.2.2.0/23`). Reduce el tamaño de las tablas de enrutamiento.

## La Receta VLSM (Corte de Tarta)
Para ejercicios donde tienes que dividir una red en trozos de distintos tamaños:
1. **Ordena**: De la red más grande a la más pequeña (fundamental).
2. **Bits de Host ($h$)**: Busca el $h$ tal que $2^h \geq \text{Hosts} + 2$.
   - Ej: Para 50 hosts necesitamos 6 bits ($2^6 = 64$).
3. **Máscara**: La nueva máscara será $32 - h$.
4. **Siguiente Salto**: La siguiente subred empieza exactamente después de donde termina el trozo actual ($2^h$).

---
**Relacionado**: [[Ejercicios - Interconexión de Redes]]
**Fuente**: [[52_Tema5.pdf]]
