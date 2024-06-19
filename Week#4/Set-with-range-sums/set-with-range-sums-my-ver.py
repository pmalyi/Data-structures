# Failed case #5/83: time limit exceeded (Time used: 239.98/120.00, memory used: 38612992/2147483648.)
from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = self.parent = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def find_node(self, key):
        node, parent, fl_find = self.__find(self.root, None, key)
        if fl_find:
            return node

    def insert(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        node, parent, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and node:
            obj.parent = node
            if obj.data < node.data:
                node.left = obj
            else:
                node.right = obj

        return obj

    def __del_leaf(self, node, parent):
        if parent is None:
            self.root = None
            node = None
        elif parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None

    def __del_one_child(self, node, parent):
        if parent.left == node:
            if node.left is None:
                parent.left = node.right
            elif node.right is None:
                parent.left = node.left
        elif parent.right == node:
            if node.left is None:
                parent.right = node.right
            elif node.right is None:
                parent.right = node.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def del_node(self, key):
        node, parent, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if node.left is None and node.right is None:
            self.__del_leaf(node, parent)
        elif node.left is None or node.right is None:
            self.__del_one_child(node, parent)
        else:
            sr, pr = self.__find_min(node.right, node)
            node.data = sr.data
            self.__del_one_child(sr, pr)

    def __left_child(self, node):
        if not node.left:
            return node
        return self.__left_child(node.left)

    def __right_parent(self, node):
        if node.parent:
            if node.data < node.parent.data:
                return node.parent
            return self.__right_parent(node.parent)

    def next(self, node):
        if node.right:
            return self.__left_child(node.right)
        return self.__right_parent(node)

    def range_search(self, start, stop):
        res_list = []
        node = self.find_node(start)
        while not node:
            start += 1
            node = self.find_node(start)
        while node.data <= stop:
            if node.data >= start:
                res_list.append(node.data)
            node = self.next(node)
            if not node:
                break
        return res_list

# inFile = open("input.txt", "r")
MODULO = 1000000001
n = int(stdin.readline())
# n = int(inFile.readline())
last_sum_result = 0
tree = Tree()
for i in range(n):
    line = stdin.readline().split()
    # line = inFile.readline().split()
    if line[0] == '+':
        x = int(line[1])
        tree.insert(Node((x + last_sum_result) % MODULO))
    elif line[0] == '-':
        x = int(line[1])
        tree.del_node((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        print("Found" if tree.find_node((x + last_sum_result) % MODULO) else "Not Found")
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        d1 = (l + last_sum_result) % MODULO
        d2 = (r + last_sum_result) % MODULO
        res = sum(tree.range_search(d1, d2))
        print(res)
        last_sum_result = res % MODULO


