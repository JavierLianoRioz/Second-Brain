# Protocolo UDP

UDP (**User Datagram Protocol**) ofrece un servicio mínimo y eficiente sobre IP.

## Características
- **No orientado a conexión**: Lanza los datos y se olvida.
  - *Analogía*: Como un locutor de radio o alguien gritando con un megáfono. No sabe quién escucha ni si le entienden, pero es rapidísimo.
- **Mantiene fronteras de mensajes**: Si envías tres mensajes distintos, el otro recibe tres "paquetes" separados. (A diferencia del "grifo" de TCP).

## Cabecera (8 bytes)
- Puertos Origen y Destino (16 bits cada uno).
- Longitud total.
- Checksum (opcional en IPv4, obligatorio en IPv6).

## Casos de Uso
- **Streaming y Tiempo Real**: Voz sobre IP (VoIP), juegos (prioriza velocidad sobre reordenación).
- **Broadcast/Multicast**: TCP no puede enviar a varios destinos a la vez.
- **Consultas Simples**: DNS, DHCP.

---
**Relacionado**: [[Conceptos de la Capa de Transporte]]
**Fuente**: [[62_Tema6.pdf]]
