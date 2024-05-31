# з хешуванням. не проходить всі тести: Failed case #6/7: time limit exceeded (Time used: 45.35/40.00, memory used: 33202176/536870912.)
def compute_hashes(s, base=263, mod=10 ** 9 + 7):
    n = len(s)
    hash_tab = [0] * (n + 1)
    for i in range(n):
        hash_tab[i + 1] = (hash_tab[i] * base + ord(s[i])) % mod
    return hash_tab


def compute_powers(s, base=263, mod=10 ** 9 + 7):
    n = len(s)
    s_powers = [1] * (n + 1)
    for i in range(n):
        s_powers[i + 1] = (s_powers[i] * base) % mod
    return s_powers


def get_substring_hash(s_hash_tab, s_powers, start, end, mod=10 ** 9 + 7):
    length = end - start
    hash_value = (s_hash_tab[end] - s_hash_tab[start] * s_powers[length] % mod + mod) % mod
    return hash_value


def mismatch_count(t_hash_tab, p_hash_tab, powers_tab, low, high, res, k):
    t_hash_value = get_substring_hash(t_hash_tab, powers_tab, low, high)
    p_hash_value = get_substring_hash(p_hash_tab, powers_tab, low, high)
    if high - low == 1 and t_hash_value != p_hash_value:
        res[0] += 1

    if res[0] > k or t_hash_value == p_hash_value or high - low == 1:
        return

    mid = (low + high) // 2
    mismatch_count(t_hash_tab, p_hash_tab, powers_tab, low, mid, res, k)
    mismatch_count(t_hash_tab, p_hash_tab, powers_tab, mid, high, res, k)
    return


def find_approximate_matches(t, p, k):
    len_t, len_p = len(t), len(p)
    if len_t < len_p:
        return []

    result = []
    t_hash_tab = compute_hashes(t)
    p_hash_tab = compute_hashes(p)
    powers_tab = compute_powers(t)
    for i in range(len_t - len_p + 1):
        count_mis = [0,]
        mismatch_count(t_hash_tab[i:i + len_p + 1], p_hash_tab, powers_tab, 0, len_p, count_mis, k)
        if count_mis[0] <= k:
            result.append(i)
    return result


def process_input(input_lines):
    results = []
    for line in input_lines:
        k, text, pattern = line.split()
        k = int(k)
        positions = find_approximate_matches(text, pattern, k)
        results.append(f"{len(positions)} " + " ".join(map(str, positions)))
    return results



if __name__ == "__main__":
    #import sys
    #input_lines = sys.stdin.read().strip().split('\n')
    filein = open("cours_input.txt", "r")
    # filein = open("test_input.txt", "r")
    fileout = open("my_output-2.txt", "w")
    input_lines = filein.read().strip().split('\n')
    results = process_input(input_lines)
    for result in results:
        #print(result)
        print(result, file=fileout)

    # filein.close()
    # fileout.close()