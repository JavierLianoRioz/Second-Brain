# Simulacro de Examen - Modelo A

Este simulacro sigue fielmente la estructura de 4 ejercicios y los puntos críticos identificados en la guía.

## Ejercicio 1: Análisis Univariante (2.5 puntos)
Se ha medido el nivel de glucosa en sangre (mg/dl) de 15 pacientes en ayunas, obteniendo los siguientes valores:
**95, 102, 98, 110, 105, 92, 108, 200, 101, 99, 103, 107, 96, 104, 88**

1. Calcule la **Media** y la **Mediana**. Explique cuál de las dos es más representativa en este caso.
2. Determine los **Cuartiles (Q1, Q2, Q3)** y el **Rango Intercuartílico (IQR)**.
3. **Detección de Atípicos:** Utilice el **Criterio de Tukey** ($Q_1 - 1.5·IQR$ y $Q_3 + 1.5·IQR$) para determinar si existe algún valor anómalo en la muestra.
4. **Media Ponderada:** Si la nota final depende de tres pruebas con pesos del 30%, 30% y 40%, y un alumno obtiene 5, 7 y 6.5 respectivamente, calcule su nota media ponderada.

**Recursos relacionados:**
- [[01_Tema1_Descriptiva/Medidas de Centralización|Teoría: Media y Mediana]]
- [[01_Tema1_Descriptiva/Medidas de Posición (Cuantiles)|Teoría: Cuartiles y Percentiles]]
- [[01_Tema1_Descriptiva/Medidas de Dispersión|Teoría: Rango e IQR]]
- [[01_Tema1_Descriptiva/Operaciones con Datos Numéricos|Teoría: Media Ponderada]]

## Ejercicio 2: Modelado (2.5 puntos)
**Parte A (Distribución):** En un hospital, se sabe que el 8% de los pacientes operados sufren una complicación postoperatoria leve.
1. Si se operan **50 pacientes**, ¿cuál es el número esperado de complicaciones?
2. Calcule la probabilidad de que **exactamente 2** pacientes sufran complicaciones usando la aproximación de **Poisson** (justifique por qué es válida).

**Parte B (Regresión):** Se estudia la relación entre la edad (X) y la capacidad pulmonar (Y). Estadísticos calculados:
$n=20$; 
$\sum X=800$; 
$\sum Y=60$; 
$\bar{x}=40$; 
$\bar{y}=3.0$; 
$S_x=8$; 
$S_y=0.5$; 
$S_{xy}=-3.2$.
1. Calcule la **Ecuación de la Recta de Regresión**. ¿Qué indica el signo de la pendiente?
2. Calcule el **Coeficiente de Correlación de Pearson ($r$)** e interprete la intensidad de la relación.

**Recursos relacionados:**
- [[04_Tema4_Distribuciones/Distribuciones Discretas|Teoría: Binomial y Poisson]]
- [[01_Tema1_Descriptiva/Regresion Lineal|Teoría: Regresión Lineal]]

## Ejercicio 3: El Azar (2.5 puntos)
Se realiza un estudio sobre una enfermedad rara que afecta al **1%** de la población. Se dispone de una prueba con:
- **Sensibilidad (S) = 98%**
- **Especificidad (E) = 95%**

1. Dibuje el **árbol de probabilidades** o describa las probabilidades totales.
2. Calcule la probabilidad de que una persona elegida al azar dé **positivo** en la prueba.
3. Si un paciente da positivo, ¿cuál es la probabilidad de que **realmente esté sano**? (Falso Positivo).

**Recursos relacionados:**
- [[02_Tema2_Probabilidad/Teorema de la Probabilidad Total y Bayes|Teoría: Probabilidad Total y Bayes]]
- [[02_Tema2_Probabilidad/Probabilidad Condicionada e Independencia|Teoría: Condicional y Falsos Positivos]]

## Ejercicio 4: La Decisión - Híbrido Inferencia (2.5 puntos)
Se quiere comparar la efectividad de dos analgésicos (A y B) para reducir el dolor en pacientes con migraña crónica.
- **Grupo A (n=200):** 62 pacientes experimentaron una mejora significativa ($p_A = 0.31$).
- **Grupo B (m=350):** 38 pacientes experimentaron una mejora significativa ($p_B = 0.108$).

1. Construya un **Intervalo de Confianza al 95%** para la **diferencia de proporciones** ($P_A - P_B$).
2. **Decisión:** A la vista del IC obtenido (¿contiene el cero?), ¿se puede afirmar que el analgésico A es significativamente más eficaz que el B?
3. Explique qué significa que el resultado sea **"Estadísticamente Significativo"** en términos de p-valor y nivel de significación ($\alpha = 0.05$).
4. **Tamaño Muestral:** Si quisiéramos repetir el estudio con el analgésico A para tener un error máximo en la estimación de la proporción del **3%** con un 95% de confianza, ¿cuál debería ser el tamaño de la muestra ($n$)?

**Recursos relacionados:**
- [[03_Tema3_VariablesAleatorias/Inferencia sobre Diferencias|Teoría: Diferencia de Proporciones]]
- [[04_Tema4_Distribuciones/Metodología del Contraste de Hipótesis|Teoría: Pasos para la Decisión]]
- [[04_Tema4_Distribuciones/p-value (Nivel Crítico)|Teoría: Significado del P-Value]]

---
> [!IMPORTANT]
> **Dato Clave:** Para el Ejercicio 4, recuerda que si el Cero **NO** está en el intervalo de la diferencia, entonces **SÍ** hay diferencias significativas entre los dos grupos.
