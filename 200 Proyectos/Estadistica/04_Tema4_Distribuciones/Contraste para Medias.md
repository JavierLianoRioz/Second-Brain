# Contraste para Medias

Se utiliza para contrastar si la media de una población ($\mu$) es igual a un valor teórico determinado ($\mu_0$).

## 1. Hipótesis
- **H₀ (Nula):** $\mu = \mu_0$
- **H₁ (Alternativa):** $\mu \neq \mu_0$ (bidireccional) o $\mu > \mu_0$ / $\mu < \mu_0$ (unidireccional).

## 2. Estadístico de Prueba
Depende de si conocemos la varianza poblacional ($\sigma^2$) o no:

### Caso A: Varianza Conocida
Se utiliza la distribución **Normal Estándar (Z)**:
$$Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}$$

El valor crítico de comparación es **$Z_{1-\alpha/2}$**.

### Caso## 2. Estadístico de Prueba
Se basa en la distribución **Z** (Normal Estándar):
$$Z = \frac{p_1 - p_2}{\sqrt{p \cdot q \cdot (\frac{1}{n_1} + \frac{1}{n_2})}}$$

Este valor se compara con el valor crítico **$Z_{1-\alpha/2}$**.

El valor crítico de comparación es **$Z_{1-\alpha/2}$**.

### Caso B: Varianza Desconocida (Lo más común)
Se utiliza la **cuasidesviación típica ($\hat{s}$)** y la distribución **t de Student** con $n-1$ grados de libertad:
$$t = \frac{\bar{x} - \mu_0}{\hat{s} / \sqrt{n}}$$

## 3. Decisión
- Si el **p-valor < $\alpha$**, rechazamos $H_0$.
- Si el estadístico cae en la **región crítica** (definida por el nivel de significación $\alpha$), rechazamos $H_0$.

---
Enlace: [[Index|Tema 4]]
Tags: #estadistica #contraste #medias #t-student
