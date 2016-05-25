# Challenge 12 - Pika Virus

En este problema debemos determinar si dos virus se propagan de forma similar.
Según el propio enunciado, las condiciones que deben cumplir ambos virus son:
- Ambos virus infectan al mismo número de ciudades.
- Cada ciudad infectada por el virus A tiene una ciudad equivalente infectada por
  el virus B.

Dos ciudades son equivalentes si:
- Ambas ciudades infectan al mismo número de ciudades.
- Ambas ciudades tienen el mismo número de saltos desde la ciudad desde la que comienza
  a propagarse el virus.
- Ambas ciudades tienen el mismo árbol de propagación.

Además, no es necesario que los ancestros de las dos ciudades sean también equivalentes.

Dado que el resultado debe seguir el orden lexicográfico, recorremos las ciudades
del virus original por orden alfabético.
Para cada ciudad seguimos el siguiente algoritmo:
- Obtenemos las ciudades del virus a comprobar que están en el mismo nivel (condición 2)
  y que no han sido asignadas a otra ciudad.
- Recorremos las ciudades por orden alfabético hasta que la ciudad del virus
  original y una ciudad del otro virus cumplan las condiciones 1 y 3.
- Si para alguna ciudad no podemos encontrar ninguna equivalente, no se cumple la
  condición necesaria y se concluye que ambos virus **NO** se propagan de forma similar.
