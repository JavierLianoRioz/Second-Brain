# Transformación: De ER a Relacional

El paso del Diseño Conceptual ([[Modelo_Entidad_Relacion]]) al Lógico ([[Modelo_Relacional_Conceptos]]) sigue reglas precisas:

## Reglas de Transformación

### 1. Entidades Fuertes
Cada entidad fuerte se convierte en una **Tabla**. Su identificador pasa a ser la [[Clave_Primaria]].

### 2. Relaciones 1:N
Se propaga la clave. La PK del lado "1" pasa como [[Clave_Foranea]] a la tabla del lado "N".
*   *Ejemplo*: `Cliente (1) -- (N) Pedido`. En `Pedido` agregamos `id_cliente`.

### 3. Relaciones N:M
Se crea una **Nueva Tabla Intermedia**.
*   Esta tabla tendrá como FKs las PKs de las dos entidades.
*   La PK de la nueva tabla suele ser la composición de ambas FKs.

### 4. Relaciones 1:1
Se propaga la clave de una tabla a la otra (preferiblemente a la que tenga participación total).

---
[[00_MOC_Diseño]]
