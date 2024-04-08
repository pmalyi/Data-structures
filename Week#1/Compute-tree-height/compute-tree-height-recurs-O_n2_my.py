# Не проходить тести через перевищення глибини рекурсії
def Height(r, tree, n):
    height = 1
    for i in range(n):
        if tree[i] == r and i != r:
            height = max(height, 1 + Height(i, tree, n))
    return height


n = int(input())
tree = tuple(map(int, input().split()))
root = tree.index(-1)
Height(root, tree, n)
print(Height(root, tree, n))


