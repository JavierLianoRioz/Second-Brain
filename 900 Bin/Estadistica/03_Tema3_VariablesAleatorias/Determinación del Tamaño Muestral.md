# Determinación del Tamaño Muestral

Cálculo de cuántos elementos ($n$) se necesitan para obtener una precisión deseada.

## Precisión (Error máximo $d$)
Es el margen de error que estamos dispuestos a aceptar en nuestra estimación.

## Fórmulas para el cálculo de $n$
- **Para estimar la media ($\mu$):**
$$n \geq \left( \frac{Z_{1-\alpha/2} \cdot \hat{s}}{d} \right) ^2$$

- **Para estimar la proporción ($p$):**
$$n \geq \frac{Z_{1-\alpha/2}^2 \cdot p \cdot q}{d^2}$$

*Nota: Si no se conoce $p$, se puede usar el caso más desfavorable ($p=0,5$, $q=0,5$) para maximizar el tamaño de la muestra.*

---
Enlace: [Tema 3](../Index.md)
Tags: #estadistica #muestreo #formulas
