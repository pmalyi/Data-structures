import sys

def PolyHash(s, prime, multiplier):
    hash_value = 0
    for i in range(len(s) - 1, -1, -1):
        hash_value = (hash_value * multiplier + ord(s[i])) % prime
    return hash_value


def HashTable(s, p_len, prime, multiplier):
    H = [0] * (len(s) - p_len + 1)
    substring = s[len(s) - p_len:]
    H[len(s) - p_len] = PolyHash(substring, prime, multiplier)
    y = pow(multiplier, p_len, prime)
    for i in range(len(s) - p_len - 1, - 1, - 1):
        H[i] = (multiplier * H[i + 1] + ord(s[i]) - y * ord(s[i + p_len])) % prime
    return H


def HashDict(s, p_len, prime, multiplier):
    D = {}
    substring = s[len(s) - p_len:]
    last = PolyHash(substring, prime, multiplier)
    D[last] = len(s) - p_len
    y = pow(multiplier, p_len, prime)
    for j in range(len(s) - p_len - 1, - 1, - 1):
        current = (multiplier * last + ord(s[j]) - y * ord(s[j + p_len])) % prime
        D[current] = j
        last = current
    return D


def SearchSubstring(hash_dict, hash_table):
    check = False
    matches = {}
    for i in range(len(hash_table)):
        a_start = hash_dict.get(hash_table[i], -1)
        if a_start != -1:
            check = True
            matches[i] = a_start
    return check, matches


def MaxLength(string_a, string_b, low, high, max_length, aStart, bStart):
    # a is long string --> hash table, b is short string --> hash dict
    mid = (low + high) // 2  # mid is the length of the tested common substring
    if low > high:
        return aStart, bStart, max_length
    prime1 = 1000000007
    prime2 = 1000004249
    x = 263

    aHash1 = HashDict(string_a, mid, prime1, x)
    aHash2 = HashDict(string_a, mid, prime2, x)
    bHash1 = HashTable(string_b, mid, prime1, x)
    bHash2 = HashTable(string_b, mid, prime2, x)

    check1, matches1 = SearchSubstring(aHash1, bHash1)
    check2, matches2 = SearchSubstring(aHash2, bHash2)
    if check1 and check2:
        for a, b in matches1.items():
            temp = matches2.get(a, -1)
            if temp != -1:
                max_length = mid
                aStart, bStart = a, b
                del aHash1, aHash2, bHash1, bHash2, matches1, matches2
                return MaxLength(string_a, string_b, mid + 1, high, max_length, aStart, bStart)

    return MaxLength(string_a, string_b, low, mid - 1, max_length, aStart, bStart)


for line in sys.stdin.readlines():
    s, t = line.split()

    k = min(len(s), len(t))

    if len(s) <= len(t):
        short_string, long_string = s, t
    else:
        short_string, long_string = t, s

    i, j, l = MaxLength(long_string, short_string, 0, k, 0, 0, 0)
    if len(s) <= len(t):
        print(i, j, l)
    else:
        print(j, i, l)
