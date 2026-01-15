# SQL JOIN

Vincula datos de múltiples tablas.

## Tipos
*   **INNER JOIN**: Solo filas que coinciden en ambas.
*   **LEFT JOIN**: Todas las de la izquierda + coincidentes derecha.
*   **RIGHT JOIN**: Todas las de la derecha.

```mermaid
graph LR
    subgraph INNER_JOIN
    A1((A)) --- B1((B))
    A1 --- C1{ } --- B1
    style C1 fill:#f9f,stroke:#333
    end

    subgraph LEFT_JOIN
    A2((A)) --- B2((B))
    style A2 fill:#f9f,stroke:#333
    style B2 fill:#fff,stroke:#333
    end

    subgraph RIGHT_JOIN
    A3((A)) --- B3((B))
    style A3 fill:#fff,stroke:#333
    style B3 fill:#f9f,stroke:#333
    end
```


## Ejemplo
```sql
SELECT c.nombre, p.total
FROM cliente c
INNER JOIN pedido p ON c.id = p.id_cliente;
```

---
[SELECT Basico](SELECT_Basico.md)
