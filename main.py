import math
from typing import List, Tuple
from random import shuffle
from classes import Point, Rectangle
from tools import get_new_vertices, chop_vertices, does_fit, check_input

def calculate_tiles(vertices: List[Point], solar_panel: Rectangle) -> int:
  """ 
  Funcion recursiva que calcula el numero de paneles que caben en un espacio delimitado por vertices
  """
  shuffle(vertices)
  max_tiles = 0
  for vertex in vertices:
    fitted_once = False
    directions = ['ULV', 'URV', 'DLV', 'DRV', 'ULH', 'URH', 'DLH', 'DRH']
    shuffle(directions)
    for direction in directions:
      new_vertices = get_new_vertices(vertex, solar_panel, direction)
      if does_fit(new_vertices, vertices):
        fitted_once = True
        new_iteration_vertices = chop_vertices(vertex, new_vertices, vertices)
        return calculate_tiles(new_iteration_vertices, solar_panel) + 1
    if not fitted_once:
      return 0
  return max_tiles

def ask_for_input() -> Tuple[Rectangle, Rectangle]:
  """
  Funcion que pide al usuario las dimensiones del techo y del panel solar
  """
  x = input('Ingrese el ancho del techo: ')
  x = check_input(x, float, 'Ingrese un numero: ')
  y = input('Ingrese el largo del techo: ')
  y = check_input(y, float, 'Ingrese un numero: ')
  roof = Rectangle(x, y)
  a = input('Ingrese el ancho del panel solar: ')
  a = check_input(a, float, 'Ingrese un numero: ')
  b = input('Ingrese el largo del panel solar: ')
  b = check_input(b, float, 'Ingrese un numero: ')
  solar_panel = Rectangle(a, b)
  return roof, solar_panel

def get_max_tiles(roof: Rectangle = None, solar_panel: Rectangle = None) -> None:
  """
  Inicializa los vertices a partir de las dimensiones del techo y llama a la funcion calculate_tiles
  """
  if not roof or not solar_panel:
    roof, solar_panel = ask_for_input()
  x, y = roof.width, roof.height
  if solar_panel.height > y and solar_panel.height> x:
    return 0
  if solar_panel.width > y and solar_panel.width > x:
    return 0
  vertices = [
    Point(0, 0),
    Point(x, 0),
    Point(x, y),
    Point(0, y)
  ]
  max_possible = math.floor(x * y / (solar_panel.width * solar_panel.height))
  max_tiles = 0
  for _ in range(20):
    tiles = calculate_tiles(vertices, solar_panel)
    if tiles == max_possible:
      max_tiles = max_possible
      break
    max_tiles = max(max_tiles, tiles)
  return max_tiles

if __name__ == '__main__':
  roof = Rectangle(6, 7)
  solar_panel = Rectangle(3, 2)
  # max_tiles = get_max_tiles(roof, solar_panel)
  max_tiles = get_max_tiles()
  print(max_tiles)
