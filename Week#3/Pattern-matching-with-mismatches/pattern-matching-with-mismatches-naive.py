def find_approximate_matches(k, t, p):
    positions = []
    n = len(p)
    m = len(t)

    for i in range(m - n + 1):
        mismatches = 0
        for j in range(n):
            if t[i + j] != p[j]:
                mismatches += 1
            if mismatches > k:
                break
        if mismatches <= k:
            positions.append(i)

    return positions


def process_input(input_lines):
    results = []
    for line in input_lines:
        k, t, p = line.split()
        k = int(k)
        positions = find_approximate_matches(k, t, p)
        results.append(f"{len(positions)} " + " ".join(map(str, positions)))
    return results


# Sample usage with input reading and processing
if __name__ == "__main__":
    import sys

    # input_lines = sys.stdin.read().strip().split('\n')
    input_lines = sys.stdin.read().strip().split('\n')
    results = process_input(input_lines)
    for result in results:
        print(result)
