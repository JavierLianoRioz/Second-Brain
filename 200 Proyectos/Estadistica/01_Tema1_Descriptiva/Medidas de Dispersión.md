# Medidas de Dispersión

Indican cuánto se alejan los datos respecto a las medidas de centralización (qué tan "esparcidos" están).

## 1. Varianza ($S^2$)
Promedio de los cuadrados de las desviaciones respecto a la media.
$$S^2 = \frac{\sum (x_i - \bar{x})^2 \cdot n_i}{n} = \frac{\sum x_i^2 \cdot n_i}{n} - \bar{x}^2$$

> [!NOTE]
> **Datos agrupados (Intervalos):** Para calcular la varianza en tablas con intervalos, se utiliza la **marca de clase** ($x_i$, el punto medio del intervalo) como valor representativo de cada grupo.

## 2. Desviación Típica ($S$)
Es la raíz cuadrada de la varianza. Tiene las mismas unidades que la variable original.
$$S = \sqrt{S^2}$$

## 3. Cuasivarianza ($\hat{s}^2$) y Cuasidesviación Típica ($\hat{s}$)
Usadas como estimadores insesgados en inferencia estadística. Utilizan $n-1$ en el denominador.
$$\hat{s}^2 = \frac{\sum (x_i - \bar{x})^2 \cdot n_i}{n-1}$$
$$\hat{s} = \sqrt{\hat{s}^2}$$

## 3. Coeficiente de Variación ($CV$)
Mide la dispersión relativa (%) y permite comparar la variabilidad entre diferentes poblaciones o magnitudes.
$$CV = \frac{S}{|\bar{x}|} \cdot 100$$

## 4. Rango o Recorrido
Diferencia entre el valor máximo y el mínimo ($V_{max} - V_{min}$).

## 5. Rango Intercuartílico ($IQR$)
Mide la dispersión del 50% central de los datos. Es robusto frente a atípicos.
$$IQR = Q_3 - Q_1$$

## 6. Detección de Atípicos (Criterio de Tukey)
Permite identificar valores numéricamente distantes del resto de la muestra:
- **Límite Inferior**: $LI = Q_1 - 1.5 \cdot IQR$
- **Límite Superior**: $LS = Q_3 + 1.5 \cdot IQR$

*Todo valor fuera del intervalo $[LI, LS]$ se considera un valor atípico (outlier).*

---
Enlace: [[Index|Tema 1]]
Tags: #estadistica #dispersion #varianza
