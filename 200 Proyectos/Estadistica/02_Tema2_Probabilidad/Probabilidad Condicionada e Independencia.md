# Probabilidad Condicionada e Independencia

Conceptos para cuando la ocurrencia de un evento afecta a la de otro.

## Probabilidad Condicionada
La probabilidad de que ocurra $A$ dado que ya ha ocurrido $B$ se define como:
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

> [!WARNING]
> **Error Frecuente**: Confundir probabilidad condicionada ($P(A|B)$) con la intersección ($P(A \cap B)$).
> - En la **intersección**, medimos la probabilidad respecto al espacio muestral total ($P(E)=1$).
> - En la **condicionada**, el espacio muestral se reduce a $B$, y medimos la probabilidad respecto a $P(B)$.

## Independencia Estadística
Dos sucesos $A$ y $B$ son **independientes** si la ocurrencia de uno no afecta la probabilidad del otro:
$$P(A|B) = P(A) \quad \text{o bien} \quad P(A \cap B) = P(A) \cdot P(B)$$

### Sucesos Dependientes
Si $P(A|B) \neq P(A)$, entonces los sucesos están condicionados o son dependientes.

---
Enlace: [[Index|Tema 2]]
Tags: #estadistica #probabilidad #condicionada
