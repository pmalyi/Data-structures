def height(array):
    depth = {-1: 0}
    while len(depth) <= len(array):
        for child, parent in enumerate(array):
            if parent in depth:
                depth[child] = depth[parent] + 1
    # print(depth)
    return max(depth.values())


n = int(input())
tree = list(map(int, input().split()))
print(height(tree))
