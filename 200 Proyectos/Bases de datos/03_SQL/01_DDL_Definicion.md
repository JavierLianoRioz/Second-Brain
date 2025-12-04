# SQL: Lenguaje de Definición de Datos (DDL)

El **DDL (Data Definition Language)** permite definir y modificar la estructura de la base de datos (tablas, índices, restricciones).

## 1. Tipos de Datos Comunes

Elegir el tipo correcto es vital para la integridad y el rendimiento.

| Tipo | Descripción | Ejemplo |
| :--- | :--- | :--- |
| **INT / BIGINT** | Números enteros. | `id_cliente INT` |
| **DECIMAL(p,s)** | Números exactos (p=precisión, s=escala). Ideal para dinero. | `precio DECIMAL(10,2)` |
| **VARCHAR(n)** | Texto de longitud variable (hasta n caracteres). | `nombre VARCHAR(100)` |
| **CHAR(n)** | Texto de longitud fija (siempre ocupa n). | `codigo_pais CHAR(2)` |
| **DATE** | Fecha (AAAA-MM-DD). | `fecha_nacimiento DATE` |
| **BOOLEAN** | Verdadero o Falso. | `activo BOOLEAN` |

---

## 2. Restricciones (Constraints)

Reglas que garantizan la calidad de los datos.

*   **PRIMARY KEY (PK)**: Identificador único. No nulo.
*   **FOREIGN KEY (FK)**: Enlace a otra tabla (Integridad Referencial).
*   **NOT NULL**: Obliga a tener un valor.
*   **UNIQUE**: Impide valores duplicados en la columna.
*   **CHECK**: Valida una condición lógica.
*   **DEFAULT**: Asigna un valor si no se especifica.

---

## 3. Comandos Principales

### CREATE TABLE
Crea una nueva tabla.

```sql
CREATE TABLE empleado (
    id_empleado INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    salario DECIMAL(10,2) CHECK (salario > 0),
    fecha_ingreso DATE DEFAULT CURRENT_DATE,
    id_departamento INT,
    FOREIGN KEY (id_departamento) REFERENCES departamento(id_departamento)
);
```

### ALTER TABLE
Modifica una tabla existente.

```sql
-- Añadir columna
ALTER TABLE empleado ADD COLUMN telefono VARCHAR(20);

-- Modificar tipo de dato
ALTER TABLE empleado MODIFY COLUMN nombre VARCHAR(150);

-- Añadir restricción
ALTER TABLE empleado ADD CONSTRAINT fk_jefe 
FOREIGN KEY (id_jefe) REFERENCES empleado(id_empleado);

-- Borrar columna
ALTER TABLE empleado DROP COLUMN telefono;
```

### DROP TABLE
Elimina una tabla y todos sus datos permanentemente.

```sql
DROP TABLE empleado;
```

> [!WARNING]
> `DROP TABLE` es irreversible. Si hay restricciones de clave foránea, primero debes borrar las tablas hijas o usar `CASCADE` (si el motor lo soporta).
