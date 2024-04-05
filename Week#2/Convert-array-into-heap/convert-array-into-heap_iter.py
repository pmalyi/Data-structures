def left_child_index(i):
    return 2 * i + 1


def right_child_index(i):
    return 2 * i + 2


def sift_down(curr, H, n, swaps):
    max_index = curr
    while curr <= (n - 1) // 2:
        l = left_child_index(curr)
        if l < n and H[l] < H[max_index]:
            max_index = l
        r = right_child_index(curr)
        if r < n and H[r] < H[max_index]:
            max_index = r
        if max_index == curr:
            break
        else:
            H[curr], H[max_index] = H[max_index], H[curr]
            swaps.append((curr, max_index))
            curr = max_index


def build_heap(data, n):
    swaps = []
    for i in range((n - 1) // 2, -1, -1):
        sift_down(i, data, n, swaps)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data, n)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
