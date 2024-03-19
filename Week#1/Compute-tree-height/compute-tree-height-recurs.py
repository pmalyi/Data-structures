# Не проходить тести через перевищення глибини рекурсії
def Height(r, tree, n):
    height = 1
    for i in range(n):
        if tree[i] == r and i != r:
            height = max(height, 1 + Height(i, tree, n))
    return height


inf = open('input.txt', 'r')
n = int(input())
#n = int(inf.readline())
tree = tuple(map(int, input().split()))
# tree = tuple(map(int, inf.readline().split()))
root = tree.index(-1)
Height(root, tree, n)
print(Height(root))
# print(memo)
inf.close()
