# Не проходить тести через перевищення Timelimits

def Height(array):
    depth = {-1: 0}
    visited = set()
    while len(depth) <= len(array):
        for child, parent in enumerate(array):
            if parent in depth and child not in visited:
                depth[child] = depth[parent] + 1
                visited.add(child)

    print(depth)
    return max(depth.values())


#n = 9
#tree = 4, -1, 4, 1, 1, 0, 2, 0, 2
n = int(input())
tree = list(map(int, input().split()))
print(Height(tree))
