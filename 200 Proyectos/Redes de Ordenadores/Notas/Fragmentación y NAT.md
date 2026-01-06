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

---
**Relacionado**: [[Protocolo IP (IPv4 e IPv6)]]
**Fuente**: [[52_Tema5.pdf]]
