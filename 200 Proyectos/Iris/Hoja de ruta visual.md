Aquí está la hoja de ruta que reestructura tus issues de GitHub según las prioridades de la auditoría, ahora con descripciones detalladas para cada acción.

He creado un "SPRINT 0 (Fundación)" que agrupa todas las tareas de la auditoría. Tus tareas de SPRINT 1 (MVP) ahora se construyen _sobre_ esa fundación segura.

### Proyecto Iris: Rumbo Corregido

#### SPRINT 0 (Fundación - Corregir la Arquitectura Rota)

- **Meta: Estabilización de Arquitectura (#31) (Épica)**
    
    - **Descripción:** El objetivo de este sprint es demoler la arquitectura rota e insegura actual y construir la fundación monolítica correcta. Esto es un requisito no negociable antes de escribir cualquier nueva funcionalidad.
        
- **✨ Tarea: Consolidar 3 Backends en 1**
    
    - **Descripción:** Fusionar `servicio-usuarios`, `servicio-asignaturas` y `servicio-suscripciones` en un solo backend FastAPI. Esto elimina la complejidad de los "microservicios fantasma" (ver auditoría) y centraliza toda la lógica de negocio en un lugar mantenible.
        
- **✨ Tarea: Refactorizar n8n (Quitar SQL)**
    
    - **Descripción:** Eliminar _todas_ las consultas SQL directas del flujo de n8n (`iris.json`). La única acción de n8n será llamar a un nuevo endpoint en nuestro backend (`POST /api/internal/notify`). Esto mueve la lógica de negocio crítica de un JSON frágil a código Python testeable y robusto.
        
- **✨ Tarea: Implementar Ingesta 'Push' (Webhook)**
    
    - **Descripción:** Eliminar el `Gmail Trigger` (que sondea 'Pull'). Reemplazarlo por un `Webhook Trigger` pasivo de n8n. Este webhook será alimentado por un servicio externo (ej. SendGrid) que reciba los correos reenviados automáticamente (flujo 'Push'), haciendo la ingesta instantánea, segura y escalable.
        
- **Tarea: Orquestación en API Gateway (#36)**
    
    - **Descripción:** Hacer que el `api-gateway` funcione. Implementar las reglas de proxy para enrutar el tráfico: `/api/*` al nuevo backend monolítico y `/n8n-webhook/*` (o la ruta que definas) al webhook de n8n. El frontend _solo_ hablará con el gateway.
        
- **Tarea: Poblar BBDD (Seed) (#35)**
    
    - **Descripción:** Actualizar el `init-db.sh` para que no solo cree tablas, sino que también inserte los datos iniciales de asignaturas y profesores. Esto asegura que el backend tenga datos con los que trabajar desde el arranque.
        

#### SPRINT 1 (MVP - El Producto Seguro)

- **Epic: Sistema de Autenticación (#37) (Épica)**
    
    - **Descripción:** El objetivo es cerrar el fallo de seguridad crítico de "Inyección de SPAM". Solo usuarios verificados de la universidad (`@alumnos.uneatlantico.es`) podrán acceder al sistema y suscribirse.
        
- **Tarea: Inicio de sesión con Gmail (#22) (Crítica)**
    
    - **Descripción:** Construir la UI en el frontend (React) que permita al usuario iniciar el flujo de Google OAuth. **Nueva Lógica:** Después de un login exitoso, el frontend debe comprobar la respuesta del backend (ej. en el JWT) para ver si el usuario ya tiene un teléfono registrado. Si no lo tiene, debe _redirigir forzosamente_ al usuario a la página de perfil/teléfono (Tarea #18).
        
- **✨ Tarea: Implementar Google OAuth (Backend) (Crítica)**
    
    - **Descripción:** Crear los endpoints en el backend monolítico (`/auth/login`, `/auth/callback`) para manejar el flujo de Google OAuth. **Nueva Lógica:** Al verificar el dominio y crear el JWT, el backend debe añadir una _claim_ (un campo) al JWT, como `has_phone: true/false`, para que el frontend sepa si el usuario ha completado el onboarding del teléfono.
        
- **Epic: Gestión de Usuario (#38) (Épica)**
    
    - **Descripción:** Permitir que los usuarios autenticados gestionen sus perfiles y las suscripciones a las que están activamente apuntados.
        
- **Tarea: Crear Perfil de Usuario (#18) (Pasa a ser Crítica)**
    
    - **Descripción:** Esta tarea ya no es una simple página de "perfil". **Es el paso de onboarding obligatorio** después del login para usuarios nuevos. Esta vista debe: (a) Ser a donde se redirige a los usuarios sin teléfono. (b) Requerir que el usuario introduzca su número de WhatsApp. (c) Idealmente, incluir un paso de verificación (ej. enviar un código por WhatsApp y pedirlo). El servicio no será accesible hasta que este paso se complete.
        
- **Tarea: Interfaz de Suscripción (#8)**
    
    - **Descripción:** Refactorizar la interfaz actual. **Nueva Lógica:** Esta página debe ser _inaccesible_ (o redirigir al perfil) si el usuario no tiene un teléfono verificado. Si tiene teléfono, debe cargar las asignaturas (`GET /api/asignaturas`) y permitir al usuario seleccionar/deseleccionar sus suscripciones (`POST /api/subscriptions`).
        
- **... (MODIFICAR: Eliminar campo de teléfono) (Crítica)**
    
    - **Descripción:** Acción específica: Eliminar los campos de 'Nombre' y 'WhatsApp' del formulario de suscripción _anónimo_ (que ya no existirá). Esta tarea se transforma en asegurar que el _nuevo_ formulario de suscripción (`#8`) no pida esta información, ya que la obtiene del JWT (nombre/email) y del perfil verificado (teléfono).
        
- **Tarea: Borrar Cuenta y Desuscripción (#21)**
    
    - **Descripción:** Implementar la funcionalidad de 'Darse de baja' (eliminar suscripciones individuales) y 'Eliminar mi cuenta' (borrado GDPR completo). Esto es un requisito legal y de confianza del usuario.
        
- **Tarea: Validar Formularios (#24)**
    
    - **Descripción:** Asegurar que toda la entrada del usuario (ej. el formulario de perfil para el teléfono) tenga validación robusta tanto en el frontend (React) como en el backend (Pydantic).
        

#### DEPLOY (Puesta en Marcha)

- **Epic: Despliegue (#39) (Épica)**
    
    - **Descripción:** Tareas relacionadas con mover el proyecto de `localhost` a un servidor de producción accesible en Internet.
        
- **Tarea: Hostear y configurar servidor (#28)**
    
    - **Descripción:** Configurar un VPS (ej. DigitalOcean, Vultr), instalar Docker, configurar DNS para tu dominio, obtener certificados SSL (Let's Encrypt) y desplegar la aplicación usando `docker-compose`.
        

#### BACKLOG (Futuro)

- **Idea: Inicio de sesión con Passkey (#23)**
    
    - **Descripción:** (Post-MVP) Explorar métodos de autenticación sin contraseña para mejorar la seguridad y la experiencia de usuario, una vez que el MVP esté estable.
        
- **Idea: Comprensión avanzada de contexto (#2)**
    
    - **Descripción:** (Post-MVP) Mejorar el _prompt_ de la LLM para que no solo resuma, sino que entienda el contexto (ej. 'examen', 'cancelación de clase') y pueda etiquetar la prioridad del mensaje.
        

### Leyenda

- **✨ Tarea (Nueva):** Tareas críticas _nuevas_ identificadas en la auditoría que no estaban en tus issues.
    
- **Tarea (Crítica):** Tareas que corrigen un fallo de seguridad fundamental.
    
- **(Épica):** Tus épicas existentes.
    
- **Tarea:** Tus tareas existentes, ahora re-priorizadas.
    
- **Idea:** Ideas para después del MVP.
    

Este plan es tu nuevo rumbo.