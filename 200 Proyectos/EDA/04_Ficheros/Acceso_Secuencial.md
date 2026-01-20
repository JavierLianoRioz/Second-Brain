---
tags: [eda, files, persistence]
---
# Acceso Secuencial

El **Acceso Secuencial** es el método más simple para gestionar ficheros, donde los datos se leen o escriben en orden, uno tras otro, desde el principio del archivo.

## Complejidad Big O

| Operación | Complejidad | Notas |
| :--- | :--- | :--- |
| **Inserción** | $O(n)$ | Normalmente requiere reescribir el fichero o buscar el final ($O(1)$ si es append). |
| **Edición** | $O(n)$ | Debe recorrer el fichero hasta encontrar el registro a modificar. |
| **Eliminación** | $O(n)$ | Requiere marcar como borrado o reescribir el resto del fichero. |
| **Peek (Índice)** | $O(n)$ | Debe leer todos los registros anteriores para llegar a la posición $n$. |

## Características
- Los registros se procesan en el mismo orden en que fueron almacenados.
- Ideal para procesamientos masivos (ej. nóminas, backups).
- Ejemplo físico: Cinta de video o cassette.

---
[Regresar al MOC](00_MOC_Ficheros.md)
