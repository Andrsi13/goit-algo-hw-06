import networkx as nx
from task_1 import G
from collections import deque
import timeit

# Виведення списку суміжностей графа
adjacency_dict = nx.to_dict_of_lists(G)
graph = {}
for vertex, neighbors in adjacency_dict.items():
    graph[vertex] = neighbors


def dfs_shortest_path(graph, current_vertex, target_vertex, path=None, shortest_path=None):
    if path is None:
        path = [current_vertex]
    else:
        path = path + [current_vertex]
    
    if current_vertex == target_vertex:
        return path
    
    for neighbor in graph[current_vertex]:
        if neighbor not in path:
            new_path = dfs_shortest_path(graph, neighbor, target_vertex, path, shortest_path)
            if new_path:
                if shortest_path is None or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    
    return shortest_path

def bfs_shortest_path(graph, queue, target_vertex, visited=None, paths=None):
    if visited is None:
        visited = set()
    if paths is None:
        paths = {queue[0]: [queue[0]]}
    
    if not queue:
        return None
    
    vertex = queue.popleft()
    
    if vertex == target_vertex:
        return paths[vertex]
    
    if vertex not in visited:
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                # Зберігаємо шлях до сусіда
                paths[neighbor] = paths[vertex] + [neighbor]
    
    return bfs_shortest_path(graph, queue, target_vertex, visited, paths)


if __name__ == "__main__":
    # Початкова і цільова вершини
    start_vertex = "Північний район"
    target_vertex = "Західний район"

    # Виклик функцій і вимірювання часу виконання DFS
    dfs_time = timeit.timeit(lambda: dfs_shortest_path(graph, start_vertex, target_vertex), number=10)
    shortest_path_dfs = dfs_shortest_path(graph, start_vertex, target_vertex)
    
    # Виклик функцій і вимірювання часу виконання BFS
    bfs_time = timeit.timeit(lambda: bfs_shortest_path(graph, deque([start_vertex]), target_vertex), number=10)
    shortest_path_bfs = bfs_shortest_path(graph, deque([start_vertex]), target_vertex)

    # Виведення результатів
    print(f"Найкоротший шлях методом DFS від {start_vertex} до {target_vertex}: {shortest_path_dfs}")
    print(f"Час виконання DFS: {dfs_time} секунд")
    
    print(f"Найкоротший шлях методом BFS від {start_vertex} до {target_vertex}: {shortest_path_bfs}")
    print(f"Час виконання BFS: {bfs_time} секунд")