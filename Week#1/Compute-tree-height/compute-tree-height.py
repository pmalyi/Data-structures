def Height(r, tree, n):
    if r not in memo:
        height = 1
        for i in range(n):
            if tree[i] == r and i != r:
                height = max(height, 1 + Height(i, tree, n))
        memo[r] = height
        return height


inf = open('input.txt', 'r')
memo = {}
n = int(input())
#n = int(inf.readline())
tree = tuple(map(int, input().split()))
# tree = tuple(map(int, inf.readline().split()))
root = tree.index(-1)
Height(root, tree, n)
print(memo[root])
# print(memo)
inf.close()
