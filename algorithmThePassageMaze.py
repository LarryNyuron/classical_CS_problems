from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import depth_first_search, node_to_path, Node, breadth_first_search, astar


class Cell(str, Enum):
    EMPTY = ' '
    BLOCKED = 'X'
    START = 'S'
    GOAL = 'G'
    PATH = '*'


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2, start: MazeLocation = (0, 0), goal: MazeLocation = MazeLocation(9, 9)) -> None:
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        self._randomly_fill(rows, columns, sparseness)
        self._grid[start[0]][start[1]] = Cell.START
        self._grid[goal[0]][goal[1]] = Cell.GOAL

    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        output: str = ''
        for row in self._grid:
            output += ''.join([c.value for c in row]) + '\n'
        return output

    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    def successors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if ml[0] + 1 < self._rows and self._grid[ml[0] + 1][ml[1]] != Cell.BLOCKED:
            locations.append(MazeLocation(ml[0] + 1, ml[1]))
        if ml[0] - 1 >= 0 and self._grid[ml[0] - 1][ml[1]] != Cell.BLOCKED:
            locations.append(MazeLocation(ml[0] - 1, ml[1]))
        if ml[1] + 1 < self._columns and self._grid[ml[0]][ml[1] + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml[0], ml[1] + 1))
        if ml[1] - 1 >= 0 and self._grid[ml[0]][ml[1] - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml[0], ml[1] - 1))
        return locations

    def mark(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location[0]][maze_location[1]] = Cell.PATH
        self._grid[self.start[0]][self.start[1]] = Cell.START
        self._grid[self.goal[0]][self.goal[1]] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location[0]][maze_location[1]] = Cell.EMPTY
        self._grid[self.start[0]][self.goal[1]] = Cell.START
        self._grid[self.goal[0]][self.goal[1]] = Cell.GOAL


def euclidean_dist(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        xdist: int = ml[1] - goal[1]
        ydist: int = ml[0] - goal[0]
        return sqrt((xdist * xdist) + (ydist * ydist))
    return distance

def manhattan_dist(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    def distance(ml: MazeLocation) -> float:
        xdist: int = abs(ml[1] - goal[1])
        ydist: int = abs(ml[0] - goal[0])
        return (xdist + ydist)
    return distance

if __name__ == '__main__':
    m: Maze= Maze()
    print(m)
    solution1: Optional[Node[MazeLocation]] = depth_first_search(m.start, m.goal_test, m.successors)
    if solution1 is None:
        print('Sorry, bro, path does not exist')
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)

    solution2: Optional[Node[MazeLocation]] = breadth_first_search(m.start, m.goal_test, m.successors)
    if solution2 is None:
        print('Sorry, bro, path does not exist')
    else:
        path2: List[MazeLocation] = node_to_path(solution2)
        m.mark(path2)
        print(m)
        m.clear(path2)

    distance: Callable[[MazeLocation], float] = manhattan_dist(m.goal)
    solutionЗ: Optional[Node[MazeLocation]] = astar(m.start, m.goal_test, m.successors, distance)
    if solutionЗ is None:
        print("No solution found using А*!")
    else:
        pathЗ: List[MazeLocation] = node_to_path(solutionЗ)
        m.mark(pathЗ)
        print(m)