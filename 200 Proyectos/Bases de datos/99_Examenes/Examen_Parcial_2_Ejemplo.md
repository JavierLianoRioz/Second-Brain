# Ejemplo de Examen - 2º Parcial de Bases de Datos

**Temario:** SQL Avanzado, Normalización, Álgebra Relacional, Transacciones.
**Tiempo estimado:** 90 minutos.

---

## Parte 1: SQL (4 Puntos)

Dada la siguiente estructura de base de datos para una **Biblioteca**:

*   `LIBROS` (<u>id_libro</u>, titulo, autor, año_publicacion, editorial)
*   `SOCIOS` (<u>id_socio</u>, nombre, fecha_registro, ciudad)
*   `PRESTAMOS` (<u>id_prestamo</u>, id_libro, id_socio, fecha_prestamo, fecha_devolucion)

**Escribe las consultas SQL para obtener:**

1.  **(0.5p)** Título y autor de los libros publicados por la editorial "Planeta" después del año 2010.
2.  **(1.0p)** Nombre de los socios que han pedido prestado el libro con título "El Quijote".
3.  **(1.0p)** Listado de ciudades y el número de socios registrados en cada una. Solo mostrar ciudades con más de 5 socios.
4.  **(1.5p)** Título del libro que ha sido prestado más veces en la historia de la biblioteca.

---

## Parte 2: Normalización (3 Puntos)

Analiza la siguiente relación no normalizada de **PEDIDOS_CLIENTE**:

| ID_Pedido | Fecha | ID_Cliente | Nombre_Cliente | Ciudad_Cliente | ID_Producto | Descripcion_Prod | Cantidad | Precio_Unit |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 101 | 2023-01-10 | C1 | Juan Pérez | Madrid | P1 | Laptop | 1 | 1000 |
| 101 | 2023-01-10 | C1 | Juan Pérez | Madrid | P2 | Ratón | 2 | 20 |
| 102 | 2023-01-11 | C2 | Ana Gómez | Barcelona | P1 | Laptop | 1 | 1000 |

**Se pide:**

1.  **(0.5p)** Identificar las Dependencias Funcionales (DF).
2.  **(1.0p)** Explicar por qué NO está en 2FN y/o 3FN.
3.  **(1.5p)** Normalizar la relación hasta la **Tercera Forma Normal (3FN)**, indicando las tablas resultantes con sus claves primarias (PK) y foráneas (FK).

---

## Parte 3: Álgebra Relacional (1.5 Puntos)

Usando las tablas del ejercicio 1 (Biblioteca), escribe las siguientes consultas en **Álgebra Relacional**:

1.  **(0.75p)** Obtener el `nombre` de todos los socios de la ciudad "Madrid".
2.  **(0.75p)** Obtener el `titulo` de los libros que han sido prestados por el socio con id_socio = 5.

---

## Parte 4: Teoría y Transacciones (1.5 Puntos)

1.  **(0.75p)** Define qué es una **Transacción** y explica brevemente las propiedades **ACID**.
2.  **(0.75p)** Dado el siguiente escenario, explica qué ocurriría si falla el sistema antes del `COMMIT`:
    ```sql
    BEGIN TRANSACTION;
    UPDATE Cuentas SET saldo = saldo - 100 WHERE id = A;
    UPDATE Cuentas SET saldo = saldo + 100 WHERE id = B;
    -- Fallo de luz aquí
    COMMIT;
    ```
    ¿Qué garantiza la base de datos en este caso?

---

## Soluciones Sugeridas (Resumen)

### SQL
1.  
   ```sql
   SELECT titulo, autor
   FROM LIBROS
   WHERE editorial = 'Planeta' AND año_publicacion > 2010;
   ```  
   
2.  
   ``` sql
   SELECT S.nombre 
   FROM SOCIOS S 
   JOIN PRESTAMOS P ON S.id_socio = P.id_socio 
   JOIN LIBROS L ON P.id_libro = L.id_libro 
   WHERE L.titulo = 'El Quijote';
   ```
3.  
   ```sql
   SELECT ciudad, COUNT(*) 
   FROM SOCIOS 
   GROUP BY ciudad 
   HAVING COUNT(*) > 5;
   ```

### Normalización
*   **Tablas 3FN**:
    *   `CLIENTES` (<u>ID_Cliente</u>, Nombre, Ciudad)
    *   `PRODUCTOS` (<u>ID_Producto</u>, Descripcion, Precio)
    *   `PEDIDOS` (<u>ID_Pedido</u>, Fecha, ID_Cliente)
    *   `DETALLE_PEDIDO` (<u>ID_Pedido, ID_Producto</u>, Cantidad)

### Álgebra
1.  π nombre (σ ciudad='Madrid' (SOCIOS))

### Transacciones
2.  Gracias a la propiedad de **Atomicidad**, si falla antes del COMMIT, se hace un **ROLLBACK** automático. Ningún cambio se guarda. El dinero no se pierde.
