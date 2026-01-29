# Inferencia sobre Diferencias

Permite comparar dos poblaciones a partir de sus muestras.

## Diferencia de Medias (Muestras Independientes)
Se utiliza para determinar si las medias de dos poblaciones independientes son iguales.
- **IC:** $(\bar{x}_1 - \bar{x}_2) \pm t_{n+m-2; \alpha/2} \cdot SE$
- Si el intervalo **contiene al 0**, no hay diferencias significativas entre las medias.

## Diferencia de Proporciones (Muestras Independientes)
Estima la diferencia entre dos proporciones poblacionales ($P_1 - P_2$).
- **IC:** $(p_1 - p_2) \pm Z_{1-\alpha/2} \sqrt{\frac{p_1q_1}{n} + \frac{p_2q_2}{m}}$
- Si el **0 está en el intervalo**, las proporciones se consideran iguales estadísticamente.

## Datos Apareados (Muestras Dependientes)
Se da cuando medimos al **mismo individuo** en dos momentos distintos (ej: antes y después de un fármaco).
- **Lógica**: Se trabaja con la variable "Diferencia" ($D = X_{antes} - X_{después}$).
- **Test**: Se realiza un test de una sola muestra sobre las diferencias $D$.
- **Hipótesis**: $H_0: \mu_d = 0$ (no hay efecto).
- **IC para Medias Apareadas:** $\bar{d} \pm t_{n-1; \alpha/2} \frac{\hat{s}_d}{\sqrt{n}}$
- **Test de McNemar**: Versión para proporciones apareadas (tablas de cambio).
  - Se fija en los casos discordantes ($A$ y $D$ en la tabla de cambio).
  - $\chi^2 = \frac{(|A - D| - 1)^2}{A + D}$

---
Enlace: [Tema 3](../Index.md)
Tags: #estadistica #comparativa #inferencia
