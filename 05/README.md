# Challenge 5 - Hangman

En este problema tenemos un servicio web con el que podemos jugar al 'Ahorcado'.
El objetivo es ganar varias partidas de forma consecutiva. Y no es tan fácil.

La primera partida consiste en una palabra de 4 letras. ¿Podemos garantizar que
ganaremos todas las partidas? NO. ¿Por qué?

Vamos a suponer que estamos en mitad de una partida donde la palabra es `LA_E`
y que no hemos fallado ninguna letra. Las palabras del diccionario que cumplen
este patrón son **ocho** (LACE, LADE, LAKE, LAME, LANE, LASE, LATE, LAZE).  
**Ocho** posibles letras y solo **siete** intentos.

Como hemos visto no podemos garantizar ganar todas las partidas, pero si podemos
utilizar toda la información que tengamos para ganar el mayor número de partidas
posible.

Cuando comienza la partida tenemos 26 letras posibles.  
En este punto, la única información que tenemos es la longitud de la palabra.
Con ello y el diccionario proporcionado, podemos reducir la lista de posibles
palabras.

A partir de aquí, en cada turno vamos a dar la letra más frecuente entre las
palabras que cumplan el patrón. De esta forma:
- Si no está la letra, podemos descartar todas aquellas que la contengan.
- Si está, podemos eliminar las palabras que no la contengan, pero **también**
  aquellas que no cumplen el patrón (p.e. ADAM no coincide con `A___`).
