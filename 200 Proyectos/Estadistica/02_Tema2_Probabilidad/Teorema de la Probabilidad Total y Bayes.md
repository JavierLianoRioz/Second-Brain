# Teorema de la Probabilidad Total y Bayes

Herramientas para calcular probabilidades en sistemas complejos.

## Teorema de la Probabilidad Total
Si tenemos un sistema exhaustivo y excluyente de sucesos ($A_1, A_2, \dots, A_n$), la probabilidad de cualquier suceso $B$ se puede calcular como la suma de sus intersecciones con cada $A_i$:
$$P(B) = \sum_{i=1}^n P(A_i) \cdot P(B|A_i)$$
Permite descomponer un problema complejo en subproblemas más simples.

## Teorema de Bayes
Permite calcular la probabilidad "a posteriori", es decir, la probabilidad de que haya ocurrido una causa $A_i$ dado que se ha observado el efecto $B$:
$$P(A_i|B) = \frac{P(A_i) \cdot P(B|A_i)}{P(B)}$$
Donde $P(B)$ se calcula usualmente mediante el Teorema de la Probabilidad Total.

---
Enlace: [[Index|Tema 2]]
Tags: #estadistica #probabilidad #bayes
