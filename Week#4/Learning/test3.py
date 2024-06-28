# не зовсім вдала спроба реалізації
class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = None if left == -1 else left
        self.right = None if right == -1 else right


class AVLTreeOprs:
    def __init__(self):
        self.num_nodes, self.nodes_arr = self.read_nodes()
        self.tree = self.__create_tree()
        self.root = self.get_root()

    @staticmethod
    def read_nodes():
        nodes_arr = []
        with open("input.txt", "r") as infile:
            num_nodes = int(infile.readline())
            for _ in range(num_nodes):
                node = tuple(map(int, infile.readline().split()))
                nodes_arr.append(node)
        return num_nodes, nodes_arr

    def __create_tree(self):
        tree = []
        for i in range(self.num_nodes):
            key, left, right = self.nodes_arr[i]
            node = Node(key, left, right)
            node.left = Node(*self.nodes_arr[left])
            node.right = Node(*self.nodes_arr[right])
            tree.append(node)
        return tree

    def get_root(self):
        return self.tree[0]

    def find_node(self, key, root):
        if root.left.key == -1 or root.right.key == -1:
            return -1
        if root.key == key:
            return root.key
        if root.key > key:
            return self.find_node(key, root.left)
        if root.key < key:
            return self.find_node(key, root.right)

    def print_tree(self):
        for node in self.tree:
            print(node.key, node.left, node.right)


oprs = AVLTreeOprs()
oprs.print_tree()
root = oprs.root
print(root.left.key, root.right.key)
print(oprs.find_node(5, root))
