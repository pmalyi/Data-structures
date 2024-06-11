# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        # inFile = open("input.txt", "r")
        self.n = int(sys.stdin.readline())
        # self.n = int(inFile.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            # [a, b, c] = map(int, inFile.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        # inFile.close()

    def inOrder(self, root, result):
        if root == -1:
            return []
        self.inOrder(self.left[root], result)
        result.append(self.key[root])
        self.inOrder(self.right[root], result)
        # Finish the implementation
        # You may need to add a new recursive method to do that
        return result

    def preOrder(self, root, result):
        if root == -1:
            return []
        result.append(self.key[root])
        self.preOrder(self.left[root], result)
        self.preOrder(self.right[root], result)
        # Finish the implementation
        # You may need to add a new recursive method to do that
        return result

    def postOrder(self, root, result):
        if root == -1:
            return []
        self.postOrder(self.left[root], result)
        self.postOrder(self.right[root], result)
        result.append(self.key[root])
        # Finish the implementation
        # You may need to add a new recursive method to do that
        return result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder(0, [])))
    print(" ".join(str(x) for x in tree.preOrder(0, [])))
    print(" ".join(str(x) for x in tree.postOrder(0, [])))


threading.Thread(target=main).start()
