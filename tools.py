from typing import List
from classes import Point, Rectangle

def get_new_vertices(vertex: Point, solar_panel: Rectangle , direction: str) -> List[Point]:
  """
  Retorna los tres vertices del panel solar (considerando que uno corresponde al vertice del techo)
  """
  solar_panel_with_rotation = solar_panel
  if direction[2] == 'H':
    solar_panel_with_rotation = Rectangle(solar_panel.height, solar_panel.width)
  height_multiplier = 1 if direction[0] == 'U' else -1
  width_multiplier = 1 if direction[1] == 'R' else -1
  corner_vector = Point(
    solar_panel_with_rotation.width * width_multiplier,
    solar_panel_with_rotation.height * height_multiplier
  )
  new_vertices = [
    Point(corner_vector.x + vertex.x, vertex.y),
    Point(corner_vector.x + vertex.x, corner_vector.y + vertex.y),
    Point(vertex.x, corner_vector.y + vertex.y),
  ]
  return new_vertices

def chop_vertices(vertex: Point, new_vertices: List[Point], vertices: List[Point]) -> List[Point]:
  """
  Toma los nuevos vertices y en caso de que ya esten presentes en la lista original los elimina.
  Tambien elimina el vertice donde se coloca el panel solar. En caso de que no esten presentes
  los agrega a la lista de vertices
  """
  new_iteration_vertices = vertices.copy()
  new_iteration_vertices.remove(vertex)
  for new_vertex in new_vertices:
    if new_vertex in new_iteration_vertices:
      new_iteration_vertices.remove(new_vertex)
    else:
      new_iteration_vertices.append(new_vertex)
  return new_iteration_vertices

def is_vertex_inside(new_vertex: Point, vertices: List[Point]) -> bool:
  """
  Retorna True si el vertice esta dentro de la region delimitada por los vertices
  Para esto se buscan los vertices arriba y a la derecha del nuevo vertice. Si la cantidad 
  es par entonces el vertice esta fuera de la region, si es impar entonces esta dentro
  """
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
  """
  Itera sobre todos los nuevos vertices y verifica si todos estan dentro de la region
  delimitada por los vertices.
  """
  for new_vertex in new_vertices:
    if not is_vertex_inside(new_vertex, vertices):
      return False
  return True

def check_input(x: str, type_: type, message: str) -> type:
  """
  Pregunta por el input del usuario y verifica que sea del tipo correcto
  """
  try:
    return type_(x)
  except ValueError:
    print(message)
    print('para salir presione Ctrl + C')
    return check_input(input(), type_, message)
    