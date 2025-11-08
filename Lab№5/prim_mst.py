# ---------------------------------------------------------------------
# КОД АЛГОРИТМУ ПРИМА (На основі C++ структури)
# ---------------------------------------------------------------------

import sys
import copy

# 4. #define INF 9999999
INF = sys.maxsize
# 5. // number of vertices in graph
# 6. #define V 8 (для Вашого графа)
V = 8

# 7. // create a 2d array of size V x V
# 8. // for adjacency matrix to represent graph
# 9. int G[V][V] = {
#    Ваша матриця суміжності (Варіант 6, вершини 1-8)
#    Індекси 0-7 відповідають вершинам 1-8
G = [
    [0, 2, 5, 3, INF, INF, 1, INF],     # 0 (вершина 1)
    [2, 0, INF, 3, 9, INF, INF, INF],   # 1 (вершина 2)
    [5, INF, 0, 5, 2, 4, 4, 6],         # 2 (вершина 3)
    [3, 3, 5, 0, 9, 5, INF, INF],       # 3 (вершина 4)
    [INF, 9, 2, 9, 0, 3, INF, 2],       # 4 (вершина 5)
    [INF, INF, 4, 5, 3, 0, 1, 1],       # 5 (вершина 6)
    [1, INF, 4, INF, INF, 1, 0, 1],     # 6 (вершина 7)
    [INF, INF, 6, INF, 2, 1, 1, 0]      # 7 (вершина 8)
]
# 16. };

def prim_mst(graph):
    # 18. int no_edge; // number of edge
    no_edge = 0
    
    # 19. // create a array to track selected vertex
    # 20. // selected will become true otherwise false
    # 21. int selected[V];
    selected = [False] * V
    
    # 24. // set number of edge to 0
    # 25. no_edge = 0; (вже зроблено вище)

    # 29. // choose 0th vertex and make it true
    # 30. selected[0] = true;
    selected[0] = True
    
    print("\nЗапустивши наведений вище код, ми отримаємо виведення у вигляді:")
    # 34. cout << "Edge" << " : " << "Weight" << endl;
    print("Edge : Weight")
    
    # 35. cout << endl;
    print()
    
    # 35. while (no_edge < V - 1) {
    while no_edge < V - 1:
        
        # 41. int min = INF;
        min_weight = INF
        
        # 42. int x = 0;
        u_row = 0
        # 43. int y = 0;
        v_col = 0
        
        # 44. for (int i = 0; i < V; i++) {
        for i in range(V):
            # 45. if (selected[i]) {
            if selected[i]:
                # 46. for (int j = 0; j < V; j++) {
                for j in range(V):
                    # 47. if (!selected[j] && G[i][j]) { 
                    # // not in selected and there is an edge
                    if not selected[j] and graph[i][j] != INF:
                        # 48. if (min > G[i][j]) {
                        if min_weight > graph[i][j]:
                            # 49. min = G[i][j];
                            min_weight = graph[i][j]
                            # 50. x = i;
                            u_row = i
                            # 51. y = j;
                            v_col = j
                        # 52. }
                    # 53. }
                # 54. }
            # 55. }
        # 56. }
        
        # 57. cout << x << " - " << y << " : " << G[x][y] << endl;
        # Виведення у нумерації 1-8 (додаємо 1 до індексів)
        print(f"{u_row + 1} - {v_col + 1} : {min_weight}")
        
        # 59. selected[y] = true;
        selected[v_col] = True
        
        # 60. no_edge++;
        no_edge += 1
        
    # 62. return 0;

# ---------------------------------------------------------------------
# ВИКОНАННЯ
# ---------------------------------------------------------------------

if __name__ == "__main__":
    prim_mst(G)
