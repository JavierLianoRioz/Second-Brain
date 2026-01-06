# Ejercicios - Interconexión de Redes

Problemas resueltos del Tema 5 sobre fragmentación, NAT y direccionamiento IP.

## Ejercicio 1: Fragmentación IP
**Enunciado**: Un datagrama de 4500 octetos (incluida cabecera) atraviesa una red Ethernet (MTU = 1500). Muestra los fragmentos resultantes.

**Solución paso a paso**:

1. **Calcular Datos (Octetos de datos)**:
   - Todo datagrama tiene una cabecera (normalmente 20 bytes).
   - $4500 \text{ (Total)} - 20 \text{ (Cabecera)} = 4480 \text{ octetos de datos}$.

2. **Calcular Capacidad de cada Fragmento**:
   - MTU de Ethernet = 1500 bytes.
   - Restamos cabecera: $1500 - 20 = 1480$ bytes de datos caben en cada fragmento.
   - *Nota*: El tamaño de datos de los fragmentos intermedios **debe ser múltiplo de 8** (para que el *Offset* sea un número entero). $1480 / 8 = 185$ (¡Perfecto!).

3. **Repartir los datos**:
   - $\lceil 4480 / 1480 \rceil = 3.02 \to 4 \text{ Fragmentos}$.
   - **Fr. 1**: 1480 datos. Offset = 0. $MF = 1$ (siguen más).
   - **Fr. 2**: 1480 datos. Offset = $1480 / 8 = 185$. $MF = 1$.
   - **Fr. 3**: 1480 datos. Offset = $(1480+1480) / 8 = 370$. $MF = 1$.
   - **Fr. 4**: Los datos que sobran ($4480 - (1480 \times 3) = 40$ datos). Offset = $4440 / 8 = 555$. $MF = 0$ (es el último).

| Fragmento | Datos (bytes) | Cabecera | Longitud Total | Offset (8 bytes) | MF |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 1480 | 20 | 1500 | 0 | 1 |
| 2 | 1480 | 20 | 1500 | 185 | 1 |
| 3 | 1480 | 20 | 1500 | 370 | 1 |
| 4 | 40 | 20 | 60 | 555 | 0 |

## Ejercicio 2: Tabla de Traducción NAT
**Enunciado**: Tres equipos internos (192.168.1.1, .2, .3) abren dos conexiones cada uno al host 128.119.40.86 puerto 80. Muestra la tabla PAT del router (IP pública 24.34.112.235).

**Solución detallada**:

En **PAT (Port Address Translation)**, el router usa una única IP pública pero asigna un **puerto de salida único** a cada flujo para poder distinguir las respuestas que vuelven.

| IP Origen (Privada) | Puerto Origen | IP Destino (Pública) | Puerto Destino | -> | IP Pública Router | Puerto Público |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 192.168.1.1 | 1000 | 128.119.40.86 | 80 | | 24.34.112.235 | **5000** |
| 192.168.1.1 | 1001 | 128.119.40.86 | 80 | | 24.34.112.235 | **5001** |
| 192.168.1.2 | 1000 | 128.119.40.86 | 80 | | 24.34.112.235 | **5002** |
| 192.168.1.2 | 1024 | 128.119.40.86 | 80 | | 24.34.112.235 | **5003** |
| 192.168.1.3 | 4321 | 128.119.40.86 | 80 | | 24.34.112.235 | **5004** |
| 192.168.1.3 | 5678 | 128.119.40.86 | 80 | | 24.34.112.235 | **5005** |

**Por qué es importante**: Sin el "Puerto Público", cuando el servidor de Google responda, el router no sabría si la web es para el equipo .1, .2 o .3.

## Ejercicio 3: Cálculo de Subredes (Subnetting)
**Enunciado**: Dividir `192.168.1.0/24` para: Operaciones (50 IPs), SCADA Sensores (40 IPs), SCADA Actuadores (32 IPs), Oficinas (25 IPs).

**Solución mediante VLSM**:

Dividimos la red `192.168.1.0/24` de mayor a menor necesidad:

1. **Operaciones (50+2 IPs)**:
   - Buscamos $2^h \geq 52 \to h=6$ bits para hosts.
   - Máscara: $32 - 6 = /26$ (64 direcciones).
   - **Rango**: `192.168.1.0/26` (Red: .0, Broadcast: .63).

2. **Sensores (40+2 IPs)**:
   - Buscamos $2^h \geq 42 \to h=6$ bits para hosts.
   - Máscara: $/26$ (64 direcciones).
   - **Rango**: `192.168.1.64/26` (Red: .64, Broadcast: .127).

3. **Actuadores (32+2 IPs)**:
   - Buscamos $2^h \geq 34 \to h=6$ bits para hosts.
   - Máscara: $/26$ (64 direcciones).
   - **Rango**: `192.168.1.128/26` (Red: .128, Broadcast: .191).

4. **Oficinas (25+2 IPs)**:
   - Buscamos $2^h \geq 27 \to h=5$ bits para hosts.
   - Máscara: $32 - 5 = /27$ (32 direcciones).
   - **Rango**: `192.168.1.192/27` (Red: .192, Broadcast: .223).

## La Receta Infalible para Subnetear (VLSM)
Si el ejercicio te pide diferentes tamaños de red (ej. una de 50, otra de 20...), usa esta lógica de "Corte de Tarta":

### 1. Ordena de Mayor a Menor
**Siempre** empieza por la red que necesita más IPs. Si empiezas por las pequeñas, fragmentarás el espacio y luego no te cabrán las grandes.

### 2. La Regla de los Bits ($2^h \geq N+2$)
Para cada red, busca cuántos bits ($h$) necesitas para los hosts:
- Si necesitas 50 IPs $\to 50+2=52 \to$ Necesitas **6 bits** ($2^6 = 64$).
- Si necesitas 10 IPs $\to 10+2=12 \to$ Necesitas **4 bits** ($2^4 = 16$).

### 3. Calcula la Máscara y el Salto
- **Máscara**: $32 - \text{bits de host}$. (Ej: $32 - 6 = /26$).
- **Tamaño del trozo (Salto)**: Es el resultado de $2^h$. (Ej: 64).

### Ejemplo Visual:
Imagina que tienes una tarta de 256 porciones (`.0` a `.255`):
1. **Red A (50 IPs)**: Necesitas un trozo de **64**. 
   - Va de la `.0` a la `.63`. 
   - *Siguiente red empieza en `.64`*.
2. **Red B (20 IPs)**: $20+2=22 \to$ Necesitas trozo de **32** ($h=5$).
   - Va de la `.64` a la `.95` ($64+32-1=95$).
   - *Siguiente red empieza en `.96`*.

| Red | Necesita | Trozo ($2^h$) | Máscara | Rango |
| :--- | :--- | :--- | :--- | :--- |
| Mayor | 50 | 64 | /26 | .0 - .63 |
| Mediana| 25 | 32 | /27 | .64 - .95 |
| Pequeña| 10 | 16 | /28 | .96 - .111 |

---
**Relacionado**: [[Direccionamiento IP y Subredes]], [[Fragmentación y NAT]]
**Fuente**: [[54_ProblemasTema5.pdf]]
