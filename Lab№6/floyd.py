import math
import copy

def print_matrix(matrix, title):
    print(f"\n=== {title} ===")
    headers = ["", "1(a)", "2(b)", "3(c)", "4(d)", "5(e)", "6(f)", "7(g)", "8(h)"]
    print(f"{'':>5}", end="")
    for header in headers[1:]: print(f"{header:>6}", end="")
    print()
    vertex_labels = ["1(a)", "2(b)", "3(c)", "4(d)", "5(e)", "6(f)", "7(g)", "8(h)"]
    for i, row in enumerate(matrix):
        print(f"{vertex_labels[i]:>5}", end="")
        for value in row:
            print(f"{'∞' if math.isinf(value) else f'{value:.0f}':>6}", end="")
        print()

def floyd_warshall(matrix):
    n = len(matrix)
    dist = copy.deepcopy(matrix)
    
    print_matrix(dist, "Початкова матриця W")
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != math.inf and dist[k][j] != math.inf:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def main():
    matrix = [
        [0, 2, 5, 1, math.inf, math.inf, 1, math.inf],
        [2, 0, math.inf, 3, 9, math.inf, math.inf, math.inf],
        [5, math.inf, 0, 9, 2, 4, 4, 6],
        [1, 3, 9, 0, 5, 5, math.inf, math.inf],
        [math.inf, 9, 2, 5, 0, 3, math.inf, math.inf],
        [math.inf, math.inf, 4, 5, 3, 0, math.inf, 1],
        [1, math.inf, 4, math.inf, math.inf, math.inf, 0, 6],
        [math.inf, math.inf, 6, math.inf, math.inf, 1, 6, 0]
    ]
    
    print("АЛГОРИТМ ФЛОЙДА-УОРШЕЛЛА")
    result = floyd_warshall(matrix)
    print_matrix(result, "Фінальна матриця D^(8)")
    
    manual = [
        [0, 2, 5, 1, 6, 6, 1, 7],
        [2, 0, 7, 3, 8, 8, 3, 9],
        [5, 7, 0, 6, 2, 4, 4, 5],
        [1, 3, 6, 0, 5, 5, 2, 6],
        [6, 8, 2, 5, 0, 3, 6, 4],
        [6, 8, 4, 5, 3, 0, 7, 1],
        [1, 3, 4, 2, 6, 7, 0, 6],
        [7, 9, 5, 6, 4, 1, 6, 0]
    ]
    
    matches = sum(1 for i in range(8) for j in range(8) 
                  if math.isclose(result[i][j], manual[i][j], rel_tol=1e-10))
    print(f"\n✓ Відповідність: {matches}/64 = {matches*100/64:.1f}%")
    
    print("\nОсновні шляхи:")
    print("3→8: 5 (через 6), 4→8: 6 (через 6), 5→8: 4 (через 6)")
    print("5→7: 6 (через 3), 6→7: 7 (через 4→1)")

if __name__ == "__main__":
    main()
