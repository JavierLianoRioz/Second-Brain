---
materia: Ingeniería de Software
---
# Cohesión

La **Cohesión** es el principio del diseño modular que mide la fortaleza con la que se relacionan las responsabilidades asignadas a un elemento del software (clase, método o paquete). Es, en esencia, el pegamento que mantiene unida la lógica interna.

---

## ¿Por qué cada pieza del sistema debe tener un propósito único y claro?
Los sistemas frágiles suelen tener componentes "todoterreno" que asumen responsabilidades inconexas, lo que dificulta enormemente su comprensión y evolución.

### ¿Qué beneficios obtenemos al especializar nuestros componentes?
Un módulo altamente cohesivo es la piedra angular de un software mantenible:
- **Facilidad de Prueba**: Es más sencillo verificar que una pieza hace bien su única tarea.
- **Reutilización**: Es más probable que necesites una herramienta especializada en el futuro que una que haga mil cosas a medias.
- **Propósito Claro**: Reduce la carga cognitiva de los desarrolladores al presentar un contrato directo y sin efectos secundarios.

### ¿Qué niveles de cohesión existen en el diseño profesional?
Existen distintos niveles de cohesión, ordenados de mejor (más deseable) a peor:
1.  **Funcional (Ideal)**: El módulo realiza una única tarea bien definida.
2.  **Secuencial**: La salida de una parte sirve de entrada para otra —un flujo de datos puro—.
3.  **Comunicacional**: Todas las partes operan sobre el mismo conjunto de datos (ej. validar stock, calcular total y aplicar descuentos sobre el mismo objeto Pedido).
4.  **Procedimental**: Las partes se ejecutan en un orden específico pero pertenecen a responsabilidades distintas. Aquí suele caer el **Antipatrón de Descomposición Funcional** (clases-verbo) detectado en [[Principios de Diseño OO]].
 Aquí suele caer el **Antipatrón de Descomposición Funcional** (clases-verbo).

### DELTA
- Vinculado el Antipatrón de Descomposición Funcional con el nivel de Cohesión Procedural.
5.  **Temporal**: Actividades agrupadas solo porque ocurren al mismo tiempo (ej. una clase `inicializarSistema`).
6.  **Lógica**: Realiza funciones parecidas pero seleccionadas por un parámetro de control (ej. un `switch` gigante que hace cosas distintas según un `String tipo`).
7.  **Coincidencial (Evitar)**: No hay relación real entre las partes; es un cajón de sastre (ej. clase `Utilidades` con `enviarEmail` y `calcularImpuesto`).

## ¿Qué niveles de cohesión podemos identificar?
No toda la cohesión es igual de buena. Existe una escala (de Larry Constantine) que nos permite evaluar la calidad de un módulo:

| Nivel | Tipo | Descripción | Calidad |
| :--- | :--- | :--- | :--- |
| **7** | **Funcional** | El módulo hace una sola cosa bien definida. | **Óptima** |
| **6** | **Secuencial** | La salida de una parte es la entrada de la siguiente. | Muy buena |
| **5** | **Comunicacional** | Varias funciones operan sobre los mismos datos. | Buena |
| **4** | **Procedimental** | Funciones agrupadas por una secuencia de ejecución. | Regular |
| **3** | **Temporal** | Funciones que se ejecutan al mismo tiempo (ej. `init()`). | Pobre |
| **2** | **Lógica** | Funciones relacionadas por categoría pero no por flujo. | Mala |
| **1** | **Coincidental** | No hay relación alguna entre las partes del módulo. | **Nula** |

### ¿Cuándo es aceptable una cohesión menor?
Existen casos justificados —compromisos de ingeniería— donde se tolera una cohesión más baja:
- **Clases de Utilidad**: (Ej. `java.lang.System`) Agrupan servicios de bajo nivel para facilitar el acceso, aunque no tengan relación funcional.
- **Servidores Distribuidos (Fachadas)**: Se agrupan operaciones heterogéneas para reducir el número de llamadas remotas (latencia) en sistemas distribuidos.

---

### ¿Cómo identificamos la falta de cohesión?
Existen señales claras —*code smells*— que indican que una clase está asumiendo demasiadas responsabilidades:
- **Envidia de Características**: Cuando un método parece más interesado en los datos de otra clase que en los propios.
- **Clase de Datos**: Contiene solo atributos y getters/setters sin comportamiento real que encapsule reglas de negocio.
- **Cambios Divergentes**: Una clase cambia por múltiples razones no relacionadas entre sí.
- **Cirugía con Escopeta**: Un solo cambio conceptual requiere modificar muchas clases distintas (indica responsabilidades fragmentadas).
- **Grupo de Datos**: Los mismos campos aparecen siempre juntos en distintos lugares; deberían ser su propia clase.
- **Obsesión por Tipos Primitivos**: Uso excesivo de primitivos en lugar de pequeñas clases de dominio cohesivas.

**La regla de oro:** El software debe ser como un equipo de especialistas: cada uno sabe hacer su trabajo a la perfección y delega todo lo demás.

---

## ¿De qué manera podemos elevar el nivel de especialización de nuestro código?
La alta cohesión se alcanza mediante la refactorización constante y la vigilancia de las responsabilidades de cada clase.

### ¿Qué técnicas de refactorización nos ayudan a separar responsabilidades?
- **Extraer Método**: Si un método hace demasiadas cosas, descompónlo en pasos con nombres significativos.
- **Extraer Clase**: Si una clase acumula responsabilidades de distintas áreas —ej. lógica de negocio y persistencia—, sepáralas sin miedo.
- **Introducir Objeto-Parámetro**: Si pasas demasiados datos relacionados entre funciones, agrúpalos en una clase que les dé sentido.

### ¿En qué escenarios es aceptable relajar la regla de la cohesión única?
Existen casos excepcionales donde se acepta una cohesión menor por razones operativas o de rendimiento:
- **Clases de Utilidad**: Como `java.lang.System`, que agrupa servicios de bajo nivel dispersos para facilitar el acceso global.
- **Fachadas (Gateways)**: En arquitecturas de microservicios o sistemas distribuidos, para reducir la latencia al agrupar varias llamadas en una sola transacción.

---

## Referencias
1. **Mmasias**. *idsw2: Cohesión*. [GitHub Repository](https://github.com/mmasias/idsw2) y en copia local: [[500 Biblioteca/idsw2/temario/02-diseñoModular/cohesion.md|Teoría de Cohesión]].
