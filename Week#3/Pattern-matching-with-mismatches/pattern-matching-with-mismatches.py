# не проходить всі тести

def compute_hashes_and_powers(s, base, mod):
    n = len(s)
    h = [0] * (n + 1)
    p_powers = [1] * (n + 1)

    for i in range(n):
        h[i + 1] = (h[i] * base + ord(s[i])) % mod
        p_powers[i + 1] = (p_powers[i] * base) % mod

    return h, p_powers


def get_substring_hash(h, p_powers, start, length, mod):
    end = start + length
    hash_value = (h[end] - h[start] * p_powers[length] % mod + mod) % mod
    return hash_value


def find_approximate_matches(k, t, p):
    m, n = len(t), len(p)
    if m < n:
        return []

    base = 257
    mod = 10 ** 9 + 7

    t_hashes, t_powers = compute_hashes_and_powers(t, base, mod)
    p_hashes, p_powers = compute_hashes_and_powers(p, base, mod)
    p_hash = get_substring_hash(p_hashes, p_powers, 0, n, mod)

    def mismatch_count(start):
        low, high = 0, n
        mismatches = 0
        max_low = 0

        while low < high and mismatches <= k:
            mid = (low + high) // 2
            t_hash = get_substring_hash(t_hashes, t_powers, start, mid, mod)
            p_sub_hash = get_substring_hash(p_hashes, p_powers, 0, mid, mod)
            if t_hash == p_sub_hash:
                low = mid + 1
                if low >= max_low:
                    max_low = low
            else:
                high = mid
                mismatches += 1

        if mismatches > k:
            return float('inf')

        for i in range(max_low, n):
            if t[start + i] != p[i]:
                mismatches += 1
                if mismatches > k:
                    break

        return mismatches

    result = []
    for i in range(m - n + 1):
        if mismatch_count(i) <= k:
            result.append(i)

    return result


def process_input(input_lines):
    results = []
    for line in input_lines:
        k, t, p = line.split()
        k = int(k)
        positions = find_approximate_matches(k, t, p)
        results.append(f"{len(positions)} " + " ".join(map(str, positions)))
    return results



if __name__ == "__main__":
    import sys
    #input_lines = sys.stdin.read().strip().split('\n')
    filein = open("cours_input.txt", "r")
    fileout = open("my_output-2.txt", "w")
    input_lines = filein.read().strip().split('\n')
    results = process_input(input_lines)
    for result in results:
        print(result, file=fileout)

    filein.close()
    fileout.close()
