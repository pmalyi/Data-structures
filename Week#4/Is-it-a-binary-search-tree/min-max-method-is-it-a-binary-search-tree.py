#!/usr/bin/python3
# Проходить всі тести на Coursera
import sys, threading
from math import inf

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c


def IsBinarySearchTreeBFS(tree):
    stack = []
    stack.append((float('-inf'), tree[0], float('inf')))
    while stack:
        min, root, max = stack.pop()
        if root.key < min or root.key > max:
            return False
        if root.left != -1:
            stack.append((min, tree[root.left], root.key))
        if root.right != -1:
            stack.append((root.key, tree[root.right], max))
    return True


def main():
    # inFile = open("input.txt", "r")
    # n_nodes = int(inFile.readline())
    n_nodes = int(input())
    nodes = []
    for i in range(n_nodes):
        a, b, c = map(int, input().split())
        # a, b, c = map(int, inFile.readline().split())
        node = Node(a, b, c)
        nodes.append(node)
    if n_nodes == 0 or IsBinarySearchTreeBFS(nodes):
        print('CORRECT')
    else:
        print('INCORRECT')


threading.Thread(target=main).start()