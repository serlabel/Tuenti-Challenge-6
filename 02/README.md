# Challenge 2 - The Voynich Manuscript

El objetivo de este problema es encontrar las tres palabras más frecuentes en
un fragmento de texto.

Para ello, primero obtendremos un diccionario de frecuencias, donde la clave
es la palabra y el valor, el número de veces que aparece en el fragmento.

```python
frequencies = {}
for i in range(start-1, end):
    if words[i] not in frequencies:
        frequencies[words[i]] = 1
    else:
        frequencies[words[i]] += 1
```

Para obtener las palabras más frecuentes, generamos una lista de tuplas
`(frecuencia, palabra)`.  
Al ordenar esta lista (en orden descendente), las tres primeras tuplas
hacen referencia a las tres palabras más frecuentes.

```python
f = [(frequencies[word], word) for word in frequencies]
f.sort(reverse=True)
```
