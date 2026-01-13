# Regresión Lineal

La regresión es un conjunto de técnicas numéricas encaminadas a encontrar la ecuación de una función que permita predecir el valor de una variable dependiente ($Y$) a partir de una o varias variables independientes ($X$).

## 1. Modelo de Regresión Lineal Simple (MRLS)
Es la forma más simple de regresión, donde la relación entre las variables se explica mediante una línea recta:
$$y = a + bx + \epsilon$$

Donde:
- **$y$**: Variable dependiente (lo que queremos predecir).
- **$x$**: Variable independiente (explicativa).
- **$a$**: Ordenada en el origen (valor de $y$ cuando $x=0$).
- **$b$**: Pendiente de la recta (indica cuánto cambia $y$ por cada unidad que aumenta $x$).
- **$\epsilon$**: Error residual o de estimación ($Y_{observada} - Y_{estimada}$).

## 2. Cálculo de Coeficientes (Mínimos Cuadrados)
Para obtener la recta $y = a + bx$ que mejor ajusta los datos:
- **Pendiente ($b$):** $b = \frac{S_{xy}}{S_x^2}$
- **Ordenada en el origen ($a$):** $a = \bar{y} - b\bar{x}$

## 3. Correlación de Pearson ($r$)
Indica la fuerza y dirección de la relación lineal entre las variables.
$$r = \frac{S_{xy}}{S_x \cdot S_y}$$
- **$r = 1$ o $-1$**: Correlación perfecta (positiva o negativa).
- **$r = 0$**: Ausencia de relación lineal.
- **Relación intensa**: $|r| > 0.7$ (aproximadamente).

## 4. Bondad de Ajuste ($R^2$)
El coeficiente de determinación ($R^2$) es el cuadrado del coeficiente de Pearson ($R^2 = r^2$). Indica qué porcentaje de la variabilidad de $y$ es explicada por el modelo de regresión.
- Un $R^2$ cercano a 1 indica un ajuste excelente.
- Un $R^2$ cercano a 0 indica que el modelo no explica bien la relación.

## 4. Clasificación de Modelos
- **Simple**: Una sola variable independiente.
- **Múltiple**: Dos o más variables independientes.
- **Lineal**: La función es una línea recta.
- **No lineal**: La función sigue otra forma (curva, exponencial, etc.).

---
Enlace: [[Index|Tema 1]]
Tags: #estadistica #regresion #modelado
