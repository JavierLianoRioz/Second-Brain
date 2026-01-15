# Cabecera y Ciclo de Vida de TCP

Estructura del segmento TCP y estados de la conexión.

## Cabecera TCP (Mínimo 20 bytes)
- **Sequence Number**: Número del primer byte de datos del segmento.
- **Acknowledgement Number**: Siguiente byte esperado (confirmación acumulativa).
- **Flags**:
  - **SYN**: Sincronización (inicio de conexión).
  - **ACK**: Confirmación válida.
  - **FIN**: Finalización de datos.
  - **RST**: Reinicio abortivo.
  - **PSH**: Solicita entrega inmediata a la aplicación.
- **Window**: Tamaño de la ventana de recepción del emisor del segmento.
- **Checksum**: Detecta errores en cabecera y datos (incluye pseudo-cabecera IP).

## Ciclo de Vida (El saludo y la despedida)
1. **Establecimiento (3-way handshake)**:
   - Cliente: "Hola, ¿podemos hablar? Mis números empiezan en X" (**SYN**).
   - Servidor: "Hola, sí. Yo empiezo en Y. He recibido tu X" (**SYN-ACK**).
   - Cliente: "Perfecto, he recibido tu Y. ¡Empezamos!" (**ACK**).
2. **Mantenimiento**: Intercambio de datos.
3. **Cierre (Despedida)**: 
   - **Modelo de 4 pasos (Estándar)**:
     1. A envía **FIN**.
     2. B envía **ACK** (A deja de enviar, pero B aún podría mandar restos).
     3. B envía **FIN**.
     4. A envía **ACK**.
   - **Modelo de 3 pasos (Optimizado)**: El paso 2 y 3 se juntan en un solo segmento (**FIN+ACK**). Es lo que suelen mostrar las diapositivas simplificadas.
   
> [!NOTE]
> El estado **TIME_WAIT** ocurre al final del cierre activo para asegurar que el último ACK llegó y que no hay paquetes viejos "perdidos" que puedan interferir con una nueva conexión.

---
**Relacionado**: [Control de Flujo, Errores y Congestión en TCP](Control%20de%20Flujo%2C%20Errores%20y%20Congesti%C3%B3n%20en%20TCP.md)
**Fuente**: [[62_Tema6.pdf]]
