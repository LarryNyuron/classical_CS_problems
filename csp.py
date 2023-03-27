from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod


V = TypeVar('V')
D = TypeVar('D')


class Constraint(Generic[V,D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, assignment: Dict[V,D]) -> bool:


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