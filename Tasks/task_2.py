import networkx as nx
from task_1 import G

# Виведення списку суміжностей графа
adjacency_dict = nx.to_dict_of_lists(G)
graph = {}
print("Список суміжностей графа:")
for vertex, neighbors in adjacency_dict.items():
    graph[vertex] = neighbors
print(graph)