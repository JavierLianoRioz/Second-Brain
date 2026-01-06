# Dispositivos de Seguridad (Firewalls, IDS, IPS)

Herramientas perimetrales e internas para el control del tráfico.

## Cortafuegos (Firewalls)
- **Analogía**: El portero de una discoteca. Si no estás en la lista o vas mal vestido (protocolo prohibido), no pasas.
- **Inspección de estado (Stateful)**: El portero que recuerda quién ha salido hace un momento a fumar para dejarle entrar sin preguntar de nuevo.
- **DPI (Deep Packet Inspection)**: El portero que no solo mira tu DNI, sino que te cachea y mira qué llevas dentro de los bolsillos (analiza el contenido de los datos).

## Zona Desmilitarizada (DMZ)
Subred protegida donde pones los servidores que deben ser vistos desde Internet (Web, Correo).
- **Diseño con 1 FW**: Tres "patas" (Internet, Red interna, DMZ). Sencillo pero un solo error en el FW expone todo.
- **Diseño con 2 FW (Cinturón y Tirantes)**: Uno protege la DMZ desde Internet y otro protege la Red Interna desde la DMZ. Si cae el primero, el segundo sigue protegiendo lo más valioso.

## IDS / IPS
- **IDS (Intrusion Detection System)**:
  - *Analogía*: Una cámara de seguridad. Graba que alguien ha entrado a robar, pero no hace nada para detenerlo. Solo avisa después.
- **IPS (Intrusion Prevention System)**:
  - *Analogía*: Un guarda de seguridad con un perro. Si ve que alguien intenta saltar la valla, lo muerde y lo detiene en el acto.

## Proxies
Intermediarios en conexiones de aplicación (ej. Proxy HTTP). Pueden filtrar contenido y ocultar la estructura interna.

---
**Relacionado**: [[Zona desmilitarizada (DMZ)]]
**Fuente**: [[72_Tema7.pdf]]
