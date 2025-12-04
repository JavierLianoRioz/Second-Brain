# SQL GROUP BY

Agrupa filas con valores idénticos para realizar cálculos (COUNT, SUM, AVG).

## Ejemplo
```sql
SELECT categoria, COUNT(*) FROM producto GROUP BY categoria;
```

## HAVING
Filtra **grupos** después de agrupar.

```sql
SELECT categoria, COUNT(*) FROM producto 
GROUP BY categoria 
HAVING COUNT(*) > 5;
```

---
[[SELECT_Basico]]
