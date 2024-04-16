class Database:
    def __init__(self, row_counts):
        self._row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self._ranks = [1] * n_tables
        self._parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self._get_parent(src)
        dst_parent = self._get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        if self._ranks[src_parent] > self._ranks[dst_parent]:
            self._parents[dst_parent] = src_parent
            self._row_counts[src_parent] += self._row_counts[dst_parent]
            self._row_counts[dst_parent] = 0
            self.max_row_count = max(self.max_row_count, self._row_counts[src_parent])
        else:
            self._parents[src_parent] = dst_parent
            self._row_counts[dst_parent] += self._row_counts[src_parent]
            self._row_counts[src_parent] = 0
            self.max_row_count = max(self.max_row_count, self._row_counts[dst_parent])
            if self._ranks[src_parent] == self._ranks[dst_parent]:
                self._ranks[dst_parent] += 1

        return True

    def _get_parent(self, table):
        # find parent and compress path
        if table != self._parents[table]:
            # table = self.parents[table]
            self._parents[table] = self._get_parent(self._parents[table])
        return self._parents[table]


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
