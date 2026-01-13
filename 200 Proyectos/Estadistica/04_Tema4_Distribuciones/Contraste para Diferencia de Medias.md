# Contraste para Diferencia de Medias

Se utiliza para comparar si las medias de dos poblaciones independientes ($\mu_1$ y $\mu_2$) son significativamente distintas.

## 1. Hipótesis
- **H₀:** $\mu_1 = \mu_2$ (o $\mu_1 - \mu_2 = 0$)
- **H₁:** $\mu_1 \neq \mu_2$

## 2. Estadístico de Prueba (Varianzas Iguales)
Si asumimos que las varianzas poblacionales son desconocidas pero iguales (homocedasticidad), se utiliza la **t de Student** con $n_1 + n_2 - 2$ grados de libertad:
$$t = \frac{\bar{x}_1 - \bar{x}_2}{SE}$$

Donde **SE** (Error Típico) se calcula a partir de la cuasivarianza ponderada.

## 3. Relación con el Intervalo de Confianza
- Si el **Intervalo de Confianza** al $95\%$ para la diferencia de medias **contiene al 0**, no podemos rechazar $H_0$ (las medias son iguales).
- Si el **0 queda fuera**, rechazamos $H_0$ y afirmamos que existe una diferencia estadísticamente significativa.

---
Enlace: [[Index|Tema 4]]
Tags: #estadistica #contraste #medias #comparacion
