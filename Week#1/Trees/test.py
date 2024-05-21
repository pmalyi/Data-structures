# print tree
def compute_height(n, parents):
    T = {}
    root = parents.index(-1)
    T[root] = 1
    for vertex in range(n):
        height = 0
        current = vertex
        while current != -1:
            height += 1
            current = parents[current]
            if current in T:
                T[vertex] = T.get(current, 0) + height
                break
    return max(T.values())


#n = 9
#parents = 4, -1, 4, 1, 1, 0, 2, 0, 2
n = int(input())
parents = list(map(int, input().split()))
print(compute_height(n, parents))
