# Test Chi-cuadrado e Independencia

Se utiliza para determinar si existe una relación estadísticamente significativa entre dos variables cualitativas a partir de una tabla de contingencia.

## 1. Tabla de Contingencia (Observed Frequencies)
Los datos se organizan en filas ($R$) y columnas ($C$). Cada casilla contiene la frecuencia observada ($O_{ij}$).

## 2. Frecuencias Esperadas ($E_{ij}$)
Representan qué valores habría si las variables fueran totalmente independientes:
$$E_{ij} = \frac{\text{Total Fila } i \cdot \text{Total Columna } j}{\text{Total Global } (n)}$$

## 3. Estadístico Chi-cuadrado ($\chi^2$)
Mide la discrepancia entre lo observado y lo esperado:
$$\chi^2 = \sum \frac{(O_{ij} - E_{ij})^2}{E_{ij}}$$
- **Grados de Libertad ($gl$):** $gl = (R-1) \cdot (C-1)$

## 4. Regla de Decisión
- **Hipótesis Nula ($H_0$):** Las variables son **Independientes** (no hay relación).
- **Hipótesis Alternativa ($H_1$):** Las variables están **Relacionadas** (hay asociación).
- Si el p-valor $< \alpha$ (normalmente 0.05), rechazamos $H_0$ y concluimos que hay una relación significativa.

---
Enlace: [Tema 4](../Index.md)
Tags: #estadistica #chi-cuadrado #independencia #contingencia
