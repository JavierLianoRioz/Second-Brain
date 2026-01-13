# Medidas de Dispersión

Indican cuánto se alejan los datos respecto a las medidas de centralización (qué tan "esparcidos" están).

## 1. Varianza ($S^2$)
Promedio de los cuadrados de las desviaciones respecto a la media.
$$S^2 = \frac{\sum (x_i - \bar{x})^2 \cdot n_i}{n}$$

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

---
Enlace: [[Index|Tema 1]]
Tags: #estadistica #dispersion #varianza
