# Challenge 15 - Seat change!

El objetivo del problema es determinar el asiento más probable después de un
determinado número de cambios (**n**) a partir de una serie de transiciones
con probabilidades.

Si generamos la matriz de transiciones del grafo asignando al elemento *(i,j)* la
probabilidad de ir del asiento *i* al asiento *j*, podemos obtener el resultado
elevando la matriz a la **n**-ésima potencia. De esta forma, solo tenemos que
recorrer la fila correspondiente al asiento inicial.

Para *intentar* reducir el coste computacional, podemos eliminar aquellos asientos
a los que no se puede llegar desde el asiento inicial. En los casos de prueba,
los grafos distan mucho de ser completos, por lo que se puede reducir considerablemente
el tamaño de la matriz.

Además, para el cálculo de la potencia se utiliza [`numpy`]
(http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.linalg.matrix_power.html#numpy.linalg.matrix_power),
que implementa un método de potencias de matrices que utiliza descomposición binaria.

**Nota**: la solución planteada es mejorable, ya que en determinados casos de prueba
el tiempo de ejecución es excesivamente alto.
