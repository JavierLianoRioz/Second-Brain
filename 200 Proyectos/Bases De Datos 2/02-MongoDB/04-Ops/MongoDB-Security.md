# Seguridad en MongoDB: Autenticación y Autorización

En producción, una base de datos que no controla el acceso es una **vulnerabilidad crítica**. MongoDB gestiona la seguridad en tres dimensiones: control de acceso, validación estructural y principio de mínimo privilegio.

### Autenticación vs Autorización
*   **Autenticación:** Verifica la identidad del usuario (¿quién eres?).
*   **Autorización:** Determina qué operaciones puede realizar (¿qué puedes hacer?).

MongoDB usa por defecto **SCRAM** (Salted Challenge Response Authentication Mechanism), que evita el envío de contraseñas en texto plano.

### Creación de Usuarios
Un usuario se define con: nombre, contraseña y **roles asignados**.
```javascript
// Administrador global
use admin
db.createUser({
  user: "adminDB",
  pwd: "passwordSeguro123",
  roles: [{ role: "userAdminAnyDatabase", db: "admin" }]
})

// Usuario de aplicación (solo una BD)
use universidad
db.createUser({
  user: "appCursos",
  pwd: "claveAplicacion",
  roles: [{ role: "readWrite", db: "universidad" }]
})
```

### Roles Predefinidos

| Rol          | Lectura  | Escritura | Administración |
| ------------ | -------- | --------- | -------------- |
| read         | Sí      | No        | No             |
| readWrite    | Sí      | Sí       | No             |
| dbAdmin      | Limitada | Limitada  | Sí            |
| clusterAdmin | Sí      | Sí       | Sí            |

### Principio de Mínimo Privilegio
Cada usuario/sistema debe tener **únicamente** los permisos estrictamente necesarios:
*   Aplicaciones → `readWrite` solo sobre sus colecciones
*   Analistas → `read`
*   Administradores → `clusterAdmin`

> [!WARNING]
> Un error frecuente es asignar `readWrite` a todos por comodidad. Simplifica al inicio pero introduce riesgos acumulativos.

Para asegurar un entorno profesional, combina la gestión de accesos con la [validación estructural](MongoDB-Schema-Validation.md) de los datos y sigue las [Buenas Prácticas Operativas](MongoDB-Best-Practices.md) para evitar [Errores de Seguridad](MongoDB-Security-Errors.md) comunes.
