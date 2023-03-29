'''
Yarnik's algorithm for finding a minimal spanning tree solves the problem
by dividing the graph into two parts: vertices in the formed minimal
spanning tree and vertices that are not yet included in the minimal spanning
tree.
The algorithm performs the following steps.
1. Select an arbitrary vertex to include in the minimal spanning
tree.
2. Find the edge with the lowest weight connecting the minimum spanning tree
 with vertices not yet included in the minimum spanning tree.
3. Add the vertex located at the end of this minimal edge to the minimal
spanning tree.
4. Repeat steps 2 and 3 until all vertices of the graph are included in
 the minimal spanning tree.
'''
from typing import TypeVar, List, Optional
from weighted_graph import WeightedGraph
from weighted_edge import  WeightedEdge
from priority_queue import PriorityQueue


V = TypeVar('V')
WeightedPath = List[WeightedEdge]


def total_weight(wp: WeightedPath) -> float:
    return sum([e.weight for e in wp])


def mst(wg: WeightedGraph[V], start: int = 0) -> Optional[WeightedPath]:
    if start > (wg.vertex_count - 1) or start < 0:
        return None
    #count ends MST
    result: WeightedPath = []
    pq: PriorityQueue[WeightedEdge] = PriorityQueue()
    #visited vertex
    visited: [bool] = [False] * wg.vertex_count

    def visit(index: int):
        visited[index] = True
        for edge in wg.edges_for_index(index):
            if not visited[edge.v]:
                pq.push(edge)

    visit(start)

    while not pq.empty:
        edge = pq.pop()
        if visited[edge.v]:
            continue
            result.append(edge)
            visit(edge.v)
        return result


def print_weighted_path(wg: WeightedGraph, wp: WeightedPath) -> None:
    for edge in wp:
        print(f'{wg.vertex_at(edge.u)} {edge.weight} > {wg.vertex_at(edge.v)}')
    print(f'Total eight: {total_weight(wp)}')


if __name__ == '__main__':
    city_graph2: WeightedGraph[str] = WeightedGraph(["Seattle","San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])
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
    result: Optional[WeightedPath] = mst(city_graph2)
    if result is None:
        print("No solution found!")
    else:
        print_weighted_path(city_graph2, result)