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

---
**Relacionado**: [[Protocolo TCP - Servicio y Multiplexación]], [[Protocolo UDP]]
**Fuente**: [[62_Tema6.pdf]]
