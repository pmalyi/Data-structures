# python3
# inF = open("06", "r")
# outF = open("06.a", "w")


def read_input():
    return (input().rstrip(), input().rstrip())
    # return (inF.readline().rstrip(), inF.readline().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))
    # print(' '.join(map(str, output)), file=outF)


def poly_hash(s, p=1000000007, x=263):
    hash_ans = 0
    for i in range(len(s) - 1, -1, -1):
        hash_ans = (hash_ans * x + ord(s[i])) % p
    return hash_ans


def precompute_hashes(text, len_patt, p=1000000007, x=263):
    n = len(text)
    H = [0] * (n - len_patt + 1)
    S = text[n - len_patt:]
    H[n - len_patt] = poly_hash(S)
    y = 1
    for i in range(1, len_patt + 1):
        y = (y * x) % p
    for i in range(n - len_patt - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + len_patt])) % p
    return H


def rabin_karp(pattern, text):
    positions = []
    p_hash = poly_hash(pattern)
    len_patt = len(pattern)
    H = precompute_hashes(text, len_patt)
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != H[i]:
            continue
        if text[i:i + len_patt] == pattern:
            positions.append(i)
    return positions


if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))

# inF.close()
# outF.close()