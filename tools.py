from classes import Point, Rectangle
from typing import List

def get_new_vertices(vertex: Point, solar_panel: Rectangle , direction: str) -> List[Point]:
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

def check_input(x: str, type_: type, message: str) -> type:
  pass