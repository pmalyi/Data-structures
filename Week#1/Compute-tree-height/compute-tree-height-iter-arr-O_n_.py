# Рішення пройшло тести
def compute_height(n, parents):
    T = [0] * n # список (масив) висот
    root = parents.index(-1)
    T[root] = 1
    for vertex in range(n): # vertex - вершина дерева
        height = 0 # висота
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
            if T[current]:
                T[vertex] = T[current] + height
                break
    return max(T)


n = int(input())
parents = list(map(int, input().split()))
print(compute_height(n, parents))
