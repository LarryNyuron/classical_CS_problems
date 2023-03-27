from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod


V = TypeVar('V')
D = TypeVar('D')


class Constraint(Generic[V,D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V,D]) -> bool:
        pass


class CSP(Generic[V,D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        #variables that will be limitede
        self.variables: List[V] = variables
        #domain every variables
        self.domains: Dict[V, List[D]] = domains
        self.constarints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constarints[variable] = []
            if variable not in self.domains:
                raise LookupError('Every variable should have a domain assigned to it')

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError('Var in constraint not in CSP')
            else:
                self.constarints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V,D]) -> bool:
        for constraint in self.constarints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        # assignment is completed if assignment exists
        # for each variable (base case)
        if len(assignment) == len(self.variables):
            return assignment

        # give all var from CSP, but not from assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]

        # get all possible values of the definition area
        # for the first variable without assignment
        first: V = unassigned[0]
        for value in self.domains[first]:
            local_assign = assignment.copy()
            local_assign[first] = value
            # if there are no contradictions, then we continue the recursion
            if self.consistent(first, local_assign):
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assign)
                if result is not None:
                    return result
        return None