# Protocolos de Acceso Múltiple (ALOHA y CSMA)

Estrategias para resolver la contienda en medios compartidos.

## ALOHA
- **ALOHA puro**: "Disparar y esperar". Transmites y si no recibes confirmación, es que algo salió mal.
  - *Analogía*: Tirar un mensaje en una botella al mar.
- **ALOHA ranurado**: Solo puedes tirar la botella cuando suena una campana (ranura de tiempo). Menos choques.

## CSMA (Carrier Sense Multiple Access)
- **CSMA/CD (Collision Detection)**: "Escuchar antes de hablar" y "Detectar si te pisan".
  - *Analogía*: Intentas hablar en una fiesta. Escuchas si alguien habla; si hay silencio, hablas. Si justo otro empieza a la vez, ambos paráis, decís "perdón" (Jamming) y esperáis un tiempo al azar para reintentar.
- **CSMA/CA (Collision Avoidance)**: "Avisar antes de hablar".
  - *Analogía*: Levantar la mano en clase y esperar a que el profesor te diga "adelante" (Petición de envío/Confirmación).

## Estrategias de Persistencia
- **1-persistente**: Transmite en cuanto el medio está libre.
- **No-persistente**: Si está ocupado, espera un tiempo aleatorio antes de volver a escuchar.
- **p-persistente**: Transmite con probabilidad $p$ si está libre.

---
**Relacionado**: [[Ethernet (IEEE 802.3)]]
**Fuente**: [[42_Tema4.pdf]]
