# Challenge 8 - Labyrinth

En este problema tenemos un laberinto que *resolver* para obtener un token.

Para resolverlo, se sigue la [técnica de la mano derecha]
(https://en.wikipedia.org/wiki/Maze_solving_algorithm#Wall_follower), por la que
los movimientos dentro del laberinto se realizan siguiendo a la pared. De esta forma,
los movimientos deben realizarse como si pusieramos la mano derecha en la pared
y avanzando sin que la mano se despegue de esta.

Al final, el token está alrededor del laberinto y este no tiene salida, pero con
la técnica anterior se recorre todo el laberinto, de forma que podemos obtener el
token.
