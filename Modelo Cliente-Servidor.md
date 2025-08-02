### 🧠 ¿Qué es el Modelo Cliente-Servidor?

Es un **modelo de comunicación** en redes donde **dos roles principales** se comunican entre sí:

* **Cliente**: pide cosas. Es el que hace las solicitudes (por ejemplo: "¡dame esta página web!").
* **Servidor**: responde cosas. Es el que recibe las solicitudes y envía respuestas (por ejemplo: "Aquí tienes la página web que pediste").

> Piensa en el cliente como alguien en una cafetería que pide un café, y el servidor como el barista que prepara y entrega ese café.

---

### 🔄 ¿Cómo funciona?

1. El **cliente inicia la conexión**.
2. Envía una **petición** al servidor.
3. El **servidor escucha** esas peticiones (está siempre en modo "estoy aquí, ¿quién quiere algo?").
4. Procesa la petición y devuelve una **respuesta**.
5. El cliente recibe la respuesta y, si quiere, hace otra petición.

---

### 📶 ¿Dónde se aplica?

* Cuando abres una página web → tu navegador es el cliente, y el servidor web (como Apache o Nginx) te manda la web.
* Cuando revisas tus correos → el cliente de correo (Outlook, Thunderbird…) se conecta al servidor de correo (Gmail, Outlook.com…).
* Cuando juegas en línea → tu juego (cliente) se conecta a un servidor central para coordinar la partida.

---

### 🧱 Características Clave

| Cliente                     | Servidor                                    |
| --------------------------- | ------------------------------------------- |
| Inicia la conexión          | Espera conexiones                           |
| Solicita recursos           | Proporciona recursos                        |
| Generalmente no persistente | Normalmente siempre activo                  |
| Muchos clientes posibles    | Un servidor puede atender a muchos clientes |

---

### 💬 Ejemplo real: HTTP (el de las webs)

* Cliente: navegador web.
* Servidor: servidor HTTP.
* El cliente hace una petición GET a `https://midaspower.com/perfil` y el servidor devuelve una página HTML.

---

### 🕹️ Ventajas del modelo

* Organización clara de roles.
* Escalable: se puede atender a muchos clientes.
* Separación de responsabilidades (el servidor puede estar optimizado para eficiencia, el cliente para interfaz).

---

### ⚠️ Desventajas

* Si el **servidor cae**, nadie puede usar el servicio.
* Mayor carga en el servidor (tiene que estar siempre disponible).
* Puede haber problemas de latencia/red si el servidor está lejos.

---

### 🤖 ¿Y en programación?

En código, por ejemplo en **sockets**, tú puedes escribir un servidor que escuche en un puerto y un cliente que se conecte a él. Básico para entender redes, protocolos y sistemas distribuidos.