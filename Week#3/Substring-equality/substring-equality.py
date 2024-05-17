# python3

import sys


class Solver:
	m1 = 10 ** 9 + 7
	m2 = 10 ** 9 + 9
	x = 263
	def __init__(self, s):
		self.s = s
		self.H1 = self._hash_array(self.m1)
		self.H2 = self._hash_array(self.m2)

	def _hash_array(self, m):
		n = len(self.s)
		H = [0] * (n + 1)
		for i in range(1, n + 1):
			H[i] = (self.x * H[i - 1] + ord(self.s[i - 1])) % m
		return H

	@staticmethod
	def _hash_value(array, m, x, start, length):
		y = pow(x, length, m)
		value = (array[start + length] - y * array[start]) % m
		return value

	def ask(self, a, b, l):
		s1a = self._hash_value(self.H1, self.m1, self.x, a, l)
		s1b = self._hash_value(self.H1, self.m1, self.x, b, l)
		s2a = self._hash_value(self.H2, self.m2, self.x, a, l)
		s2b = self._hash_value(self.H2, self.m2, self.x, b, l)
		return s1a == s1b and s2a == s2b


s = sys.stdin.readline()
q = int(sys.stdin.readline())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, sys.stdin.readline().split())
	print("Yes" if solver.ask(a, b, l) else "No")
