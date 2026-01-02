# Protocolos IP (ICMP, ARP, DHCP, DNS)

Protocolos auxiliares esenciales para el funcionamiento de una red IP.

## ICMP (Internet Control Message Protocol)
- **Analogía**: Las señales de tráfico. "Vía cortada" (Red inalcanzable), "Desvío" (Redirección), o "Aviso de radar" (Expiración de TTL).
- **Traceroute**: Usa el campo *TTL* para obligar a cada router del camino a decir "¡Aquí estoy!" cuando el paquete muere.

## ARP (Address Resolution Protocol)
- **Analogía**: Estás en una oficina y buscas a alguien pero solo sabes su nombre (IP). Te levantas y gritas: "¡¿Quién es Juan Pérez?! ¡Dime tu número de mesa (MAC)!". Solo Juan Pérez responde.

## DHCP (Dynamic Host Configuration Protocol)
Configuración automática de red (IP, Máscara, Gateway, DNS).
- El cliente solicita mediante broadcast y el servidor asigna ("lease") los parámetros.

## DNS (Domain Name System)
Traduce nombres legibles (ej. `google.com`) a direcciones IP numéricas.

---
**Relacionado**: [[Principios de la Capa de Red]]
**Fuente**: [[52_Tema5.pdf]]
