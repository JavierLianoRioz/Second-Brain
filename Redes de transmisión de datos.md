## 🕸️ ¿Qué son las Redes de Transmisión de Datos?

Son **infraestructuras físicas y lógicas** que permiten **enviar y recibir datos entre dispositivos** (ordenadores, móviles, routers, tostadoras inteligentes...).

### En resumen:

> Son las **autopistas de la información**. Los datos (como mensajes, vídeos, archivos, comandos) viajan por ellas de un lugar a otro, como coches por carreteras.

---

## 📦 ¿Qué tipo de datos se transmiten?

Todo lo que ves en internet o en una red local:

* Archivos
* Streaming de vídeo o audio
* Correos electrónicos
* Juegos en línea
* Señales de sensores o cámaras
* Paquetes TCP/IP (los verdaderos MVPs)

---

## 🧱 Componentes básicos

1. **Dispositivos emisores y receptores**
   Ejemplo: un ordenador y un servidor.

2. **Medios de transmisión**

   * 🧵 *Alámbricos*: cobre (Ethernet), fibra óptica.
   * 📡 *Inalámbricos*: Wi-Fi, 4G/5G, satélite, Bluetooth.

3. **Protocolos de comunicación**
   Como las reglas del tráfico. Ejemplo: TCP/IP, HTTP, FTP, etc.

4. **Equipos intermedios**

   * Routers
   * Switches
   * Hubs (en paz descansen)
   * Repetidores

---

## ⚙️ ¿Cómo funciona la transmisión?

Imagina que quieres mandar un archivo:

1. Lo divides en **paquetes** de datos.
2. Cada paquete tiene **información de control** (origen, destino, número de orden).
3. Los paquetes viajan por la red (por rutas que pueden cambiar dinámicamente).
4. El receptor los **reensambla** y verifica que todo ha llegado.
5. Si algo falla, se reenvían los paquetes perdidos.

¡Voilà! Acabas de usar una red de transmisión.

---

## 📡 Tipos de transmisión

### Según dirección de datos:

| Tipo        | Descripción                           | Ejemplo                       |
| ----------- | ------------------------------------- | ----------------------------- |
| Simplex     | Solo en un sentido                    | Televisión                    |
| Half-Duplex | En ambos sentidos, pero no simultáneo | Walkie-talkie                 |
| Full-Duplex | En ambos sentidos simultáneamente     | Videollamadas, navegación web |

---

## 🌐 Clasificación por cobertura

| Tipo                          | Cobertura                                  | Ejemplo                     |
| ----------------------------- | ------------------------------------------ | --------------------------- |
| PAN                           | Personal (metros)                          | Bluetooth, USB-C, NFC       |
| LAN                           | Local (edificio)                           | Red doméstica o de oficina  |
| MAN                           | Metropolitana                              | Red de campus universitario |
| [[Redes de área amplia\|WAN]] | [[Redes de área amplia\|Amplia (mundial)]] | Internet                    |

---

## 🚦 Protocolos importantes

* **TCP/IP**: núcleo de Internet, asegura que todo llega bien.
* **UDP**: más rápido, pero menos fiable (ideal para streaming/juegos).
* **Ethernet**: estándar de redes LAN.
* **Wi-Fi (802.11x)**: redes inalámbricas.
* **HTTP/HTTPS, FTP, SMTP, DNS…**: protocolos de aplicación.

---

## ⚡ Factores que afectan la transmisión

* Ancho de banda (capacidad máxima)
* Latencia (tiempo que tarda en llegar)
* Pérdida de paquetes
* Interferencias (en redes inalámbricas)
* Congestión de red

---

## 📌 Ejemplo visual:

```txt
[ PC de Midas ] ─────┬────── [Router WiFi] ───╮
                     │                        │
               [Impresora WiFi]         [Servidor Google]
```

Cuando imprimes algo, los datos van desde tu PC al router, y de ahí a la impresora.
Cuando buscas algo en Google, los datos viajan miles de km por cables submarinos y routers internacionales hasta llegar a ti en milisegundos. 😮
