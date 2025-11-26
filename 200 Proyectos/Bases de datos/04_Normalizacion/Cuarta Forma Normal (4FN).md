# Cuarta Forma Normal (4FN)

Una tabla está en **Cuarta Forma Normal (4FN)** si:

1.  Está en [[Tercera Forma Normal (3FN)]].
2.  No existen **dependencias multivaluadas no triviales**.

Una **dependencia multivaluada** ocurre cuando un atributo en una tabla determina **independientemente** a otros dos o más conjuntos de atributos. Es decir, un atributo determina varias listas de valores independientes.

### Ejemplo
Si un profesor puede enseñar varios cursos y hablar varios idiomas, y esas dos listas son independientes entre sí, guardarlas en la misma tabla genera redundancia.

**Tabla PROFESOR_INFO (no normalizada)**

| id_profesor | nombre     | curso        | idioma   |
|------------|------------|--------------|----------|
| 1          | Ana López  | Matemáticas  | Inglés   |
| 1          | Ana López  | Matemáticas  | Español  |
| 1          | Ana López  | Historia     | Inglés   |
| 1          | Ana López  | Historia     | Español  |

Aquí, `curso` e `idioma` son independientes entre sí, pero se repiten para cada combinación, causando redundancia.

### Normalización a 4FN
Se descompone la tabla en relaciones separadas para cada dependencia multivaluada.

**PROFESOR_CURSO**

| id_profesor | curso        |
|------------|--------------|
| 1          | Matemáticas  |
| 1          | Historia     |

**PROFESOR_IDIOMA**

| id_profesor | idioma   |
|------------|----------|
| 1          | Inglés   |
| 1          | Español  |

De esta manera, cada tabla representa una única relación sin redundancia, y los cambios en una no afectan a la otra.

---
**Relacionado:** [[Normalización]], [[Tercera Forma Normal (3FN)]], [[Quinta Forma Normal (5FN)]]
