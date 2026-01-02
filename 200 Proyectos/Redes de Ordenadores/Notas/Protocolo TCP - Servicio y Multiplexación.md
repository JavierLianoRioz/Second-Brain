# Protocolo TCP - Servicio y Multiplexación

TCP (**Transmission Control Protocol**) es un protocolo fiable y orientado a conexión.

## Características del Servicio
- **Fiable**: Si algo falla, se retransmite. Es como un envío certificado.
- **Orientado a Conexión**: No envía nada sin antes asegurarse de que el otro está "al teléfono".
- **Basado en Flujos (Streams)**:
  - *Analogía*: Como un grifo de agua. Los datos salen uno tras otro sin marca de dónde termina un vaso y empieza el siguiente. La aplicación debe saber cuándo parar de leer.

## Multiplexación y Sockets
- **Puertos**: 16 bits (0-65535).
  - **Well-known (1-1023)**: Reservados para servicios estándar (ej. 80 HTTP, 443 HTTPS, 22 SSH).
  - **Efímeros (49152-65535)**: Usados por los clientes para iniciar conexiones.
- **Socket**: Identificado por la **5-tupla**: (IP Origen, Puerto Origen, IP Destino, Puerto Destino, Protocolo TCP).

---
**Relacionado**: [[Cabecera y Ciclo de Vida de TCP]]
**Fuente**: [[62_Tema6.pdf]]
