# Transformación: De ER a Relacional

El paso del Diseño Conceptual ([Modelo Entidad Relacion](Modelo_Entidad_Relacion.md)) al Lógico ([Modelo Relacional Conceptos](Modelo_Relacional_Conceptos.md)) sigue reglas precisas:

## Reglas de Transformación

### 1. Entidades Fuertes
Cada entidad fuerte se convierte en una **Tabla**. Su identificador pasa a ser la [Clave Primaria](Clave_Primaria.md).

### 2. Relaciones 1:N
Se propaga la clave. La PK del lado "1" pasa como [Clave Foranea](Clave_Foranea.md) a la tabla del lado "N".
*   *Ejemplo*: `Cliente (1) -- (N) Pedido`. En `Pedido` agregamos `id_cliente`.

### 3. Relaciones N:M
Se crea una **Nueva Tabla Intermedia**.
*   Esta tabla tendrá como FKs las PKs de las dos entidades.
*   La PK de la nueva tabla suele ser la composición de ambas FKs.

### 4. Relaciones 1:1
Se propaga la clave de una tabla a la otra (preferiblemente a la que tenga participación total).

---
## 📝 Ejercicios de Práctica

**Caso: Sistema de Videoclub**
1.  **Entidades**: `Pelicula` (id, titulo) y `Socio` (id, nombre).
2.  **Relación**: Un `Socio` alquila muchas `Peliculas`. Una `Pelicula` es alquilada por un `Socio` a la vez.

**Pregunta**: ¿Cómo transformarías esta relación 1:N al modelo relacional?
*   *Solución*: Añadir `id_socio` como FK en la tabla `Pelicula`.

**Pregunta**: Si fuera N:M (un socio alquila muchas películas a lo largo del tiempo y una película es alquilada por muchos socios), ¿qué harías?
*   *Solución*: Crear una tabla `Alquiler` con `id_socio` e `id_pelicula` como FKs (y juntas como PK).

---
[00 MOC Diseño](00_MOC_Dise%C3%B1o.md)
