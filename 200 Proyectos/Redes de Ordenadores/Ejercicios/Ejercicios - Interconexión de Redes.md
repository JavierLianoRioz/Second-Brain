# Ejercicios - Interconexión de Redes

Problemas resueltos del Tema 5 sobre fragmentación, NAT y direccionamiento IP.

## Ejercicio 1: Fragmentación IP
**Enunciado**: Un datagrama de 4500 octetos (incluida cabecera) atraviesa una red Ethernet (MTU = 1500). Muestra los fragmentos resultantes.

**Solución**:
- Datos totales: $4500 - 20 = 4480$ octetos.
- Payload máximo Ethernet: $1500 - 20 = 1480$ octetos.
- Fragmentos necesarios: $\lceil 4480 / 1480 \rceil = 4$.
1. **Fr. 1**: Longitud 1500, Offset 0, More Flag 1 ($1480$ bytes datos).
2. **Fr. 2**: Longitud 1500, Offset $1480/8 = 185$, More Flag 1 ($1480$ bytes datos).
3. **Fr. 3**: Longitud 1500, Offset $2960/8 = 370$, More Flag 1 ($1480$ bytes datos).
4. **Fr. 4**: Longitud $40 + 20 = 60$, Offset $4440/8 = 555$, More Flag 0 ($40$ bytes datos).

## Ejercicio 2: Tabla de Traducción NAT
**Enunciado**: Tres equipos internos (192.168.1.1, .2, .3) abren dos conexiones cada uno al host 128.119.40.86 puerto 80. Muestra la tabla PAT del router (IP pública 24.34.112.235).

**Solución**:
- El router usará su IP pública y puertos diferentes para cada flujo interno.
- **Entrada 1**: 192.168.1.1:1000 $\to$ 24.34.112.235:5000
- **Entrada 2**: 192.168.1.1:1001 $\to$ 24.34.112.235:5001
- **Entrada 3**: 192.168.1.2:1000 $\to$ 24.34.112.235:5002 ... y así sucesivamente.

## Ejercicio 3: Cálculo de Subredes (Subnetting)
**Enunciado**: Dividir `192.168.1.0/24` para: Operaciones (50 IPs), SCADA Sensores (40 IPs), SCADA Actuadores (32 IPs), Oficinas (25 IPs).

**Solución**:
1. **Operaciones**: Necesita 50 (+2 gateway/net). Máscara /26 (64 IPs). $\to$ `192.168.1.0/26`.
2. **Sensores**: Necesita 40. Máscara /26. $\to$ `192.168.1.64/26`.
3. **Actuadores**: Necesita 32. Máscara /26. $\to$ `192.168.1.128/26`.
4. **Oficinas**: Necesita 25. Máscara /27 (32 IPs). $\to$ `192.168.1.192/27`.

## Guía Rápida: Cómo Subnetear
Para dividir una red (ej. `/24`) en subredes:
1. **Cuántos bits robar ($n$)?**: $2^n \geq \text{Nº de subredes}$.
2. **Nueva máscara**: Sumas esos $n$ bits al prefijo original ($24 + n$).
3. **Salto de red**: $256 - \text{Valor del último octeto de la máscara}$.
   - *Ejemplo*: Si la máscara es `255.255.255.192` ($/26$), el salto es $256-192 = 64$.
   - Redes: `.0`, `.64`, `.128`, `.192`.

---
**Relacionado**: [[Direccionamiento IP y Subredes]], [[Fragmentación y NAT]]
**Fuente**: [[54_ProblemasTema5.pdf]]
