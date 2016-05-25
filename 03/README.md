# Challenge 3 - YATM Microservice

Quizás lo más difícil de este problema es parsear la entrada.  
Bueno, lo es si no conoces el formato [YAML](https://es.wikipedia.org/wiki/YAML). 
Utilizando [PyYAML](http://pyyaml.org/) es así de fácil:

```python
import yaml as pyml

with sys.stdin as input:
    data = pyml.load(input)
return data['code'], data['tapes']
```

Una vez hecho esto solo queda procesar cada una de las cintas, empezando en el
estado `start` y hasta llegar al estado `end`.  
En cada iteración seguimos las indicaciones en el siguiente orden:
1. Escribimos en la posición actual
2. Nos movemos a izquierda o a derecha
3. Cambiamos de estado

Debemos tener en cuenta que los pasos a seguir pueden ser diferentes según el
símbolo de la posición actual.