---
title: "Polinomios de Lagrange"
category: "Matemáticas Numéricas"
moc: "[[Matemáticas Numéricas]]"
---

# Polinomios de Lagrange

## 🧠 Resumen / Punto Clave
La interpolación de Lagrange es un método para encontrar un polinomio de grado $n$ que pasa exactamente por $n+1$ puntos dados. Se construye como una combinación lineal de polinomios base llamados **coeficientes de Lagrange**.

## 📝 Desarrollo / Explicación

### 1. Definición del Polinomio
Dados $(n+1)$ puntos distintos $(x_0, y_0), \dots, (x_n, y_n)$, el polinomio de Lagrange $P(x)$ se define como:
$$P(x) = \sum_{i=0}^{n} f(x_i) L_{n,i}(x)$$
Donde $L_{n,i}(x)$ son los polinomios base de Lagrange:
$$L_{n,i}(x) = \prod_{j=0, j \neq i}^{n} \frac{x - x_j}{x_i - x_j}$$

### 2. Propiedades de los Coeficientes
- $L_{n,i}(x_j) = 1$ si $i=j$.
- $L_{n,i}(x_j) = 0$ si $i \neq j$.

### 3. Error de Interpolación
Si $f \in C^{n+1}[a, b]$, para cada $x \in [a, b]$ existe $\xi$ en $(a, b)$ tal que:
$$f(x) = P(x) + \frac{f^{(n+1)}(\xi)}{(n+1)!} \prod_{i=0}^{n} (x - x_i)$$

## 📊 Concepto de Interpolación (Mermaid)
```mermaid
graph LR
    Points["Puntos x0, x1, ..., xn"] --> Base["Polinomios Base L_ni"]
    Base --> Sum["Suma Puesta f(xi) * L_ni"]
    Sum --> Result["Polinomio de Interpolación P(x)"]
```

## 💡 Ejemplos / Casos de uso
- Útil para interpolar datos con pocos puntos o cuando se requiere una forma explícita del polinomio.
- **Desventaja**: Si se añade un nuevo punto, hay que recalcular todos los coeficientes $L_{n,i}$ (para evitar esto se usa el método de Newton).

## 🔗 Conexiones
- [MOC Matemáticas Numéricas](../Matemáticas%20Numéricas.md)
- [Diferencias Divididas de Newton](Diferencias_Divididas.md)
- [Interpolación de Hermite](Hermite.md)
