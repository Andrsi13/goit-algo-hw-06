import networkx as nx
import matplotlib.pyplot as plt

# Створюємо порожній граф
G = nx.Graph()

# Додаємо вузли (Локації міста)
G.add_node("Північний вїзд")
G.add_node("Західний вїзд")
G.add_node("Східний район")
G.add_node("Західний район")
G.add_node("Північний район")
G.add_node("Індустріальний район")
G.add_node("Центр")
G.add_node("Пд-Зх район")
G.add_node("Новий Південний район")
G.add_node("Старий Південний район")
G.add_node("Південний вїзд")


# Додаємо ребра (дороги) з вагами (відстанями в кілометрах)
G.add_edge("Північний вїзд", "Західний вїзд", weight=15)
G.add_edge("Північний вїзд", "Північний район", weight=2)
G.add_edge("Північний вїзд", "Східний район", weight=5)
G.add_edge("Північний район", "Східний район", weight=4)
G.add_edge("Північний район", "Центр", weight=6)
G.add_edge("Західний вїзд", "Західний район", weight=2)
G.add_edge("Західний район", "Центр", weight=2)
G.add_edge("Західний район", "Індустріальний район", weight=3)
G.add_edge("Пд-Зх район", "Індустріальний район", weight=1)
G.add_edge("Новий Південний район", "Індустріальний район", weight=2)
G.add_edge("Новий Південний район", "Центр", weight=4)
G.add_edge("Південний вїзд", "Центр", weight=6)
G.add_edge("Південний вїзд", "Новий Південний район", weight=4)
G.add_edge("Південний вїзд", "Старий Південний район", weight=3)
G.add_edge("Центр", "Старий Південний район", weight=5)




# Позиції вузлів для візуалізації (довільні координати)
pos = {
    "Північний вїзд": (6000, 6000),
    "Західний вїзд": (1000, 5000),
    "Східний район": (6500, 4500),
    "Західний район": (2000, 4500),
    "Північний район": (4500, 5000),
    "Індустріальний район": (2000, 2500),
    "Центр": (3000,3000),
    "Пд-Зх район": (1000, 2000),
    "Новий Південний район": (2500, 1500),
    "Старий Південний район": (4500, 1500),
    "Південний вїзд": (3000, 500),
}

# Аналіз основних характеристик графа

# Кількість вершин
num_nodes = G.number_of_nodes()
print(f"Кількість вершин: {num_nodes}")

# Кількість ребер
num_edges = G.number_of_edges()
print(f"Кількість ребер: {num_edges}")

# Ступінь кожної вершини
degrees = dict(G.degree())
print("Ступінь вершин:")
for node, degree in degrees.items():
    print(f"   {node}: {degree}")

# Середній ступінь вершин
average_degree = sum(degrees.values()) / num_nodes
print(f"Середній ступінь вершини: {average_degree:.2f}")

# Малюємо граф
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=8, font_weight="bold", edge_color="gray")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Показуємо графік
plt.title("Транспортна мережа міста")
plt.show()


