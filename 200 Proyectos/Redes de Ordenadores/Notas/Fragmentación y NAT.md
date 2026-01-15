# Fragmentación y NAT

Mecanismos para manejar limitaciones físicas y de direccionamiento.

## Fragmentación
- En **IPv4**, si un datagrama es mayor que la **MTU** del siguiente enlace, el router lo divide en fragmentos.
- Usa los campos **Identification**, **Flags** (MF, DF) y **Fragment Offset**.
- El reensamblado solo se realiza en el destino final.
- **Nota**: En **IPv6**, los routers NO fragmentan; si el paquete es muy grande, se descarta y se avisa al origen.

## NAT (Network Address Translation)
- **Concepto**: Un "traductor" en la frontera de casa.
  - *Analogía*: En un hotel, todas las habitaciones tienen un número interno (IP Privada), pero si alguien de fuera envía una carta, la envía a la dirección del hotel (IP Pública). El recepcionista (Router/NAT) sabe a qué habitación entregarla.
- **PAT (NAPT)**: Usa números de puerto para saber qué "conversación" pertenece a quién si varios equipos navegan a la vez.

> [!TIP]
> **En el examen**: Si te piden la tabla NAT/PAT, recuerda que cada flujo (IP origen + Puerto origen) debe mapearse a un **Puerto Público Único** en la IP del router para que la vuelta no se pierda.

## Cómo Resolver Fragmentación (Pasos de Examen)
Cuando te den un datagrama de tamaño $X$ y un un MTU de $M$:
1. **Datos Reales**: Resta la cabecera (20 bytes) al total del datagrama ($X - 20$).
2. **Trozo Máximo**: Resta la cabecera al MTU ($M - 20$).
   - **IMPORTANTE**: Este número de datos debe ser **múltiplo de 8**. Si no lo es, redondea hacia abajo al múltiplo de 8 más cercano.
3. **Offset**: Es el acumulado de datos de fragmentos anteriores dividido por 8.
4. **MF (More Fragments)**: Poner un `1` si siguen más fragmentos, y un `0` solo en el último.

---
**Relacionado**: [Protocolo IP (IPv4 e IPv6)](Protocolo%20IP%20%28IPv4%20e%20IPv6%29.md), [Ejercicios - Interconexión de Redes](../Ejercicios/Ejercicios%20-%20Interconexi%C3%B3n%20de%20Redes.md)
**Fuente**: [[52_Tema5.pdf]]
