#не проходить всі тести на Coursers але проходить всі тести на Stepik
# ймовірна причина непроходження всіх тестів - перевищення ліміту глибини рекурсії

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Tree:

    def read(self):
        # inFile = open("input.txt", "r")
        self.n = int(sys.stdin.readline())
        # self.n = int(inFile.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            # a, b, c = map(int, inFile.readline().split())
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
        return result

    def IsBinarySearchTree(self):
        if self.n == 0:
            return True
        nodes = self.inOrder(0, [])
        for i in range(1, self.n):
            if nodes[i] <= nodes[i - 1]:
                return False
        return True


def main():
    tree = Tree()
    tree.read()
    if tree.IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
