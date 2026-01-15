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

### 1. Datos Brutos (Lista de valores)
1. Ordenar los datos de menor a mayor.
2. Calcular la posición $i = n \cdot \alpha$ (donde $\alpha$ es $0.25, 0.50, 0.75$, etc.).
    - Si $i$ no es entero: Redondear al siguiente entero. El cuantil es el valor en esa posición.
    - Si $i$ es entero: El cuantil es la media entre el valor en la posición $i$ y la posición $i+1$.

### 2. Tablas de Frecuencia (Datos Discretos)
Se utiliza la columna de **Frecuencia Absoluta Acumulada ($N_i$)**:
1. Calcular el valor de posición $L = n \cdot \alpha$.
2. Buscar en la columna $N_i$:
    - **Si $L$ coincide exactamente con un $N_i$:** El cuantil es el valor de la variable $x_i$ (o la media entre $x_i$ y $x_{i+1}$ dependiendo de la rigurosad del test).
    - **Si $L$ no coincide:** Buscamos el primer $N_i$ que sea **estrictamente mayor** que $L$. El cuantil es el valor de $x_i$ correspondiente.

*Ejemplo: Si $n=20$ y buscamos $Q_1$ ($\alpha=0.25$), calculamos $L = 20 \cdot 0.25 = 5$. Si $N_2=5$, entonces $Q_1 = x_2$.*

### 3. Datos Agrupados (Intervalos)
Cuando los datos están en intervalos, el cuantil no es un valor exacto de la tabla, sino que se estima mediante **interpolación lineal**:

$$C_\alpha = L_i + \frac{\frac{n \cdot \alpha}{100} - N_{i-1}}{n_i} \cdot c_i$$

Donde:
- **$L_i$**: Límite inferior del intervalo donde se encuentra el cuantil.
- **$n \cdot \alpha$**: Valor de posición buscado.
- **$N_{i-1}$**: Frecuencia absoluta acumulada del intervalo anterior.
- **$n_i$**: Frecuencia absoluta del intervalo actual.
- **$c_i$**: Amplitud del intervalo ($LI - LS$).

## Rango Intercuartílico ($IQR$)
Es la diferencia entre el tercer y el primer cuartil:
$$IQR = Q_3 - Q_1$$
Mide la dispersión del 50% central de los datos y se usa para detectar **valores atípicos** (outliers).

---
Enlace: [Tema 1](../Index.md)
Tags: #estadistica #posicion #cuantiles
