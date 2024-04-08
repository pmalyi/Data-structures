from collections import namedtuple
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Heap:
    def __init__(self, n_workers, jobs):
        self.n = n_workers
        self.jobs = jobs
        self._next_free_time = [[i, 0] for i in range(n_workers)]
        self.result = []

    @staticmethod
    def _left_child_index(i):
        return 2 * i + 1

    @staticmethod
    def _right_child_index(i):
        return 2 * i + 2

    def _sift_down(self, i):
        n = len(self._next_free_time)
        min_index = i
        while i <= (n - 1) // 2:
            l = self._left_child_index(i)
            if l < n and self._next_free_time[l][1] < self._next_free_time[min_index][1]:
                min_index = l
            elif l < n and self._next_free_time[l][1] == self._next_free_time[min_index][1] and \
                    self._next_free_time[l][0] < self._next_free_time[min_index][0]:
                min_index = l
            r = self._right_child_index(i)
            if r < n and self._next_free_time[r][1] < self._next_free_time[min_index][1]:
                min_index = r
            elif r < n and self._next_free_time[r][1] == self._next_free_time[min_index][1] and \
                    self._next_free_time[r][0] < self._next_free_time[min_index][0]:
                min_index = r
            if min_index == i:
                break
            else:
                self._next_free_time[i], self._next_free_time[min_index] = \
                    self._next_free_time[min_index], self._next_free_time[i]
                i = min_index

    def assign_jobs(self, jobs):
        for job in jobs:
            next_worker = self._next_free_time[0][0]
            started_at = self._next_free_time[0][1]
            self.result.append(AssignedJob(next_worker, started_at))
            self._next_free_time[0][1] += job
            self._sift_down(0)
        return self.result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs
    heap = Heap(n_workers, jobs)
    assigned_jobs = heap.assign_jobs(jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
