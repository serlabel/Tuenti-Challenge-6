# Challenge 9 - 0-1 Immiscible numbers

El objetivo de este problema es calcular el menor múltiplo de un número **N**
que tenga la forma **1^a 0^b** .

Primero vamos a calcular el número de ceros que tendrá el múltiplo que buscamos.
La descomposición factorial de **10** es **2 x 5**, de forma que un múltiplo con
***k*** ceros tendrá en su descomposición **2^k x 5^k**.

Resumiendo, como el múltiplo debe ser el menor posible, el número de ceros (**b**) será:
```
b = max(n, m)
```
donde **N = 2^n x 5^m x N'**.

A partir de aquí, tenemos el número **N'** cuyo múltiplo correspondiente es **1^a**.
Por lo tanto, podemos calcular el número de unos del múltiplo de **N** a partir de **N'**.

Vamos a ir comprobando todos los números de la forma **1^a** hasta encontar aquel
que sea múltiplo de **N'**. Para este cálculo será necesario aplicar matemática
modular, ya que el múltiplo puede ser un número muy alto:

``` python
ones = 1  # número de unos (a)
n = 1 % x  # primera iteración: n = 1
while n != 0:
    n = ((10*n) % x + 1) % x  # siguientes iteraciones: 11, 111, ...
    ones += 1
```
donde `x` es el número **N'**.
