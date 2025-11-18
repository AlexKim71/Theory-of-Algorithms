import heapq

def dijkstra(graph, start_node):
    """
    Реалізація алгоритму Дейкстри для пошуку найкоротших шляхів.

    Args:
        graph (dict): Граф, представлений як словник:
                      {вершина: [(сусід, вага), (сусід, вага), ...]}
        start_node: Початкова вершина.

    Returns:
        tuple: (dist, pred)
               dist (dict): Словник найкоротших відстаней {вершина: відстань}.
               pred (dict): Словник попередників {вершина: попередник}.
    """
    # Ініціалізація
    dist = {node: float('infinity') for node in graph}
    pred = {node: None for node in graph}
    dist[start_node] = 0
    
    # Черга з пріоритетом: (відстань, вершина)
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Якщо ми вже знайшли коротший шлях до цієї вершини,
        # пропускаємо її (це може статися через UpdatePQ, якщо черга додає дублікати)
        if current_distance > dist[current_node]:
            continue
            
        # Перебираємо сусідів поточної вершини
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Релаксація: якщо знайдено коротший шлях
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                pred[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return dist, pred

def reconstruct_path(pred, start_node, end_node):
    """
    Відновлює найкоротший шлях від start_node до end_node.
    """
    path = []
    current = end_node
    
    # Перевірка на недосяжність
    if pred[end_node] is None and end_node != start_node:
        return "Шлях не знайдено"

    while current is not None and current != start_node:
        path.append(current)
        current = pred[current]
    
    if current == start_node: # Додаємо стартову вершину
        path.append(start_node)
        return ' -> '.join(map(str, path[::-1])) # Розвертаємо шлях
    elif end_node == start_node: # Випадок, коли start_node = end_node
        return str(start_node)
    
    return "Шлях не знайдено" # Якщо current став None, але не досяг start_node

# --- Дані для Варіанту 6 ---
# Граф з Вашого зображення (Варіант 6)
# Важливо: оскільки це неорієнтований граф, додаємо ребра в обидва боки
graph_variant_6 = {
    1: [(2, 2), (3, 5), (4, 1), (7, 1)],
    2: [(1, 2), (4, 3), (5, 9)],
    3: [(1, 5), (4, 9), (5, 2), (6, 4), (7, 4), (8, 6)],
    4: [(1, 1), (2, 3), (3, 9), (5, 5), (6, 5)],
    5: [(2, 9), (3, 2), (4, 5), (6, 3)],
    6: [(3, 4), (4, 5), (5, 3), (8, 1)],
    7: [(1, 1), (3, 4), (8, 6)],
    8: [(3, 6), (6, 1), (7, 6)]
}

start_node_variant_6 = 1

# --- Запуск алгоритму Дейкстри ---
distances, predecessors = dijkstra(graph_variant_6, start_node_variant_6)

# --- Виведення результатів ---
print(f"Початкова вершина: {start_node_variant_6}\n")

print("Найкоротші відстані (dist):")
for node, dist_val in sorted(distances.items()):
    print(f"  Вершина {node}: {dist_val}")

print("\nПопередники на найкоротшому шляху (pred):")
for node, pred_node in sorted(predecessors.items()):
    print(f"  Вершина {node}: {pred_node}")

print("\nНайкоротші шляхи:")
for node in sorted(graph_variant_6.keys()):
    if node == start_node_variant_6:
        print(f"  До вершини {node}: {start_node_variant_6} (Відстань: 0)")
    else:
        path_str = reconstruct_path(predecessors, start_node_variant_6, node)
        print(f"  До вершини {node}: {path_str} (Відстань: {distances[node]})")
