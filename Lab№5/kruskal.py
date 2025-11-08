# ---------------------------------------------------------------------
# КОД АЛГОРИТМУ КРУСКАЛА (На основі C++ структури)
# ---------------------------------------------------------------------

class Graph:
    # 7. class Graph {
    
    # 8-11. private: G, T, parent, V
    
    def __init__(self, V):
        self.V = V
        self.G = []  # Список ребер у форматі (вага, u, v)
        self.T = []  # Ребра MST
        
        # 21-23. Ініціалізація parent
        self.parent = list(range(V)) 
        
    # 14. void AddWeightedEdge(int u, int v, int w);
    def AddWeightedEdge(self, u, v, w):
        # Додавання ребра у форматі (вага, u, v)
        self.G.append((w, u, v)) 

    # 15. int find_set(int i);
    def find_set(self, i):
        # 33-34. if (i == parent[i]) return i; 
        if i == self.parent[i]:
            return i
        
        # 40. Рекурсивний виклик зі стисненням шляху
        self.parent[i] = self.find_set(self.parent[i])
        return self.parent[i]

    # 16. void union_set(int u, int v);
    def union_set(self, u, v):
        u_rep = self.find_set(u)
        v_rep = self.find_set(v)
        
        if u_rep != v_rep:
            # 44. parent[u_rep] = v_rep; 
            self.parent[u_rep] = v_rep
            return True
        return False
        
    # 17. void kruskal();
    def kruskal(self):
        # 46. sort(G.begin(), G.end()); // increasing weight
        self.G.sort(key=lambda item: item[0])
        
        # 47. for (i = 0; i < G.size(); i++) {
        for weight, u, v in self.G:
            # 49-50. Знайти представників множин
            u_rep = self.find_set(u)
            v_rep = self.find_set(v)
            
            # 51. if (uRep != vRep) {
            if u_rep != v_rep:
                # 52. T.push_back(G[i]); // add to tree
                self.T.append((weight, (u, v))) 
                
                # 53. union_set(uRep, vRep);
                self.union_set(u, v)

    # 18. void print();
    def print_mst(self):
        total_weight = sum(w for w, (u, v) in self.T)
        
        print("Edge : Weight")
        
        # 58. for (int i = 0; i < T.size(); i++) {
        for weight, (u, v) in self.T:
            # 60. Виведення у нумерації 1-8
            print(f"{u + 1} - {v + 1} : {weight}")

        print(f"\nЗагальна вартість MST: {total_weight}")

# ---------------------------------------------------------------------
# 64. int main() { / БЛОК ВИКОНАННЯ
# ---------------------------------------------------------------------
if __name__ == "__main__":
    
    # 65. Graph g(8); // V=8 для Вашого графа
    V_COUNT = 8
    g = Graph(V_COUNT)
    
    # Ребра графа Варіанта 6 (1-8, вага)
    # Ми переводимо нумерацію 1-8 в індекси 0-7 при додаванні
    edges = [
        (1, 7, 1), (7, 6, 1), (6, 8, 1), 
        (1, 2, 2), (5, 3, 2), (8, 5, 2), 
        (1, 4, 3), (2, 4, 3), (5, 6, 3), 
        (3, 6, 4), (7, 3, 4), 
        (1, 3, 5), (4, 6, 5), 
        (3, 8, 6), 
        (2, 5, 9), (4, 5, 9)
    ]
    
    # Додаємо ребра, переводячи нумерацію 1-8 в індекси 0-7
    for u, v, w in edges:
        g.AddWeightedEdge(u - 1, v - 1, w)
    
    print("--- АЛГОРИТМ КРУСКАЛА (Варіант 6) ---")
    
    # 89. g.kruskal();
    g.kruskal()
    
    # 90. g.print();
    g.print_mst()
