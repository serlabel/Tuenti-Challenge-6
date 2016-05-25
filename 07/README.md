# Challenge 7 - Tiles

Este problema es un caso típico de programación dinámica. El objetivo es
determinar la suma máxima de cualquier submatriz. En este caso, como la matriz
se repite en ambas dimensiones, debemos también tener en cuenta que es posible
que la suma máxima sea infinito, o que la submatriz de suma máxima ocupe más de
un azulejo.

Para el primer caso, lo único que debemos hacer es obtener la suma de todas las
columnas y filas de la matriz. Si encontramos una fila o columna cuya suma sea
mayor que cero, existe una submatriz cuya suma es infinito.

En el segundo caso, vamos a aplicar la solución de programación dinámica a la
matriz duplicada en ambas dimensiones (si teníamos una matriz de **N** x **M**, 
ahora tendremos una matriz de **2N** x **2M**).

**¡Cuidado!** Si solo aplicamos [imagen integral]
(https://en.wikipedia.org/wiki/Summed_area_table) el coste es **O(2N² x 2M²)**,
inasumible en el peor de los casos (**N = M = 1000**).

Para reducir el coste computacional podemos aplicar el [algoritmo de Kadane]
(https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane.27s_algorithm).
Con este método podemos calcular la máxima suma de cualquier submatriz entre
dos filas en tiempo lineal, de forma que el coste se reduce a **O(2N² x 2M)**.
