# Challenge 6 - Through the Looking-Glass

En este problema se proporciona un código QR que apunta a la página de
Wikipedia de [Piet Mondrian](https://en.wikipedia.org/wiki/Piet_Mondrian).

Si observamos el apartado de [*References in Culture*]
(https://en.wikipedia.org/wiki/Piet_Mondrian#References) vemos una referencia al
lenguaje de programación Piet, en el que los programas se representan mediante
imágenes.

En Piet se utilizan 20 colores: negro, blanco y tres tonalidades de rojo,
amarillo, verde, cian, azul y magenta. *Casualmente* la imagen que contiene el QR
está formada por estos colores, por lo que parece que también es un programa en Piet.

En este caso, probamos el intérprete de Piet [`npiet`](http://www.bertnase.de/npiet/)
con la imagen. Sin éxito. El píxel situado en la esquina superior izquierda
(donde comienza la ejecución) es negro, lo que no tiene sentido ya que las
instrucciones en Piet se codifican utilizando las diferentes tonalidades de rojo,
amarillo, verde, cian, azul y magenta.

Si volvemos al enunciado encontraremos la pista que nos falta para encontrar la
solución. Según el enunciado, Alicia ve la imagen "a través del espejo"...
¡Bingo! Alicia está viendo la imagen *espejada*, por lo que revertiremos la imagen
volteandola horizontalmente. Si volvemos a ejecutar el intérprete con la nueva
imagen vemos como el programa muestra un mensaje por pantalla.
