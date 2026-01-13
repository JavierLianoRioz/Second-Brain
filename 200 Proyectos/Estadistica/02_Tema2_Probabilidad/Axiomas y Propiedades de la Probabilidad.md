# Axiomas y Propiedades de la Probabilidad

Reglas fundamentales que rigen cualquier función de probabilidad.

## Axiomas de Kolmogorov
Cualquier función de probabilidad $P$ que asigne un valor $P(A)$ a un suceso $A$ debe verificar:
1. **$0 \leq P(A) \leq 1$**: La probabilidad es siempre un número real en este intervalo.
2. **$P(E) = 1$**: La probabilidad del suceso seguro es 1.
3. **Sucesos Excluyentes**: Si $A$ y $B$ son excluyentes ($A \cap B = \emptyset$), entonces $P(A \cup B) = P(A) + P(B)$.

## Propiedades Derivadas
- **Suceso Complementario**: $P(A') = 1 - P(A)$.
- **Suceso Imposible**: $P(\emptyset) = 0$.
- **Inclusión**: Si $A \subset B$, entonces $P(A) \leq P(B)$.
- **Unión General (No Excluyentes)**: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.

---
Enlace: [[Index|Tema 2]]
Tags: #estadistica #probabilidad #axiomas
