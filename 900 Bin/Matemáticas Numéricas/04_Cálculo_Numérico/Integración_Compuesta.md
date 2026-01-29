---
title: "Integración Numérica Compuesta"
category: "Matemáticas Numéricas"
moc: "[[Matemáticas Numéricas]]"
---

# Integración Numérica Compuesta

## 🧠 Resumen / Punto Clave
Las fórmulas simples de Newton-Cotes se vuelven inexactas en intervalos grandes. La integración compuesta divide el intervalo $[a, b]$ en $n$ subintervalos pequeños y aplica una regla simple en cada uno, sumando luego los resultados.

## 📝 Desarrollo / Explicación

### 1. Regla del Trapecio Compuesta
Para $n$ subintervalos de ancho $h = (b-a)/n$:
$$\int_{a}^{b} f(x) dx \approx \frac{h}{2} [f(a) + 2 \sum_{j=1}^{n-1} f(x_j) + f(b)]$$
- **Error**: $-\frac{(b-a)h^2}{12} f''(\mu)$.

### 2. Regla de Simpson Compuesta
Requiere $n$ par.
$$\int_{a}^{b} f(x) dx \approx \frac{h}{3} [f(a) + 2 \sum_{j=1}^{n/2-1} f(x_{2j}) + 4 \sum_{j=1}^{n/2} f(x_{2j-1}) + f(b)]$$
- **Error**: $-\frac{(b-a)h^4}{180} f^{(4)}(\mu)$.

## 📊 Propiedades (Mermaid)
```mermaid
graph LR
    Simple[Regla Simple] -->|Divide Intervalo| Compuesta[Regla Compuesta]
    Compuesta -->|Aumentar n| Precision[Aumenta Precisión]
    Precision -->|h disminuye| Stability[Estabilidad Numérica]
```

## 💡 Ejemplos / Casos de uso
- Es el estándar para integrar funciones continuas sobre dominios extensos.
- **Estrategia**: Se suele aumentar $n$ hasta que la diferencia entre dos iteraciones consecutivas sea menor que la tolerancia deseada.

## 🔗 Conexiones
- [MOC Matemáticas Numéricas](../Matemáticas%20Numéricas.md)
- [Reglas de Newton-Cotes](Newton_Cotes.md)
- [Cuadratura Gaussiana](Cuadratura_Gaussiana.md)
