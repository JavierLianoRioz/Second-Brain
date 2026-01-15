# Operaciones con Datos Numéricos

Reglas fundamentales para el manejo de precisión en cálculos estadísticos.

## Redondeo
- Se redondea al número más cercano.
- **Caso de empate (x,x5)**: Se redondea al **par más cercano** (ej: 43,45 $\to$ 43,4; 43,55 $\to$ 43,6).

## Cifras Significativas
Dígitos exactos de un número, excluyendo ceros usados solo para posicionar el separador decimal.
- Ej: `0,042` tiene 2 cifras significativas (`4,2 x 10^-2`).
- Ej: `0,04200` tiene 4 cifras significativas.

## Precisión en Cálculos
- **Sumas y Restas**: El resultado no puede tener más decimales que el término con menos decimales.
- **Multiplicación, División y Raíces**: El resultado no puede tener más cifras significativas que el término con menos cifras significativas.
- **Regla general**: Usar una cifra significativa extra en cálculos intermedios.

---
Enlace: [Tema 1](../Index.md)
Tags: #estadistica #matematicas
