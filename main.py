from typing import List
from dataclasses import dataclass

@dataclass(frozen=True)
class Rectangle:
  width: float
  height: float

@dataclass(frozen=True)
class Point:
  x: float
  y: float

def get_new_vertices(vertex: Point, vertices: List[Point], solar_panel:Rectangle , direction: str) -> List[Point]:
  solar_panel_with_rotation = solar_panel if direction[2] == 'V' else Rectangle(solar_panel.height, solar_panel.width)
  height_multiplier = 1 if direction[0] == 'U' else -1
  width_multiplier = 1 if direction[1] == 'R' else -1
  corner_vector = Point(solar_panel_with_rotation.width * width_multiplier, solar_panel_with_rotation.height * height_multiplier)
  new_vertices = [
    Point(corner_vector.x + vertex.x, vertex.y),
    Point(corner_vector.x + vertex.x, corner_vector.y + vertex.y),
    Point(vertex.y, corner_vector.y + vertex.y),
  ]
  return new_vertices

def chop_vertices(vertex: Point, new_vertices: List[Point], vertices: List[Point]) -> List[Point]:
  # cortamos el techo al sacar el vertice y colocar los nuevos vertices del panel solar
  pass
def does_fit(new_vertices: List[Point], vertices: List[Point]) -> bool:
  # tomamos la lista de pountos cuyo valor en x es mayor o igual a cada new vertex, igualmente para el valor en y
  # si es par entonces el punto esta fuera del techo
  for new_vertex in new_vertices:
    x = new_vertex.x
    y = new_vertex.y
    x_lines = {vertex.x for vertex in vertices}
    y_lines = {vertex.y for vertex in vertices} # deben ser conjuntos para evitar duplicados

    if len(list(filter(lambda point: point.x >= x ,x_lines))) % 2 == 0:
      return False
    if len(list(filter(lambda point: point.y >= y ,y_lines))) % 2 == 0:
      return False
  return True

def calculate_tiles(vertices: List[Point], solar_panel: Rectangle) -> int:
  max_tiles = 0
  for vertex in vertices:
    fitted_once = False
    for direction in ['ULV', 'URV', 'DLV', 'DRV', 'ULH', 'URH', 'DLH', 'DRH']:
      new_vertices = get_new_vertices(vertex, vertices, solar_panel, direction)
      if does_fit(new_vertices, vertices):
        fitted_once = True
        new_iteration_vertices = chop_vertices(vertex, new_vertices, vertices)
        tiles = calculate_tiles(new_iteration_vertices, solar_panel) + 1
        max_tiles = max(max_tiles, tiles)
    if not fitted_once:
      return 0
  return max_tiles

def main(roof: Rectangle, solar_panel: Rectangle) -> None:
  x, y = roof.width, roof.height
  vertices = [
    Point(0, 0),
    Point(x, 0),
    Point(x, y),
    Point(0, y)
  ]

  tiles = calculate_tiles(vertices, solar_panel)
  print(tiles)

if __name__ == '__main__':
  roof = Rectangle(10, 10)
  solar_panel = Rectangle(2, 1)
  main(roof, solar_panel)

