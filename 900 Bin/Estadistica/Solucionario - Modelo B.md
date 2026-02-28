# Solucionario: Simulacro de Examen - Modelo B

## Ejercicio 1: Estadística Descriptiva (2.5 puntos)

### 1. Tabla de Frecuencias
| Intervalo | $x_i$ | $n_i$ | $N_i$ | $f_i$ | $F_i$ | $x_i \cdot n_i$ | $x_i^2 \cdot n_i$ |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| (0, 2] | 1 | 5 | 5 | 0.10 | 0.10 | 5 | 5 |
| (2, 4] | 3 | 23 | 28 | 0.46 | 0.56 | 69 | 207 |
| (4, 6] | 5 | 12 | 40 | 0.24 | 0.80 | 60 | 300 |
| (6, 8] | 7 | 7 | 47 | 0.14 | 0.94 | 49 | 343 |
| (8, 10] | 9 | 3 | 50 | 0.06 | 1.00 | 27 | 243 |
| **Sumas** | | **50** | | **1.00** | | **210** | **1098** |

### 2. Medidas de Posición (Interpolación)
- **$P_{85}$ (Posición 42.5):** Cae en (6, 8].
  $P_{85} = 6 + \frac{42.5 - 40}{7} \cdot 2 = \mathbf{6.71 \text{ h}}$.
- **$C_{0.65}$ (Posición 32.5):** Cae en (4, 6].
  $C_{0.65} = 4 + \frac{32.5 - 28}{12} \cdot 2 = \mathbf{4.75 \text{ h}}$.
- **$IQR$ ($Q_3 - Q_1$):**
  - $Q_1$ (Pos 12.5): En (2, 4] $\rightarrow 2 + \frac{12.5-5}{23} \cdot 2 = 2.65$.
  - $Q_3$ (Pos 37.5): En (4, 6] $\rightarrow 4 + \frac{37.5-28}{12} \cdot 2 = 5.58$.
  - $IQR = 5.58 - 2.65 = \mathbf{2.93 \text{ h}}$.

### 3. Centralización y Dispersión
- **Media ($\bar{x}$):** $210 / 50 = \mathbf{4.2 \text{ h}}$.
- **Moda ($Mo$):** Mayor $n_i$ es 23 en (2, 4]. $d_1 = 18, d_2 = 11$.
  $Mo = 2 + \frac{18}{18+11} \cdot 2 = \mathbf{3.24 \text{ h}}$.
- **Varianza ($S^2$):** $1098/50 - 4.2^2 = 21.96 - 17.64 = \mathbf{4.32 \text{ h}^2}$.
- **Desviación ($S$):** $\sqrt{4.32} = \mathbf{2.08 \text{ h}}$.

---

## Ejercicio 2: Modelado (2.5 puntos)

### 2.1 Alumnos de ADE ($n=45, p=0.08$)
Usamos aproximación de Poisson con $\mu = 45 \cdot 0.08 = 3.6$.
$P(X \geq 2) = 1 - [P(X=0) + P(X=1)]$
$P(X=0) = e^{-3.6} = 0.0273$
$P(X=1) = e^{-3.6} \cdot 3.6 = 0.0983$
**Resultado:** $1 - (0.0273 + 0.0983) = \mathbf{0.8744 \ (87.44\%)}$.

### 2.2 Alumnos de NHD ($n=25, p=0.20$)
Usamos Binomial directa $BIN(25, 0.2)$.
$P(4 \leq Y \leq 6) = P(Y=4) + P(Y=5) + P(Y=6)$
- $P(4) = \binom{25}{4} 0.2^4 0.8^{21} = 0.1876$
- $P(5) = \binom{25}{5} 0.2^5 0.8^{20} = 0.1960$
- $P(6) = \binom{25}{6} 0.2^6 0.8^{19} = 0.1633$
**Resultado:** $0.1876 + 0.1960 + 0.1633 = \mathbf{0.5469 \ (54.69\%)}$.

---

## Ejercicio 3: Inferencia (2.5 puntos)

### 3.A Tamaño Muestral ($n$)
**Objetivo:** ¿A cuánta gente hay que preguntar para cometer un error máximo de 0.05h?

1. **Datos:** 
   - Confianza 95% $\rightarrow Z_{1-\alpha/2} = 1.96$.
   - Precisión deseada (Error $d$): $0.05$.
   - Desviación típica ($S$): $0.8$ (del estudio piloto de n=25).
2. **Fórmula:**
   $$n \geq \left( \frac{Z_{1-\alpha/2} \cdot S}{d} \right) ^2$$
3. **Cálculo:**
   $$n \geq \left( \frac{1.96 \cdot 0.8}{0.05} \right) ^2 = \left( \frac{1.568}{0.05} \right) ^2 = 31.36^2 = 983.45$$

**Resultado:** Se necesitan al menos **984 alumnos** para garantizar esa precisión.

---

### 3.B Intervalo de Confianza para la Media (99%)
**Objetivo:** Estimar entre qué valores está la media real de la población con un 99% de seguridad.

1. **Datos:** 
   - Muestra ($n$): $800$.
   - Media muestral ($\bar{x}$): $3.3$.
   - **Varianza poblacional conocida ($\sigma^2$):** $0.54 \rightarrow \sigma = \sqrt{0.54} = 0.7348$.
   - Confianza 99% $\rightarrow Z_{1-\alpha/2} = 2.575$ (valor de las tablas).
