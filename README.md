# Ruuf, Tarea

## Descripción de la solucion

El approach que se utilizó fue tomar el techo y obtener los vertices en el plano carstesiano,luego iremos probando colocar los paneles solares de 8 formas posibles en cada vertice (el panel horizontal o vertical y cada uno de los 4 vertices del panel en el vertice del techo). Si se puede colocar cortamos el techo, y ahora hacemos lo mismo con el resto del techo, de manera recursiva se obtienen los vertices posibles. Notar que esta solucion debiese encontrar la solucion optima a costo de ser muy lenta cuando el techo es mucho mas grande que el panel solar. Debido a este costo es que se utilizo un approach greedy para encontrar una solucion aproximada, este consiste en que cuando una pieza encaje, nos quedamos con ella sin considerar si en otra orientacion podría encajar. Dado que esta es significativamente mas rapida, se ejecuta varias veces aleatorizando el orden de las orientaciones y se toma la mejor solucion.

## Instrucciones de uso

Se le pueden pasar entregar las dimensiones del techo y el panel solar directamente en main, descomentando la linea 63 y comentando la 64 o se pueden entregar por consola que es como viene por defecto.

## Ejeccucion

Para ejecutar el programa se debe correr el siguiente comando en la terminal:

```bash
python main.py
```
