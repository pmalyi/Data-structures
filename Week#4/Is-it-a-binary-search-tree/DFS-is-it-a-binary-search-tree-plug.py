#!/usr/bin/python3
# Проходить всі тести на Coursera
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c


def inOrder(tree):
    stack = []
    result = []
    curr = 0
    while stack or curr != -1:
        if curr != -1:
            root = tree[curr]
            stack.append(root)
            curr = root.left
        else:
            root = stack.pop()
            result.append(root.key)
            curr = root.right
    return result


def IsBinarySearchTree(tree, n):
    nodes = inOrder(tree)
    for i in range(1, n):
        if nodes[i] <= nodes[i - 1]:
            return False
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
    if n_nodes == 0 or IsBinarySearchTree(nodes, n_nodes):
        print('CORRECT')
    else:
        print('INCORRECT')


threading.Thread(target=main).start()