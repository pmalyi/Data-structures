# Рішення пройшло тести
def compute_height(n, parents):
    T = {} # словник висот
    root = parents.index(-1)
    T[root] = 1
    max_height = 0
    for vertex in range(n): # vertex - вершина дерева
        height = 0 # висота
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
            if current in T:
                T[vertex] = T.get(current, 0) + height
                if T[vertex] > max_height:
                    max_height = T[vertex]
                break
    return max_height


n = int(input())
parents = list(map(int, input().split()))
print(compute_height(n, parents))