2. **Cálculo del Error (Margen de error):**
   $$E = Z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}} = 2.575 \cdot \frac{0.7348}{\sqrt{800}} = 2.575 \cdot 0.02598 = 0.0669 \approx 0.067$$
3. **Construcción del Intervalo:**
   $$IC = \bar{x} \pm E = 3.3 \pm 0.067$$

**Resultado:** $\mathbf{IC_{99\%} = [3.233, 3.367]}$. Con un 99% de confianza, los alumnos de la UNEAT estudian entre 3.23 y 3.37 horas de media.

---

### 3.C Diferencia de Medias (UNEAT vs UC)
**Objetivo:** ¿Es esa diferencia de 0.8 horas real o es fruto del azar?

1. **Planteamiento:**
   - UNEAT (Muestra 1): $n_1=800, \bar{x}_1=3.3, \sigma_1^2=0.54$.
   - UC (Muestra 2): $n_2=1200, \bar{x}_2=4.1, \sigma_2^2=0.8$.
2. **Error Típico de la Diferencia ($SE_{diff}$):**
   $$SE = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}} = \sqrt{\frac{0.54}{800} + \frac{0.8}{1200}} = \sqrt{0.000675 + 0.000667} = 0.0366$$
3. **Cálculo del IC de la Diferencia (95%):**
   - $Z_{1-\alpha/2} = 1.96$.
   - $Error = 1.96 \cdot 0.0366 = 0.0718$.
   - **Diferencia observada:** $3.3 - 4.1 = -0.8$.
   $$IC = -0.8 \pm 0.0718 = [-0.8718, -0.7282]$$

**Interpretación Final:**
> [!IMPORTANT]
> Como el intervalo **NO contiene al 0** (ambos límites son negativos), podemos afirmar que **existente diferencias significativas** entre ambas universidades. Dado que el intervalo es totalmente negativo, concluimos con un 95% de seguridad que los alumnos de la UC estudian más que los de la UNEAT.

---

## Ejercicio 4: Contraste de Hipótesis (2.5 puntos)

### 4.1 Contraste de Medias (Tiempo de Cuestionario)
**Objetivo:** ¿Es cierto que se tarda 12 min o se tarda **más**?

1. **Definición de Hipótesis (4.A):**
   - $H_0: \mu = 12$
   - $H_1: \mu > 12$ (Contraste unilateral derecho)
2. **Valor Crítico Teórico (4.B):**
   - Usamos **t de Student** (n=25 es pequeña y $\sigma$ desconocida).
   - Grados de libertad: $n-1 = 24$.
   - $\alpha = 0.05$.
   - Mirando la tabla de la t: $t_{24; 0.05} = \mathbf{1.711}$.
3. **Estadístico Experimental (4.C):**
   $$t_{exp} = \frac{\bar{x} - \mu_0}{S / \sqrt{n}} = \frac{13.5 - 12}{2.9 / 5} = \frac{1.5}{0.58} = \mathbf{2.586}$$
4. **Conclusión (4.D):**
   - Como $2.586 > 1.711$, el estadístico cae en la **región crítica**.
   - **Rechazamos $H_0$** y aceptamos $H_1$.
   - **Concluyendo:** Sí, se tarda significativamente más de 12 minutos.

---

### 4.2 Contraste de Proporciones (Nivel Educativo)
**Objetivo:** ¿Influye el nivel educativo en los aciertos?

1. **Definición de Hipótesis (4.E):**
   - $H_0: P_1 = P_2$ (No influye / Proporciones iguales)
   - $H_1: P_1 \neq P_2$ (Sí influye / Proporciones distintas)
2. **Valor Crítico Teórico (4.F):**
   - Nivel de significancia $\alpha = 0.01$.
   - Al ser bidireccional, buscamos $1-\alpha/2 = 0.995$.
   - En la tabla normal: $Z_{0.995} = \mathbf{2.575}$.
3. **Estadístico Experimental (4.G):**
   - $p_1 = 25/40 = 0.625 \rightarrow q_1 = 0.375$.
   - $p_2 = 28/50 = 0.56 \rightarrow q_2 = 0.44$.
   - Usamos la formula del formulario: 
   $$Z_{exp} = \frac{p_1 - p_2}{\sqrt{\frac{p_1q_1}{n_1} + \frac{p_2q_2}{n_2}}} = \frac{0.625 - 0.56}{\sqrt{\frac{0.625 \cdot 0.375}{40} + \frac{0.56 \cdot 0.44}{50}}}$$
   $$Z_{exp} = \frac{0.065}{\sqrt{0.00585 + 0.00493}} = \frac{0.065}{0.1038} = \mathbf{0.626}$$
4. **Conclusión (4.H):**
   - Como $0.626 < 2.575$, el estadístico **no cae** en la región crítica.
   - **No rechazamos $H_0$**.
   - **Concluyendo:** No hay evidencia suficiente para decir que el nivel educativo influya en los aciertos.

---
[Volver al Examen](Simulacro%20de%20Examen%20-%20Modelo%20B.md) | [Inicio](900%20Bin/Estadistica/Index.md)
