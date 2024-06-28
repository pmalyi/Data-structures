# Реалізація бінарного дерева
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
                res_list.append(node)
            node = self.next(node)
        return res_list

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data, end=" ")
        self.show_tree(node.right)

    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    def __del_leaf(self, node, parent):
        if parent.left == node:
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


    # Пошук inorder-спадкоємця
    def minValueNode(self, node):
        current = node
        # Знайдемо крайній лівий лист — він і буде inorder-спадкоємцем
        while (current.left is not None):
            current = current.left

        return current

    # Видалення вузла
    def deleteNode(self, root, key):
        # Повертаємо, якщо дерево порожнє
        if root is None:
            return root

        # Знайдемо вузол, який потрібно видалити
        if key < root.data:
            root.left = self.deleteNode(root.left, key)
        elif (key > root.data):
            root.right = self.deleteNode(root.right, key)
        else:
            # Якщо у вузла тільки один дочірній вузол або взагалі їх немає
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp


            # Якщо у вузла є два дочірніх вузли,
            # поміщаємо центрованого спадкоємця
            # на місце вузла, який потрібно видалити
            temp = self.minValueNode(root.right)

            root.data = temp.data

            # Видаляємо inorder-спадкоємця
            root.right = self.deleteNode(root.right, temp.data)

        return root


v = [10, 5, 7, 16, 13, 2, 20]
# v = [20, 5, 24, 2, 16, 11, 18]
print(*v)
tree = Tree()

for x in v:
    tree.insert(Node(x))

print(tree.root.data)
#t.del_node(5)
tree.show_wide_tree(tree.root)
tree.show_tree(tree.root)
print()

node_found = tree.find_node(2)
if node_found:
    next_node = tree.next(node_found)
    if next_node:
        print(next_node.data)
    else:
        print("next node not exist")
else:
    print("node not found")

range_list = tree.range_search(3, 14)
for node in range_list:
    print(node.data, end=" ")