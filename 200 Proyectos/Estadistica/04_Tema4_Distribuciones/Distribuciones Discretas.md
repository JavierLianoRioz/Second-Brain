# Distribuciones Discretas

Las distribuciones discretas se utilizan cuando la variable aleatoria solo puede tomar valores aislados (enteros).

## 1. Distribución Binomial ($BIN(n, p)$)
Se aplica a experimentos dicotómicos (éxito/fracaso) repetidos un número fijo de veces ($n$).
- **Parámetros**:
    - $n$: número de ensayos.
    - $p$: probabilidad de éxito.
    - $q = 1 - p$: probabilidad de fracaso.
- **Fórmulas**:
    - **Probabilidad exacta**: $P(X=k) = \binom{n}{k} p^k q^{n-k}$
    - **Esperanza (Media)**: $\mu = n \cdot p$
    - **Varianza**: $\sigma^2 = n \cdot p \cdot q$
- **Requisito**: Usualmente $p > 0.1$.

## 2. Distribución de Poisson
Se aplica a eventos que ocurren en un intervalo específico (tiempo, área, etc.) o "sucesos raros".
- **Parámetros**:
    - $\mu$ (o $\lambda$): media de ocurrencias en el intervalo.
- **Fórmulas**:
    - **Probabilidad exacta**: $P(X=k) = \frac{e^{-\mu} \cdot \mu^k}{k!}$
    - **Esperanza y Varianza**: $\mu = \sigma^2$
- **Aproximación**: Se usa como aproximación de la Binomial cuando $n > 30$ y $p < 0.1$ ($\mu = n \cdot p$).

---
Enlace: [Tema 4](../Index.md)
Tags: #estadistica #probabilidad #binomial #poisson
