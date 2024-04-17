class DisjoinSet:
    def __init__(self, n_var):
        self.n_var = n_var
        self._ranks = [0] * n_var
        self._parents = list(range(n_var))

    def find(self, i):
        while i != self._parents[i]:
            i = self._parents[i]
        return i

    def union(self, i, j):
        id_i = self.find(i)
        id_j = self.find(j)

        if id_i == id_j:
            return False

        if self._ranks[id_i] > self._ranks[id_j]:
            self._parents[id_j] = id_i
        else:
            self._parents[id_i] = id_j
            if self._ranks[id_i] == self._ranks[id_j]:
                self._ranks[id_j] += 1

        return True

def main():
    n_var, equal, not_equal = map(int, input().split())
    ds_set = DisjoinSet(n_var)
    for _ in range(equal):
        a, b = map(int, input().split())
        ds_set.union(a - 1, b - 1)

    fail = False
    for _ in range(not_equal):
        a, b = map(int, input().split())
        if ds_set.find(a - 1) == ds_set.find(b - 1):
            fail = True
    if fail:
        return 0
    return 1


if __name__ == "__main__":
    print(main())
