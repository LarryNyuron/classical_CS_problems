from __future__ import annotations
from typing import List, Optional
from generic_search import breadth_first_search, Node, node_to_path

MAX_NUM: int = 3

class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.west_m: int = missionaries
        self.west_c: int = cannibals
        self.east_m: int = MAX_NUM - self.west_m
        self.east_c: int = MAX_NUM - self.west_c
        self.boat: bool = boat

    def __str__(self) -> str:
        return ('On the west bank there r {} missi & {} canni. On the east bank there r {} missi & {} canni. The boat is on the {} bank').format(self.west_m, self.west_c, self.east_m, self.east_c, ('west' if self.boat else 'east'))

    def goal_test(self) -> bool:
        return self.is_legal and self.east_m == MAX_NUM and self.east_c == MAX_NUM

    @property
    def is_legal(self) -> bool:
        if self.west_m < self.west_c and self.west_m > 0:
            return False
        if self.west_c < self.east_c and self.east_m > 0:
            return False
        return True

    def successors(self) -> List[MCState]:
        sucs: List[MCState] = []
        #boat on west bank
        if self.boat:
            if self.west_m > 1 :
                sucs.append(MCState(self.west_m - 2, self.west_c, not self.boat))
            if self.west_m > 0 :
                sucs.append(MCState(self.west_m - 1, self.west_c, not self.boat))
            if self.west_c > 1 :
                sucs.append(MCState(self.west_m, self.west_c - 2, not self.boat))
            if self.west_c > 0 :
                sucs.append(MCState(self.west_m, self.west_c - 1, not self.boat))
            if (self.west_c > 0) and (self.west_m > 0) :
                sucs.append(MCState(self.west_m - 1, self.west_c - 1, not self.boat))
        else:
            if self.east_m > 1 :
                sucs.append(MCState(self.west_m + 2, self.west_c, not self.boat))
            if self.east_m > 0 :
                sucs.append(MCState(self.west_m + 1, self.west_c, not self.boat))
            if self.east_c > 1 :
                sucs.append(MCState(self.west_m, self.west_c + 2, not self.boat))
            if self.east_c > 0 :
                sucs.append(MCState(self.west_m, self.west_c + 1, not self.boat))
            if (self.east_c > 0) and (self.east_m > 0) :
                sucs.append(MCState(self.west_m + 1, self.west_c + 1, not self.boat))
        return [x for x in sucs if x.is_legal]

def display_solution(path: List[MCState]):
    #health check
    if len(path) == 0:
        return
    old_state: MCState = path[0]
    print(old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print('{} missi & {} canni moved from E to W \n'.format(old_state.east_m - current_state.east_m, old_state.east_c - current_state.east_c))
        else:
            print('{} missi & {} canni moved from W to E \n'.format(old_state.west_m - current_state.west_m, old_state.west_c - current_state.west_c))
        print(current_state)
        old_state = current_state


if __name__ == '__main__':
    start: MCState = MCState(MAX_NUM, MAX_NUM, True)
    solution: Optional[Node[MCState]] = breadth_first_search(start, MCState.goal_test, MCState.successors)
    if solution is None:
        print('No solution found!')
    else:
        path: List[MCState] = node_to_path(solution)
        display_solution(path)