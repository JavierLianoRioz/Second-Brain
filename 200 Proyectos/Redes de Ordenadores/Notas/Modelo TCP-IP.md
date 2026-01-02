  # Modelo TCP-IP

A diferencia del modelo OSI, el modelo TCP/IP es la arquitectura real sobre la que se fundamenta Internet. Es más simple y práctico.

## Capas del Modelo TCP/IP
- **Capa de Acceso a Red**: Engloba las capas físicas y de enlace del modelo OSI. Se encarga de la interfaz con el hardware de red.
- **Capa de Internet (IP)**: Proporciona direccionamiento global y enrutamiento a través de redes físicamente distintas. Utiliza el protocolo **IP**.
- **Capa de Transporte**: Comunicación de proceso a proceso.
  - **TCP (Transmission Control Protocol)**: Fiable, orientado a la conexión, con control de errores y flujo.
  - **UDP (User Datagram Protocol)**: No fiable, rápido, orientado a datagramas, sin control de flujo ni errores.
- **Capa de Aplicación**: Engloba las capas de sesión, presentación y aplicación de OSI. Incluye protocolos como HTTP, FTP, DNS, etc.

## Direccionamiento y Puertos
- **Dirección IP**: Identifica a un host en Internet (Capa de Red).
- **Puerto**: Identifica a una aplicación específica dentro de un host (Capa de Transporte). El conjunto (IP:Puerto) se denomina a veces **Socket**.

---
**Relacionado**: [[Modelo OSI]], [[Arquitectura de Protocolos]]
**Fuente**: [[12_Tema1.pdf]]
