from collections import namedtuple
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def left_child_index(i):
    return 2 * i + 1


def right_child_index(i):
    return 2 * i + 2


def sift_down(i, H):
    n = len(H)
    min_index = i
    while i <= (n - 1) // 2:
        l = left_child_index(i)
        if l < n and H[l][1] < H[min_index][1]:
            min_index = l
        elif l < n and H[l][1] == H[min_index][1] and H[l][0] < H[min_index][0]:
            min_index = l
        r = right_child_index(i)
        if r < n and H[r][1] < H[min_index][1]:
            min_index = r
        elif r < n and H[r][1] == H[min_index][1] and H[r][0] < H[min_index][0]:
            min_index = r
        if min_index == i:
            break
        else:
            H[i], H[min_index] = H[min_index], H[i]
            i = min_index


def assign_jobs(n_workers, jobs):
    result = []
    next_free_time = [[i, 0] for i in range(n_workers)]
    for job in jobs:
        next_worker = next_free_time[0][0]
        started_at = next_free_time[0][1]
        result.append(AssignedJob(next_worker, started_at))
        next_free_time[0][1] += job
        sift_down(0, next_free_time)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
