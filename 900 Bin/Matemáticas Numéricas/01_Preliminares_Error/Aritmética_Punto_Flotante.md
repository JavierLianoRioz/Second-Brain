---
title: "Aritmética de Punto Flotante"
category: "Matemáticas Numéricas"
moc: "[[Matemáticas Numéricas]]"
---

# Aritmética de Punto Flotante

## 🧠 Resumen / Punto Clave
Los ordenadores no usan números reales, sino una aproximación discreta llamada **Punto Flotante**. Esta representación introduce errores de redondeo inherentes debido a que la mantisa tiene un tamaño limitado.

## 📝 Desarrollo / Explicación

### 1. Representación Normalizada
Cualquier número real $x \neq 0$ se puede escribir como:
$$
x = \sigma \cdot m \cdot \beta^E
$$
Donde:
- $\sigma$: Signo ($\pm 1$).
- $m$: Mantisa (fracción), con $1 \leq m < \beta$.
- $\beta$: Base (generalmente 2 o 10).
- $E$: Exponente.

### 2. Estándar IEEE 754 (Doble Precisión)
El formato de 64 bits se distribuye de la siguiente manera:

## 📊 Estructura de Memoria (64 bits)
```mermaid
flowchart LR
    S[Signo: 1 bit] --- E[Exponente: 11 bits] --- M[Mantisa: 52 bits]
```

### 3. Épsilon de la Máquina ($\epsilon_{mach}$)
Es el número más pequeño tal que $1 + \epsilon > 1$. Define la precisión relativa del sistema.
- Para doble precisión: $\epsilon \approx 2.22 \times 10^{-16}$.

## 💡 Ejemplo / Aplicación
En Python/C++, sumar $0.1 + 0.2$ no da exactamente $0.3$ debido a que $0.1$ no tiene una representación binaria finita exacta, lo que genera un error de redondeo en el bit 53.

## 🔗 Conexiones
- [MOC Matemáticas Numéricas](../Matemáticas%20Numéricas.md)
- [Errores de Redondeo y Truncamiento](Errores_Redondeo_Truncamiento.md)
