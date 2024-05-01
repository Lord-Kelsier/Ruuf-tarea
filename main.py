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

def get_new_vertices(vertex: Point, vertices: List[Point], direction: str) -> List[Point]:
  # cortamos el techo al sacar el vertice y colocar los nuevos vertices del panel solar
  pass

def does_fit(
    vertex: Point,
    solar_panel: Rectangle,
    vertices: List[Point],
    direction: str) -> bool:
  pass

def calculate_tiles(vertices: List[Point], solar_panel: Rectangle) -> int:
  max_tiles = 0
  for vertex in vertices:
    fitted_once = False
    for direction in ['ULV', 'URV', 'DLV', 'DRV', 'ULH', 'URH', 'DLH', 'DRH']:
      if does_fit(vertex, solar_panel, vertices, direction):
        fitted_once = True
        new_vertices = get_new_vertices(vertex, vertices, direction)
        tiles = calculate_tiles(new_vertices, solar_panel) + 1
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

