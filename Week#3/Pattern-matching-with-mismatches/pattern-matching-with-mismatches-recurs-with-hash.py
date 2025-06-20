# з хешуванням.
# проходить всі тести
def compute_hashes(s, mod, base=263):
    n = len(s)
    hash_tab = [0] * (n + 1)
    for i in range(n):
        hash_tab[i + 1] = (hash_tab[i] * base + ord(s[i])) % mod
    return hash_tab


def compute_powers(s, mod, base=263):
    n = len(s)
    s_powers = [1] * (n + 1)
    for i in range(n):
        s_powers[i + 1] = (s_powers[i] * base) % mod
    return s_powers


def get_substring_hash(s_hash_tab, s_powers, start, end, mod=10 ** 9 + 7):
    length = end - start
    hash_value = (s_hash_tab[end] - s_hash_tab[start] * s_powers[length]) % mod
    return hash_value


def mismatch_count(t_hash_tab, p_hash_tab, powers_tab, low_t, high_t, low_p, high_p, res, k):
    t_hash_value = get_substring_hash(t_hash_tab, powers_tab, low_t, high_t)
    p_hash_value = get_substring_hash(p_hash_tab, powers_tab, low_p, high_p)
    len_sub_str = high_t - low_t
    if len_sub_str == 1 and t_hash_value != p_hash_value:
        res[0] += 1

    if res[0] > k or t_hash_value == p_hash_value or len_sub_str < 2:
        return

    t_mid_hash_tab = (low_t + high_t) // 2
    p_mid_hash_tab = (low_p + high_p) // 2
    mismatch_count(t_hash_tab, p_hash_tab, powers_tab, low_t, t_mid_hash_tab, low_p, p_mid_hash_tab, res, k)
    mismatch_count(t_hash_tab, p_hash_tab, powers_tab, t_mid_hash_tab, high_t, p_mid_hash_tab, high_p, res, k)
    return


def find_approximate_matches(t, p, k):
    len_t, len_p = len(t), len(p)
    if len_t < len_p:
        return []

    result = []
    mod = 10 ** 9 + 7
    t_hash_tab = compute_hashes(t, mod)
    p_hash_tab = compute_hashes(p, mod)
    powers_tab = compute_powers(p, mod)
    len_t_hash_tab = len(t_hash_tab)
    len_p_hash_tab = len(p_hash_tab)
    for i in range(len_t_hash_tab - len_p_hash_tab + 1):
        count_mis = [0,]
        mismatch_count(t_hash_tab, p_hash_tab, powers_tab, i, i + len_p, 0, len_p, count_mis, k)
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
    import sys
    input_lines = sys.stdin.read().strip().split('\n')
    results = process_input(input_lines)
    for result in results:
        print(result)
