# Contraste para Proporciones

Se utiliza para determinar si la proporción de una característica en una población ($P$) coincide con un valor esperado ($p_0$).

## 1. Hipótesis
- **H₀:** $P = p_0$
- **H₁:** $P \neq p_0$ (o contrastes unilaterales).

## 2. Estadístico de Prueba (Aproximación Normal)
Para muestras suficientemente grandes ($n \cdot p > 5$ y $n \cdot q > 5$), se utiliza la distribución **Z**:
$$Z = \frac{p - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}$$

Se compara con el valor crítico $Z_{1-\alpha/2}$ de la tabla Normal Estándar.

Donde:
- **$p$**: Proporción observada en la muestra ($x/n$).
- **$p_0$**: Proporción teórica bajo la hipótesis nula.

## 3. Interpretación
- Un valor de **Z** muy alejado de 0 (habitualmente $> 1.96$ para $\alpha=0.05$) lleva al rechazo de $H_0$.
- La decisión final se basa en si el **p-valor** obtenido es menor que el nivel de significación $\alpha$.

---
Enlace: [Tema 4](../Index.md)
Tags: #estadistica #contraste #proporciones #z-test
