# python 3
from sys import stdin

class Vertex:
    def __init__(self, key, sum, left, right, parent):
        (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

class SplayTree:
    def __init__(self):
        self.root = None

    def update(self, v):
        if v is None:
            return
        v.sum = v.key + (v.left.sum if v.left is not None else 0) + (v.right.sum if v.right is not None else 0)
        if v.left is not None:
            v.left.parent = v
        if v.right is not None:
            v.right.parent = v

    def smallRotation(self, v):
        parent = v.parent
        if parent is None:
            return
        grandparent = v.parent.parent
        # rotate right
        if parent.left == v:
            m = v.right
            v.right = parent
            parent.left = m
        # rotate left
        else:
            m = v.left
            v.left = parent
            parent.right = m
        self.update(parent)
        self.update(v)
        v.parent = grandparent
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = v
            else:
                grandparent.right = v

    def bigRotation(self, v):
        # zig-zig right: RotateRight 2 times
        if v.parent.left == v and v.parent.parent.left == v.parent:
            self.smallRotation(v.parent)
            self.smallRotation(v)
        # zig-zig left: RotateLeft 2 times
        elif v.parent.right == v and v.parent.parent.right == v.parent:
            self.smallRotation(v.parent)
            self.smallRotation(v)
        # zig-zag: RotateRight
        else:
            self.smallRotation(v)
            self.smallRotation(v)
        # Причина, чому zig і малий поворот розміщуються окремо, полягає в тому, що у випадку zig
        # немає бабусі та дідуся, і якщо велике обертання використовується безпосередньо,
        # буде повідомлено про помилку.


    # Makes splay of the given vertex and makes it the new root.
    def splay(self, v):
        if v is None:
            return None
        while v.parent is not None:
            if v.parent.parent == None:
                self.smallRotation(v)
                break
            self.bigRotation(v)
        return v # останній v.parent = None

    # Шукає заданий ключ у дереві з заданим коренем і після цього викликає splay для найглибшого відвіданого вузла.
    # Повертає пару результату та нового кореня. Якщо значення знайдено, результатом буде вказівник на вузол
    # із заданим ключем.
    # В іншому випадку результатом буде вказівник на вузол із найменшим більшим ключем (наступне значення в порядку).
    # Якщо ключ більший за всі ключі в дереві, тоді результатом буде None.
    def find(self, root, key): # key is int，isn't node
        v = root
        last = root
        next = None
        while v is not None:
            if v.key >= key and (next is None or v.key < next.key):
                next = v
            last = v
            if v.key == key:
                break
            if v.key < key:
                v = v.right
            else:
                v = v.left
        root = self.splay(last)
        if next is not None:
            root = self.splay(next)
        return (next, root)

    def split(self, root, key):
        (result, root) = self.find(root, key)
        # Відповідно до find(), ми знаємо, що результат має бути >= key, тому ми розміщуємо результат у
        # піддереві праворуч, тобто CutLeft()
        if result is None:
            return (root, None)
        right = self.splay(result)
        left = right.left
        right.left = None
        if left is not None:
            left.parent = None
        self.update(left)  # important!!
        self.update(right)  # important!!
        return (left, right)

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left
        # find the smallest node in the right tree, splay the node,
        # (Method 2：node = find(right, -inf), splay(node))
        # then merge left tree and right tree
        while right.left is not None:
            right = right.left
        right = self.splay(right)
        right.left = left
        left.parent = right
        self.update(right)
        return right

    # root = None

    def insert(self, x):
        # global root
        (left, right) = self.split(self.root, x)
        new_vertex = None
        if right is None or right.key != x:
            new_vertex = Vertex(x, x, None, None, None)
        self.root = self.merge(self.merge(left, new_vertex), right)

    def erase(self, x):
        # global root
        (left, middle) = self.split(self.root, x)
        (middle, right) = self.split(middle, x + 1)
        self.root = self.merge(left, right)

    def search(self, x):
        # global root
        (result, self.root) = self.find(self.root, x)
        if result is None or result.key != x:
            return False
        else:
            return True


    def sum(self, fr, to):
        # global root
        (left, middle) = self.split(self.root, fr)
        (middle, right) = self.split(middle, to + 1)
        ans = 0
        if middle is not None:
            ans += middle.sum
        self.root = self.merge(self.merge(left, middle), right)
        return ans


MODULO = 1000000001
# inFile = open("input.txt", "r")
# n_operations = int(inFile.readline())
n_operations = int(stdin.readline())
last_sum_result = 0
spl_tree = SplayTree()
for _ in range(n_operations):
    # line = inFile.readline().split()
    line = stdin.readline().split()
    if line[0] == '+':
        x = int(line[1])
        spl_tree.insert((x + last_sum_result) % MODULO)
    elif line[0] == '-':
        x = int(line[1])
        spl_tree.erase((x + last_sum_result) % MODULO)
    elif line[0] == '?':
        x = int(line[1])
        if spl_tree.search((x + last_sum_result) % MODULO):
            print('Found')
        else:
            print('Not found')
    elif line[0] == 's':
        l = int(line[1])
        r = int(line[2])
        res = spl_tree.sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO