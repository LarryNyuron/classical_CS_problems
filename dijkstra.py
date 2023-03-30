'''
Dijkstra's algorithm solves the problem of finding the shortest path from one vertex.
The initial vertex is given, and the algorithm returns the path with the least weight
to any other vertex in the weighted graph. It also returns the minimum
total weight for the path from the initial vertex to each of the remaining ones.
 Algorithm
Dijkstra starts from one source vertex and then continuously explores
the nearest peaks to it. For this reason, Dijkstra's algorithm, like the algorithm
Yarnik, is greedy. When Dijkstra's algorithm explores a new vertex,
it checks how far it is from the starting vertex and updates this
value if it finds a shorter path. Like a breadth-first search algorithm,
it keeps track of which edges lead to each vertex.
Dijkstra's algorithm performs such steps.
1. Add the starting vertex to the priority queue.
2. Extract the nearest vertex from the priority queue (at first it is only
the original vertex) - let's call it the current one.
3. Explore all neighboring vertices connected to the current one. If they have
not been written before, or if an edge offers a new shortest path, then for
write down the distance to the initial vertex for each of these vertices, specify
an edge corresponding to this distance, and add a new vertex to the
priority queue.
4. Repeat steps 2 and 3 until the priority queue is empty.
5. Return the shortest distance to each vertex from the initial one and
the path that allows you to get to each of them.
'''
from __future__ import annotations
from typing import TypeVar, List, Optional, Tuple, Dict
from dataclasses import dataclass
from mst import WeightedPath, print_weighted_path
from weighted_graph import WeightedGraph
from weighted_edge import WeightedEdge
from priority_queue import PriorityQueue


V = TypeVar('V')


@dataclass
class DijkstraNode:
    vertex: int
    distance: float

    def  __lt__(self, other: DijkstraNode) -> bool:
        return self.distance < other.distance

    def __eq__(self, other: DijkstraNode) -> bool:
        return self.distance == other.distance


def dijkstra(wg: WeightedGraph[V], root: V) -> Tuple[List[Optional[float]], Dict[int, WeightedEdge]]:
    first: int = wg.index_of(root)
    distance: List[Optional[float]] = [None] * wg.vertex_count
    distance[first] = 0
    path_dict: Dict[int, WeightedEdge] = {}
    pq: PriorityQueue[DijkstraNode] = PriorityQueue()
    pq.push(DijkstraNode(first, 0))

    while not pq.empty:
        u: int = pq.pop()
        dist_u: float = distance[u]
        for we in wg.edges_for_index(u):
            dist_v: float = distance[we.v]
            if dist_v is None or dist_v > we.weight + dist_u:
                distance[we.v] = we.weight + dist_u
                path_dict[we.v] = we
                pq.push(DijkstraNode(we.v, we.weight + dist_u))
    return distance, path_dict

def distance_array_to_vertex_dict(wg: WeightedGraph[V], distances: List[Optional[float]]) -> Dict[V, Optional[float]]:
    distance_dict: Dict[V, Optional[float]] = {}
    for i in range(len(distances)):
        distance_dict[wg.vertex_at(i)] = distances[i]
    return distance_dict


def path_dict_to_path(start:  int, end: int, path_dict: Dict[int, WeightedEdge]) -> WeightedPath:
    if len(path_dict) == 0:
        return []
    edge_path: WeightedPath = []
    e: WeightedEdge = path_dict[end]
    edge_path.append(e)
    while e.u != start:
        e = path_dict[e.u]
        edge_path.append(e)
    return list(reversed(edge_path))


if __name__ == '__main__':
    city_graph2: WeightedGraph[str] = WeightedGraph(["Seattle", "San Francisco",\
         "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", \
    "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", \
    "Philadelphia", "Washington"])
    city_graph2.add_edge_by_vertices("Seattle", "Chicago", 1737)
    city_graph2.add_edge_by_vertices("Seattle", "San Francisco", 678)
    city_graph2.add_edge_by_vertices("San Francisco", "Riverside", 386)
    city_graph2.add_edge_by_vertices("San Francisco", "Los Angeles", 348)
    city_graph2.add_edge_by_vertices("Los Angeles", "Riverside", 50)
    city_graph2.add_edge_by_vertices("Los Angeles", "Phoenix", 357)
    city_graph2.add_edge_by_vertices("Riverside", "Phoenix", 307)
    city_graph2.add_edge_by_vertices("Riverside", "Chicago", 1704)
    city_graph2.add_edge_by_vertices("Phoenix", "Dallas", 887)
    city_graph2.add_edge_by_vertices("Phoenix", "Houston", 1015)
    city_graph2.add_edge_by_vertices("Dallas", "Chicago", 805)
    city_graph2.add_edge_by_vertices("Dallas", "Atlanta", 721)
    city_graph2.add_edge_by_vertices("Dallas", "Houston", 225)
    city_graph2.add_edge_by_vertices("Houston", "Atlanta", 702)
    city_graph2.add_edge_by_vertices("Houston", "Miami", 968)
    city_graph2.add_edge_by_vertices("Atlanta", "Chicago", 588)
    city_graph2.add_edge_by_vertices("Atlanta", "Washington", 543)
    city_graph2.add_edge_by_vertices("Atlanta", "Miami", 604)
    city_graph2.add_edge_by_vertices("Miami", "Washington", 923)
    city_graph2.add_edge_by_vertices("Chicago", "Detroit", 238)
    city_graph2.add_edge_by_vertices("Detroit", "Boston", 613)
    city_graph2.add_edge_by_vertices("Detroit", "Washington", 396)
    city_graph2.add_edge_by_vertices("Detroit", "New York", 482)
    city_graph2.add_edge_by_vertices("Boston", "New York", 190)
    city_graph2.add_edge_by_vertices("New York", "Philadelphia", 81)
    city_graph2.add_edge_by_vertices("Philadelphia", "Washington", 123)
    distances, path_dict = dijkstra(city_graph2, "Los Angeles")
    name_distance: Dict[str, Optional[int]] = distance_array_to_vertex_dict(city_graph2, distances)
    print("Distances from Los Angeles:")
    for key, value in name_distance.items():
        print(f"{key} : {value}")
    print ("") # пустая строка
    print("Shortest path from Los Angeles to Boston:")
    path: WeightedPath = path_dict_to_path(city_graph2.index_of("Los Angeles"), city_graph2.index_of("Boston"), path_dict)
    print_weighted_path(city_graph2, path)