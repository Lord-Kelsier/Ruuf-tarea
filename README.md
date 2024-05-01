# Ruuf, Tarea

## Descripción de la solucion

El approach que se utilizó fue tomar el techo y obtener los vertices en el plano carstesiano,luego iremos probando colocar los paneles solares de 8 formas posibles en cada vertice (el panel horizontal o vertical y cada uno de los 4 vertices del panel en el vertice del techo). Si se puede colocar cortamos el techo, y ahora hacemos lo mismo con el resto del techo, de manera recursiva se obtienen los vertices posibles. Notar que esta solucion debiese encontrar la solucion optima a costo de ser muy lenta cuando el techo es mucho mas grande que el panel solar. Debido a este costo es que se utilizo un approach greedy para encontrar una solucion aproximada, este consiste en que cuando una pieza encaje, nos quedamos con ella sin considerar si en otra orientacion podría encajar. Dado que esta es significativamente mas rapida, se ejecuta varias veces aleatorizando el orden de las orientaciones y se toma la mejor solucion.

## Instrucciones de uso

Se le pueden pasar entregar las dimensiones del techo y el panel solar directamente en main, descomentando la linea 73 y comentando la 74 o se pueden entregar por consola que es como viene por defecto.

## Ejeccucion

Para ejecutar el programa se debe correr el siguiente comando en la terminal:

```bash
python main.py
```

## Consideraciones adicionales

El programa al utilizar un acercamiento greedy, no siempre va a encontrar la solucion optima, especialmente cuando el techo es mucho mas grande que el panel solar. En estos casos es mejor utilizar otro algoritmo. La decision de hacerlo de esta manera es generalizar el problema para abarcar el bonus (opcion 2), ya que se podria modelar con el mismo concepto.

No considere necesario (dada la corta extension de la tarea) documentar mucho mas el codigo, ya que es bastante reducido.
Tambien respescto al linting de python, hay una peculiaridad y es que siempre prefiero que la indentacion sea de 2 espacios, por lo que si se corre un linter van a saltar warnings por todos lados. Es solo una preferencia personal y no afecta en nada el funcionamiento del codigo.
