# python3

import sys
from collections import deque


def HashTable(s, prime, x):
    hash_table = list([] for _ in range(len(s) + 1))
    hash_table[0] = 0
    for i in range(1, len(s) + 1):
        hash_table[i] = (hash_table[i - 1] * x + ord(s[i - 1])) % prime
    return hash_table


def HashValue(hash_table, prime, x, start, length):
    y = pow(x, length, prime)
    hash_value = (hash_table[start + length] - y * hash_table[start]) % prime
    return hash_value


def PreCompute(text, pattern):
    global m, x
    h1 = HashTable(text, m, x)
    h2 = HashTable(pattern, m, x)
    return h1, h2


def CheckMatch(a_start, half_p_len, p_len, k):
    global m, h1, h2
    stack = deque()
    stack.append((a_start, 0, half_p_len, 1))
    stack.append((a_start + half_p_len, half_p_len, p_len - half_p_len, 1))
    count = 0
    temp = 2
    C = 0
    while stack:
        a, b, L, n = stack.popleft()
        u1 = HashValue(h1, m, x, a, L)
        v1 = HashValue(h2, m, x, b, L)
        if temp != n:
            count = C
        if u1 != v1:
            count += 1
            if L > 1:
                stack.append((a, b, L//2, n+1))
                stack.append((a + L//2, b + L//2, L - L//2, n+1))
            else:
                C += 1
        if count > k:
            return False
        temp = n
    if count > k:
        return False
    else:
        return True


def Solve(text, pattern, k):
    global h1, h2
    h1, h2 = PreCompute(text, pattern)
    pos = []
    for i in range(len(text) - len(pattern) + 1):
        if CheckMatch(i, len(pattern) // 2, len(pattern), k):
            pos.append(i)
    return pos


m = 1000000007
x = 263

for line in sys.stdin.readlines():
    k, t, p = line.split()
    results = Solve(t, p, int(k))
    print(len(results), *results)