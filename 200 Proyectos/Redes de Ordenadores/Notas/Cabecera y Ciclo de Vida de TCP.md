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
3. **Cierre**: Se despiden con **FIN**. El estado `TIME_WAIT` es como quedarse un momento en la puerta tras decir adiós "por si se te olvida decir algo último".

---
**Relacionado**: [[Control de Flujo, Errores y Congestión en TCP]]
**Fuente**: [[62_Tema6.pdf]]
