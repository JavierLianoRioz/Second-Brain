# Intervalos de Confianza para Medias y Proporciones

## 1. Para la Media ($\mu$)
### Caso 1: Varianza $\sigma^2$ conocida
Poco práctico, usa la distribución Normal $Z$.
$$\mu = \bar{x} \pm Z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

### Caso 2: Varianza $\sigma^2$ desconocida (Caso General)
Se usa la cuasidesviación típica $\hat{s}$ y la distribución **t de Student** con $n-1$ grados de libertad.
$$\mu = \bar{x} \pm t_{n-1; \alpha/2} \cdot \frac{\hat{s}}{\sqrt{n}}$$

## 2. Para una Proporción ($p$)
Basado en la aproximación Normal.
$$P = p \pm Z_{1-\alpha/2} \sqrt{\frac{pq}{n}}$$
Donde $q = 1-p$. El error cometido es la parte de la derecha de la fórmula.

---
Enlace: [[Index|Tema 3]]
Tags: #estadistica #formulas #confianza
