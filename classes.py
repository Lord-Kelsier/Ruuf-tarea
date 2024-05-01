from dataclasses import dataclass

@dataclass(frozen=True)
class Rectangle:
  width: float
  height: float

@dataclass(frozen=True)
class Point:
  x: float
  y: float
