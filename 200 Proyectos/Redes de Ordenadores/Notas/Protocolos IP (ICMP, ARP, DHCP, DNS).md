# Protocolos IP (ICMP, ARP, DHCP, DNS)

Protocolos auxiliares esenciales para el funcionamiento de una red IP.

## ICMP (Internet Control Message Protocol)
- **Analogía**: Las señales de tráfico. "Vía cortada" (Red inalcanzable), "Desvío" (Redirección), o "Aviso de radar" (Expiración de TTL).
- **Traceroute**: Usa el campo *TTL* para obligar a cada router del camino a decir "¡Aquí estoy!" cuando el paquete muere.

## ARP (Address Resolution Protocol)
- **Función**: Es el "traductor" entre el mundo lógico (IP) y el mundo físico (MAC).
- **El Problema**: Tu ordenador sabe a qué IP (lógica) enviar el dato, pero la tarjeta de red (hardware) solo sabe enviar tramas a direcciones MAC.
- **La Solución (Analogía)**: Estás en una oficina y buscas a alguien pero solo sabes su nombre (IP). Te levantas y gritas: "¡¿Quién es Juan Pérez?! ¡Dime tu número de mesa (MAC)!". Solo Juan Pérez responde con su ubicación física.

## DHCP (Dynamic Host Configuration Protocol)
Configuración automática de red (IP, Máscara, Gateway, DNS).
- El cliente solicita mediante broadcast y el servidor asigna ("lease") los parámetros.

## DNS (Domain Name System)
Traduce nombres legibles (ej. `google.com`) a direcciones IP numéricas.

---
**Relacionado**: [Principios de la Capa de Red](Principios%20de%20la%20Capa%20de%20Red.md)
**Fuente**: [[52_Tema5.pdf]]
