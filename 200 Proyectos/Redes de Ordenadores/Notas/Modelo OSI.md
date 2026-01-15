# Modelo OSI

El modelo de interconexión de sistemas abiertos (OSI) es un modelo de referencia creado por la ISO para estandarizar las comunicaciones. Se divide en 7 capas:

1. **Capa Física**: Transmisión de bits por el medio físico (cables, ondas).
2. **Capa de Enlace**: Gestión de tramas (frames), control de acceso al medio (MAC), detección de errores y control de flujo.
3. **Capa de Red**: Direccionamiento lógico y enrutamiento (Routing). Une redes físicas distintas.
4. **Capa de Transporte**: Comunicación extremo a extremo, segmentación de datos, control de errores y flujo extremo a extremo.
5. **Capa de Sesión**: Control de diálogos y gestión de sesiones entre aplicaciones.
6. **Capa de Presentación**: Formato de datos, cifrado, compresión y traducción.
7. **Capa de Aplicación**: Proporciona servicios de red directamente a las aplicaciones del usuario (ej. HTTP, SMTP).

### ¿Por qué necesitamos IP y MAC si la IP "ya nos identifica"?
Aunque parezca redundante, cumplen funciones distintas:
- **MAC (Capa 2)**: Identificación **física y local**. Es como tu nombre o tu cara en una habitación. Los switches la usan para saber por qué cable físico enviar la señal.
- **IP (Capa 3)**: Identificación **lógica y global**. Es como tu dirección postal (calle, ciudad). Los routers la usan para mover datos entre distintas redes del mundo.

**La Analogía Definitiva**:
- **IP** = Tu dirección de casa (cambia si te mudas).
- **MAC** = Tu número de DNI o tu cuerpo físico (te sigue a todas partes).
- Si quieres que te llegue una carta desde Japón, necesitan tu **IP** (dirección). Pero para que el cartero te la entregue en mano al entrar en tu edificio, necesita reconocerte a ti físicamente (**MAC**).

**Sobre la seguridad (Spoofing)**: La MAC no se diseñó para ser segura, sino para ser eficiente. Que sea "simulable" es un riesgo de seguridad, pero técnicamente sigue siendo necesaria para que el hardware sepa a quién "escuchar" en el cable.

---
**Relacionado**: [Modelo TCP-IP](Modelo%20TCP-IP.md), [Arquitectura de Protocolos](Arquitectura%20de%20Protocolos.md)
**Fuente**: [[12_Tema1.pdf]]
