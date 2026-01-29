# Ejercicio: Exceso de Riesgo Atribuible (Tabaco)

Este ejercicio muestra cómo calcular el impacto de un factor de riesgo (fumar) en la salud de una población.

## Enunciado
Calculemos el exceso de enfermos debido al tabaco en una población con los siguientes datos:
- **Población total**: 1.000.000 habitantes.
- **Prevalencia de fumadores**: 10% (100.000 personas).
- **Riesgo en No-fumadores**: 1% enferman.
- **Riesgo Relativo (RR)**: Fumar multiplica por 4 el riesgo de contraer la enfermedad.

## Resolución Paso a Paso

### 1. Situación Hipotética (Si nadie fumara)
Si el riesgo fuera del 1% para todos (como si fueran no-fumadores):
$$Enfermos_{hip} = 1.000.000 \times 0,01 = 10.000 \text{ personas}$$

### 2. Situación Real (Con fumadores)
- **Fumadores (10%)**: 100.000 personas.
    - Riesgo: $1\% \times 4 = 4\%$.
    - Enfermos: $100.000 \times 0,04 = 4.000 \text{ personas}$.
- **No-Fumadores (90%)**: 900.000 personas.
    - Riesgo: $1\%$.
    - Enfermos: $900.000 \times 0,01 = 9.000 \text{ personas}$.
- **Total de enfermos reales**: $4.000 + 9.000 = 13.000 \text{ personas}$.

### 3. Cálculo del Exceso de Riesgo
La diferencia entre la realidad y el escenario ideal sin tabaco:
$$Exceso = 13.000 - 10.000 = 3.000 \text{ enfermos}$$

### 4. Porcentaje Atribuible
¿Qué porcentaje de todos los enfermos lo son debido al tabaco?
$$\% = \frac{3.000}{13.000} \times 100 \approx 23\%$$

---
**Base Teórica**: [[01_Tema1_Descriptiva/Medidas de Posición (Cuantiles)|Percentiles y Proporciones]]
Tags: #estadistica #ejercicio #proporciones #riesgo
