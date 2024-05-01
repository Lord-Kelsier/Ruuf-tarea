from typing import List
from dataclasses import dataclass
from random import shuffle

@dataclass(frozen=True)
class Rectangle:
  width: float
  height: float

@dataclass(frozen=True)
class Point:
  x: float
  y: float

def get_new_vertices(vertex: Point, solar_panel:Rectangle , direction: str) -> List[Point]:
  solar_panel_with_rotation = solar_panel if direction[2] == 'V' else Rectangle(solar_panel.height, solar_panel.width)
  height_multiplier = 1 if direction[0] == 'U' else -1
  width_multiplier = 1 if direction[1] == 'R' else -1
  corner_vector = Point(solar_panel_with_rotation.width * width_multiplier, solar_panel_with_rotation.height * height_multiplier)
  new_vertices = [
    Point(corner_vector.x + vertex.x, vertex.y),
    Point(corner_vector.x + vertex.x, corner_vector.y + vertex.y),
    Point(vertex.x, corner_vector.y + vertex.y),
  ]
  return new_vertices

def chop_vertices(vertex: Point, new_vertices: List[Point], vertices: List[Point]) -> List[Point]:
  # cortamos el techo al sacar el vertice y colocar los nuevos vertices del panel solar
  new_iteration_vertices = vertices.copy()
  new_iteration_vertices.remove(vertex)
  for new_vertex in new_vertices:
    if new_vertex in new_iteration_vertices:
      new_iteration_vertices.remove(new_vertex)
    else:
      new_iteration_vertices.append(new_vertex)
  new_iteration_vertices = new_iteration_vertices
  return new_iteration_vertices

def is_vertex_inside(new_vertex: Point, vertices: List[Point]) -> bool:
  # Buscamos los vertices con componente x e y mayor a los nuevos vertices
  if new_vertex in vertices:
    return True
  x = new_vertex.x
  y = new_vertex.y
  vertices_up = [vertex for vertex in vertices if vertex.y > y and vertex.x >= x]
  vertices_right = [vertex for vertex in vertices if vertex.x > x and vertex.y >= y]
  if len(vertices_up) % 2 == 0 and len(vertices_right) % 2 == 0:
    return False    
  return True
def does_fit(new_vertices: List[Point], vertices: List[Point]) -> bool:
  for new_vertex in new_vertices:
    if not is_vertex_inside(new_vertex, vertices):
      return False
  return True
    

def calculate_tiles(vertices: List[Point], solar_panel: Rectangle) -> int:
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

def main(roof: Rectangle, solar_panel: Rectangle) -> None:
  x, y = roof.width, roof.height
  if solar_panel.height > y and solar_panel.height> x:
    print(0)
    return
  if solar_panel.width > y and solar_panel.width > x:
    print(0)
    return
  vertices = [
    Point(0, 0),
    Point(x, 0),
    Point(x, y),
    Point(0, y)
  ]
  max_possible = x * y // (solar_panel.width * solar_panel.height)
  max_tiles = 0
  print('Numero maximo de paneles que se pueden colocar:', max_possible)
  for _ in range(20):
    tiles = calculate_tiles(vertices, solar_panel)
    if tiles == max_possible:
      max_tiles = max_possible
      break
    max_tiles = max(max_tiles, tiles)
  print('Paneles solares encajados: ',tiles)

if __name__ == '__main__':
  roof = Rectangle(6, 7)
  solar_panel = Rectangle(3, 2)
  main(roof, solar_panel)

