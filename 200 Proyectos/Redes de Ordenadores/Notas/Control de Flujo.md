# Control de Flujo

Mecanismo para evitar que un emisor rápido sature a un receptor lento.

## Estrategias de Control de Flujo
1. **Parada y Espera (Stop & Wait)**: Envías una carta y no envías la siguiente hasta que recibes la carta de confirmación.
   - *Problema*: Muy lento si el cartero tarda mucho (mucha distancia). El buzón está vacío casi siempre.
2. **Ventana Deslizante (Sliding Window)**: Puedes enviar hasta $W$ cartas seguidas sin esperar.
   - *Analogía*: Malabarismos. Mientras una pelota (trama) vuela por el aire, lanzas la siguiente. Mantienes el canal ocupado y eficiente.

---
**Relacionado**: [[Protocolos ARQ]]
**Fuente**: [[32_Tema3.pdf]]
