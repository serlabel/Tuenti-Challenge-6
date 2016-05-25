# Challenge 1 - Team Lunch

Este problema es fácil de resolver. El objetivo es calcular cuantas mesas
son necesarias para que se sienten `n` comensales.

La implementación ha sido la siguiente:

```python
if n == 0:
    return 0
if n <= 4:
    return 1
else:
    return 1 + (n - 3)//2
```

La explicación es:
- Si no hay comensales (`n = 0`), no es necesaria ninguna mesa.
- Si el número de comensales es cuatro o menos, caben en una mesa.
- Con cinco o más comensales, son necesarias una mesa para los tres primeros
  comensales más una mesa por cada dos comensales extra.  
  Si el número de comensales extra es impar, el último comensal se sentará en
  el lado no ocupado de la última mesa (por este motivo la división es entera).