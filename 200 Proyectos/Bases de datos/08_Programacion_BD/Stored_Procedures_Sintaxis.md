# Sintaxis de Stored Procedures

Un Procedimiento Almacenado (Stored Procedure) es un conjunto de sentencias SQL que se guardan en el servidor para ser ejecutadas mediante una sola llamada.

## Estructura Básica

Para crear un procedimiento, se debe cambiar temporalmente el delimitador para que el punto y coma (`;`) no finalice la creación del procedimiento antes de tiempo.

```sql
DELIMITER //

CREATE PROCEDURE nombre_procedimiento(IN parametro_entrada INT, OUT parametro_salida VARCHAR(50))
BEGIN
    -- Cuerpo del procedimiento
    -- Sentencias SQL
END //

DELIMITER ;
```

## Componentes Clave

- **DELIMITER**: Cambia el carácter de fin de sentencia (comúnmente a `//` o `$$`).
- **IN / OUT / INOUT**: Define si los parámetros son de entrada, salida o ambos.
- **BEGIN ... END**: Delimita el bloque de código lógico del procedimiento.
- **CALL**: Comando para ejecutar el procedimiento: `CALL nombre_procedimiento(args);`.

## Ventajas
- **Rendimiento**: Se precompila en el servidor.
- **Seguridad**: Permite dar permisos de ejecución sin dar acceso directo a las tablas.
- **Mantenibilidad**: La lógica reside en un solo lugar.

---
- **Relacionado**: [Control de Flujo](Control_de_Flujo.md), [Ejemplos](Ejemplos_Programacion.md)
