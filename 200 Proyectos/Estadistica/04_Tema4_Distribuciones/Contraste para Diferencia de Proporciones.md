# Contraste para Diferencia de Proporciones

Se utiliza para comparar dos proporciones de éxito ($P_1$ y $P_2$) de dos poblaciones independientes (ej: efectividad de dos fármacos).

## 1. Hipótesis
- **H₀:** $P_1 = P_2$
- **H₁:** $P_1 \neq P_2$

## 2. Estadístico de Prueba
Se basa en la distribución **Z** (Normal Estándar):
$$Z = \frac{p_1 - p_2}{\sqrt{p \cdot q \cdot (\frac{1}{n_1} + \frac{1}{n_2})}}$$

Donde **$p$** es la proporción combinada de ambas muestras.

## 3. Decisión
- **Rechazar H₀** si el **p-valor < $\alpha$**.
- Si el p-valor es mayor que $\alpha$, concluimos que no hay evidencia suficiente para decir que las proporciones son distintas.

---
Enlace: [[Index|Tema 4]]
Tags: #estadistica #contraste #proporciones #comparacion
