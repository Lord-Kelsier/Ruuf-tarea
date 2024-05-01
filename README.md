# Ruuf, Tarea

## Descripción de la solucion

El approach que se utilizó fue tomar el techo y obtener los vertices en el plano carstesiano,luego iremos probando colocar los paneles solares de 8 formas posibles en cada vertice (el panel horizontal o vertical y cada uno de los 4 vertices del panel en el vertice del techo). Si se puede colocar cortamos el techo, y ahora hacemos lo mismo con el resto del techo, de manera recursiva se obtienen los vertices posibles. Notar que esta solucion debiese encontrar la solucion optima a costo de ser muy lenta cuando el techo es mucho mas grande que el panel solar.
