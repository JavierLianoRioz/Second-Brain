---
title: "Método de Euler"
category: "Matemáticas Numéricas"
moc: "[[Matemáticas Numéricas]]"
---

# Método de Euler

## 🧠 Resumen / Punto Clave
El método de Euler es el procedimiento más simple para resolver numéricamente un Problema de Valor Inicial (PVI). Utiliza la pendiente de la función en un punto para aproximar el siguiente valor mediante una línea recta.

## 📝 Desarrollo / Explicación

### 1. Definición del PVI
Dado $\frac{dy}{dt} = f(t, y)$ con $y(a) = \alpha$, en el intervalo $[a, b]$.

### 2. Derivación y Algoritmo
Utilizando el Polinomio de Taylor de primer grado:
$$w_{i+1} = w_i + h f(t_i, w_i)$$
Donde:
- $h = (b-a)/N$ es el tamaño de paso.
- $t_i = a + i h$.
- $w_i$ es la aproximación de $y(t_i)$.

### 3. Error
- **Error de truncamiento local**: $O(h^2)$.
- **Error de truncamiento global**: $O(h)$.
Es un método de **primer orden**.

## 📊 Geometría del Método (Mermaid)
```mermaid
graph LR
    Ti["Punto Actual ti, wi"] -->|Tangente f_ti_wi| Tip1["Siguiente Punto ti+1, wi+1"]
    Tip1 -->|Iterar| Next[...]
    style Ti fill:#f9f,stroke:#333
```

## 💡 Ejemplos / Casos de uso
- Se utiliza como base conceptual para métodos más avanzados.
- **Inestabilidad**: Puede ser muy inestable si el tamaño de paso $h$ no es lo suficientemente pequeño.

## 🔗 Conexiones
- [MOC Matemáticas Numéricas](../Matemáticas%20Numéricas.md)
- [Métodos de Taylor](Taylor.md)
- [Métodos de Runge-Kutta](Runge_Kutta.md)
