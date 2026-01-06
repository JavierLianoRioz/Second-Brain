# Conceptos de la Capa de Transporte

La capa de transporte (Capa 4) proporciona una transferencia de datos lógica extremo a extremo entre aplicaciones.

## Funciones Principales
- **Direccionamiento (Puertos)**: 
  - *Analogía*: El IP es la dirección de un edificio de oficinas. El **Puerto** es el número de despacho. Necesitas ambos para entregar el paquete a la persona correcta (Aplicación).
- **Multiplexación**: Permite que mientras navegas por la web (Puerto 443), estés también en una llamada de Zoom (UDP) sin que se mezclen.
- **Segmentación**: Divide el archivo grande en "paquetes" manejables.

## Protocolos Principales
- **UDP**: Rápido, sin conexión, no fiable (mejor esfuerzo).
- **TCP**: Fiable, orientado a conexión, flujo de bytes.

## Interfaz de Programación: Sockets
Para usar el nivel de transporte, los programadores usan **Sockets**:
- **Socket**: Punto final de la comunicación (IP + Puerto).
- **Primitivas comunes**:
  - `BIND`: Asocia un puerto al socket.
  - `LISTEN`: El servidor se queda esperando.
  - `CONNECT`: El cliente inicia el saludo (3-way handshake).
  - `SEND/RECEIVE`: Envío y recepción de datos.

## El Checksum y la "Pseudo-cabecera"
TCP y UDP calculan un resumen (checksum) para detectar errores, pero hacen algo "sucio" técnicamente:
> [!NOTE]
> Durante el cálculo, incluyen campos de la capa de Red (IP origen y destino). Esto se llama **Pseudo-cabecera**. 
> *¿Por qué?*: Para asegurar que si la red "se equivoca" y te manda un paquete que no era para ti, el transporte lo detecte y lo tire. Esto rompe la separación estricta entre capas para ganar seguridad.

---
**Relacionado**: [[Protocolo TCP - Servicio y Multiplexación]], [[Protocolo UDP]]
**Fuente**: [[62_Tema6.pdf]]
