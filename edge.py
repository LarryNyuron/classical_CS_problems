from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Edge:
    #the vertex 'from wrere'
    u: int
    #the vertex 'where'
    v: int

    def reversed(self) -> Edge:
        return Edge(self.v, self.u)

    def __str__(self) -> str:
        return f'{self.u} -> {self.v}'
