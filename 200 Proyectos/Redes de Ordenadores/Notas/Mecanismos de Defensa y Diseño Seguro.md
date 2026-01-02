# Mecanismos de Defensa y Diseño Seguro

Estrategias para proteger la red desde su arquitectura.

## Diseño Seguro
- **Segmentación**: Dividir la red en subredes (VLANs) para limitar el "radio de explosión" de un ataque.
- **Zona Desmilitarizada (DMZ)**:
  - *Analogía*: El jardín delantero de una casa. Cualquiera puede entrar al jardín para llamar al timbre o mirar las flores (Servidor Web), pero para entrar al salón (Red Interna) necesitas una llave especial y pasar otra puerta mucho más fuerte.
- **Redundancia**: Evitar puntos únicos de fallo.

## Control de Acceso
- **Principio de Privilegio Mínimo**: Dar solo los permisos estrictamente necesarios.
- **ACLs (Access Control Lists)**: Filtros en routers/switches que permiten o deniegan tráfico basado en IP/Puerto/Protocolo.
- **Actualización y Parcheado**: Mantener el firmware y software al día para eliminar vulnerabilidades conocidas.

---
**Relacionado**: [[Dispositivos de Seguridad (Firewalls, IDS, IPS)]], [[Zona desmilitarizada (DMZ)]]
**Fuente**: [[72_Tema7.pdf]]
