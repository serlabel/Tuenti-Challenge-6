# Challenge 11 - Toast

El objetivo de este problema es determinar si es posible obtener **k** tostadas
a partir de **n** pilas de **m** tostadas.

Podemos obtener más tostadas cortando una pila de tostadas. Tras el corte, podemos
apilar las tostadas obteniendo una pila con el doble de tostadas o podemos separar
las tostadas obteniendo una nueva pila.

Para empezar, no existe solución si el número de tostadas iniciales es superior
a **k**. En caso contrario, solo podemos asegurar que existirá una solución si **k**
es múltiplo de **m**, ya que una posible solución sería tener **k/m** pilas de **m**
tostadas.

Si el caso tiene solución, a continuación calculamos la solución con menor número
de cortes. Para ello, vamos duplicando una de las pilas hasta tener el máximo número
de tostadas menor o igual a **k**.

En el caso que no se alcance **k**, vamos a recorrer en orden decreciente el tamaño
previo de la pila, de forma que vamos cubriendo las tostadas restantes. Por ejemplo,
si faltan 16 tostadas y anteriormente hemos duplicado varias veces una pila de 8 tostadas
hasta llegar a 64, solo necesitamos un corte más para obtener las tostadas restantes:
un corte intermedio cuando la pila tiene 16 tostadas para obtener dos pilas de 16.
