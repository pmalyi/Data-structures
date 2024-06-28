# не зовсім вдала спроба реалізації
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = None if left == -1 else left
        self.right = None if right == -1 else right


class Tree:
    def __init__(self, tree_arr):
        self.tree_arr = tree_arr
        self.root = self.append(self.tree_arr[0])



    def append(self, obj):
        key = obj[0]
        left = None if obj[1] == -1 else obj[1]
        right = None if obj[2] == -1 else obj[2]
        return Node(key, left, right)

    def build_tree(self):
        self.obj_arr = []
        for obj in self.tree_arr:
            self.obj_arr.append(self.append(obj))
        return self.obj_arr

    def inOrder(self, root, result):
        if not root:
            return []
        self.inOrder(self.root.left, result)
        result.append(self.root.key)
        self.inOrder(self.root.right, result)
        # Finish the implementation
        # You may need to add a new recursive method to do that
        return result



    '''def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.key, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn'''


tree_arr = [(4, 1, 2), (2, 3, 4), (6, 5, 6), (1, -1, -1), (3, -1, -1), (5, -1, -1), (7, -1, -1)]
# tree_arr = [(0, 7, 2), (10, -1, -1), (20, -1, 6), (30, 8, 9), (40, 3, -1), (50, -1, -1), (60, 1, -1), (70, 5, 4), (80, -1, -1), (90, -1, -1)]
# infile = open("input.txt", "r")
# n = int(infile.readline())
n = 7
tree = Tree(tree_arr)
obj_arr = tree.build_tree()
print(tree.inOrder(tree.root, []))
