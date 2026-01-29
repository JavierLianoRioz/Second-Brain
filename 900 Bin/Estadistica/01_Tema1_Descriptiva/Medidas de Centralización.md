# Medidas de Centralización

Resumen la información de la muestra mediante un valor numérico que suele situarse en el **centro** de la distribución.

## 1. Media Aritmética ($\bar{x}$)
Es el promedio de los valores.
$$\bar{x} = \frac{\sum x_i \cdot n_i}{n}$$
- **Ventaja**: Usa toda la información.
- **Inconveniente**: Muy sensible a valores extremos (atípicos).

## 2. Mediana ($Me$ o $Q_2$)
Valor que deja el 50% de los datos por debajo y el 50% por arriba.
- No se ve afectada por valores extremos.

## 3. Moda ($Mo$)
Es el valor (o modalidad) con mayor frecuencia absoluta ($n_i$).
- Puede haber más de una moda (unimodal, bimodal, etc.).

### Moda en Datos Agrupados (Intervalos)
Se busca el **Intervalo Modal** (el de mayor $n_i$) y se interpola:
$$Mo = L_i + \frac{d_1}{d_1 + d_2} \cdot c_i$$

Donde:
- **$d_1$**: Diferencia entre la frecuencia modal y la anterior ($n_i - n_{i-1}$).
- **$d_2$**: Diferencia entre la frecuencia modal y la siguiente ($n_i - n_{i+1}$).
- **$L_i$**: Límite inferior del intervalo modal.
- **$c_i$**: Amplitud del intervalo.

---
Enlace: [Tema 1](../Index.md)
Tags: #estadistica #centralizacion #media
