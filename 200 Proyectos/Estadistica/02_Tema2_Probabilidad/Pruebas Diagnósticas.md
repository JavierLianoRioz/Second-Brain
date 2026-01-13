# Pruebas Diagnósticas

El estudio de la validez de una prueba diagnóstica se basa en la comparación de sus resultados con un "Criterio de Referencia" (Gold Standard).

## 1. Parámetros de la Prueba
- **Sensibilidad ($S$):** Probabilidad de que la prueba sea positiva dado que el individuo está enfermo.
    - $S = P(+|E)$
- **Especificidad ($E$):** Probabilidad de que la prueba sea negativa dado que el individuo está sano.
    - $E = P(-|S)$

## 2. Valores Predictivos (Probabilidades a Posteriori)
Calculados normalmente mediante el **Teorema de Bayes**:
- **Valor Predictivo Positivo (VPP):** Probabilidad de estar enfermo sabiendo que se ha dado positivo.
    - $VPP = P(E|+)$
- **Valor Predictivo Negativo (VPN):** Probabilidad de estar sano sabiendo que se ha dado negativo.
    - $VPN = P(S|-)$

## 3. Falsos Resultados
- **Falso Positivo (FP):** Sujeto sano que da positivo ($1 - E$).
- **Falso Negativo (FN):** Sujeto enfermo que da negativo ($1 - S$).

*Nota: El VPP y VPN dependen fuertemente de la **Prevalencia** (proporción de enfermos en la población). A menor prevalencia, mayor probabilidad de que un positivo sea falso.*

---
Enlace: [[Index|Tema 2]]
Tags: #estadistica #diagnostico #sensibilidad #especificidad #bayes
