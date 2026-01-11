# Protocolo TCP - Servicio y Multiplexación

TCP (**Transmission Control Protocol**) es un protocolo fiable y orientado a conexión.

## Características del Servicio
- **Fiable**: Si algo falla, se retransmite. Es como un envío certificado.
- **Orientado a Conexión**: No envía nada sin antes asegurarse de que el otro está "al teléfono".
- **Basado en Flujos (Streams)**:
  - *Analogía*: Como un grifo de agua. Los datos salen uno tras otro sin marca de dónde termina un vaso y empieza el siguiente. La aplicación debe saber cuándo parar de leer.

## Multiplexación y Sockets
La multiplexación es lo que permite que una sola conexión física (tu cable de red o WiFi) transporte datos de 50 aplicaciones distintas a la vez sin que se mezclen.

### 1. Multiplexación (Lado Emisor)
El nivel de transporte recoge los datos de distintos **Sockets** (puertos), les pone una "etiqueta" (el número de puerto origen) y los suelta todos por el mismo tubo hacia el nivel de Red (IP).
- *Analogía*: Varios vecinos de un edificio bajando a la vez para dejar sus cartas en el único buzón de correos de la esquina.

### 2. Demultiplexación (Lado Receptor)
Cuando los paquetes llegan al destino, el nivel de transporte mira el **Puerto Destino** y entrega cada trozo de datos a la aplicación que le toca.
- *Analogía*: El cartero llega al edificio (IP) y usa los **timbres/interfono** (Puertos) para saber en qué buzón dejar cada carta. Sin el interfono, sabría a qué edificio ir, pero no a quién entregarle la carta.

## Identificación Única (La 5-tupla)
Para que el receptor no se confunda, una conexión se identifica por 5 datos clave:
1. IP Origen
2. Puerto Origen
3. IP Destino
4. Puerto Destino
5. Protocolo (TCP o UDP)

## Tamaño Máximo Teórico (MSS)
En los problemas de examen suele preguntarse por la "Carga útil máxima de TCP":
- **Límite IP (IPv4)**: 65.535 bytes (16 bits de longitud).
- **Cabecera IP**: - 20 bytes.
- **Cabecera TCP**: - 20 bytes.
- **Carga Útil Máxima**: **65.495 bytes**.

## ¿Puerto Origen o Puerto Destino?
Cuando te conectas a un servidor de Minecraft, se usan **dos** puertos distintos:

1. **Puerto Destino (25565)**: Es el puerto del **Servidor**. Es fijo y conocido por todos para que sepan dónde "tocar a la puerta".
2. **Puerto Origen (Ej. 58234)**: Es un puerto aleatorio que abre **tu PC (el Cliente)**. 
   - *¿Para qué sirve?*: Para que cuando el servidor te mande los datos del juego de vuelta, tu Windows sepa que ese paquete es para el proceso `minecraft.exe` y no para el navegador.

**Regla de oro**:
- El **Servidor** escucha en un puerto fijo (Destino).
- El **Cliente** abre un puerto aleatorio (Origen) para cada conexión que inicia.

## ¿Se pueden agotar los puertos?
Sí, pero es difícil. Los puertos son un número de 16 bits, por lo que el máximo teórico es **65.535**.
- **Puertos Libres**: Tu sistema suele tener unos 16.000 puertos "dinámicos" listos para ser usados por tus aplicaciones (YouTube, Discord, etc.).
- **Reutilización**: En cuanto cierras una pestaña o terminas la descarga, el puerto no se pierde para siempre. Tras unos segundos de seguridad (`TIME_WAIT`), el sistema lo marca como libre y lo vuelve a asignar a otra cosa.

> [!NOTE]
> Para que un usuario normal "llene" los puertos, tendría que abrir miles de conexiones simultáneas. Solo es un problema real en servidores masivos (como los de Google) o balanceadores de carga.

---
**Relacionado**: [[Cabecera y Ciclo de Vida de TCP]]
**Fuente**: [[62_Tema6.pdf]]
