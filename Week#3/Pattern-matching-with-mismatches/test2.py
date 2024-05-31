def compute_hashes_and_powers(s, base=257, mod=10 ** 9 + 7):
    n = len(s)
    hash_tab = [0] * (n + 1)
    s_powers = [1] * (n + 1)
    for i in range(n):
        hash_tab[i + 1] = (hash_tab[i] * base + ord(s[i])) % mod
        s_powers[i + 1] = (s_powers[i] * base) % mod

    return hash_tab, s_powers


def get_substring_hash(s_hash_tab, s_powers, start, end, mod=10 ** 9 + 7):
    length = end - start
    hash_value = (s_hash_tab[end] - s_hash_tab[start] * s_powers[length] % mod + mod) % mod
    return hash_value


def mismatch_count(t_hash_tab, t_powers, p_hash_tab, p_powers, low, high, res, k):
    t_hash_value = get_substring_hash(t_hash_tab, t_powers, low, high)
    p_hash_value = get_substring_hash(p_hash_tab, p_powers, low, high)
    if high - low == 1 and t_hash_value != p_hash_value:
        res[0] += 1
    if res[0] > k or t_hash_value == p_hash_value or high - low == 1:
        return

    mid = (low + high) // 2
    mismatch_count(t_hash_tab, t_powers, p_hash_tab, p_powers, low, mid, res, k)
    mismatch_count(t_hash_tab, t_powers, p_hash_tab, p_powers, mid, high, res, k)
    return


text =    "caba8abaata"
pattern = "daab7abaaya"
n = len(pattern)
k = 2
res = [0,]
t_hash_tab, t_powers = compute_hashes_and_powers(text)
p_hash_tab, p_powers = compute_hashes_and_powers(pattern)
low = 0
high = n
mismatch_count(t_hash_tab, t_powers, p_hash_tab, p_powers, low, high, res, k)
print(res)
print(t_powers, p_powers, sep="\n")

