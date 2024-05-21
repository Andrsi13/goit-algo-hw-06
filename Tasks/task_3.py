from task_1 import G
import networkx as nx

# Виведення списку суміжностей графа з вагами ребер
adjacency_dict_with_weights = nx.to_dict_of_dicts(G)
graph_with_weights = {}
for vertex, neighbors in adjacency_dict_with_weights.items():
    weighted_neighbors = {neighbor: G[vertex][neighbor]['weight'] for neighbor in neighbors}
    graph_with_weights[vertex] = weighted_neighbors


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    previous_vertices = {vertex: None for vertex in graph}

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances, previous_vertices

def shortest_path(graph, start, target):
    distances, previous_vertices = dijkstra(graph, start)
    path = []
    current_vertex = target

    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = previous_vertices[current_vertex]
    
    path = path[::-1]
    if path[0] == start:
        return path
    else:
        return None

if __name__ == "__main__":
    start_vertex = "Північний район"
    target_vertex = "Західний район"
    shortest_path_result = shortest_path(graph_with_weights, start_vertex, target_vertex)
    
    print(f"Найкоротший шлях від {start_vertex} до {target_vertex}: {shortest_path_result}")