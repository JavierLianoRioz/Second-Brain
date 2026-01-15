# Contraste para Diferencia de Proporciones

Se utiliza para comparar dos proporciones de éxito ($P_1$ y $P_2$) de dos poblaciones independientes (ej: efectividad de dos fármacos).

## 1. Hipótesis
- **H₀:** $P_1 = P_2$
- **H₁:** $P_1 \neq P_2$

## 2. Estadístico de Prueba
Se basa en la distribución **Z** (Normal Estándar):
$$Z_{exp} = \frac{\widehat{P}_1 - \widehat{P}_2 - \Delta}{\sqrt{\frac{\widehat{p}_1 \widehat{q}_1}{n_1} + \frac{\widehat{p}_2 \widehat{q}_2}{n_2}}}$$

Este valor se compara con el valor crítico **$Z_{1-\alpha/2}$**.
- **$\Delta$**: Diferencia esperada (habitualmente 0).
- **$\widehat{p}, \widehat{q}$**: Proporción de éxitos y fracasos de cada muestra.

## 3. Decisión
- **Rechazar H₀** si el **p-valor < $\alpha$**.
- Si el p-valor es mayor que $\alpha$, concluimos que no hay evidencia suficiente para decir que las proporciones son distintas.

---
Enlace: [Tema 4](../Index.md)
Tags: #estadistica #contraste #proporciones #comparacion
