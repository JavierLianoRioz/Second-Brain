# Medidas de Posición (Cuantiles)

Llamamos **cuantiles** ($C_\alpha$) a los valores de la variable que dividen a los datos en grupos con el mismo número de individuos.

## Tipos de Cuantiles
- **Cuartiles ($Q$)**: Dividen los datos en 4 grupos (25% cada uno).
    - $Q_1$ (Cuartil 1): Deja debajo el 25% de los datos.
    - $Q_2$ (Mediana): Deja debajo el 50% de los datos.
    - $Q_3$ (Cuartil 3): Deja debajo el 75% de los datos.
- **Percentiles ($P$)**: Dividen los datos en 100 grupos (1% cada uno).
    - Ejemplo: $P_{85}$ deja debajo el 85% de los datos.

## Cálculo de Cuantiles
1. Ordenar los datos de menor a mayor.
2. Calcular el índice $i = n \cdot \alpha$ (donde $n$ es el tamaño de muestra y $\alpha$ el orden del cuantil).
    - Si $i$ no es entero: $i = \lceil i \rceil$
    - Si $i$ es entero: 
	    - Si $i$ es par: $C_\alpha = \frac{X_{(i)} + X_{(i+1)}}{2}$
	    - Si $i$ es impar: $C_\alpha = X_{(i)}$

## Rango Intercuartílico ($IQR$)
Es la diferencia entre el tercer y el primer cuartil:
$$IQR = Q_3 - Q_1$$
Mide la dispersión del 50% central de los datos y se usa para detectar **valores atípicos** (outliers).

---
Enlace: [[Index|Tema 1]]
Tags: #estadistica #posicion #cuantiles
