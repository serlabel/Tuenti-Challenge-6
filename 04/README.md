# Challenge 4 - Hadouken!

En este problema, el objetivo es detectar el número de veces que aparece en
una cadena un conjunto de patrones. En concreto, debemos determinar cuantas
veces encontramos en una cadena las siguientes subcadenas:
- `L-LD-D-RD-R-x`
- `     D-RD-R-x`
- `     R-D-RD-x`
- `     D-LD-L-y`
- `R-RD-D-LD-L-y`

donde `x` es cualquier símbolo excepto `P` e `y` es cualquier símbolo excepto `K`.

Si nos fijamos, la segunda y cuarta subcadenas son sufijos de la primera y quinta,
respectivamente. En estos casos, siguiendo el enunciado, solo se debe tener en
cuenta uno.

Con esta restricción el problema se simplifica, ya que solo tenemos que buscar
las subcadenas `D-RD-R-x`, `R-D-RD-x` y `D-LD-L-y`.

