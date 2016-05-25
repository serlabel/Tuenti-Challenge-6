# Challenge 13 - Legacy Code

En este caso tenemos un programa para la Sinclair ZX Spectrum del cual queremos
saber que hace.

A partir del binario, hemos obtenido el código ensamblador mediante un
desensamblador para código `z80`. Aparentemente, lo único que hace este programa
es cargar en memoria una serie de datos.

Sin embargo, si conocemos la [estructura de la memoria]
(http://www.animatez.co.uk/computers/zx-spectrum/screen-memory-layout/) de la Sinclair ZX Spectrum,
el bloque donde está cargando los datos corresponde a la memoria utilizada para la pantalla.

A partir de la información sobre la codificación de la pantalla, se puede comprobar
que el programa muestra el siguiente mensaje por pantalla:

![GAMEOVER](output.png)
