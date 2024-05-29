# без хешування, але проходить всі тести
def mismatch_count(t, p, res, k):
    if res[0] > k or t == p or len(t) < 2:
        return t, p

    mid = len(t) // 2
    left_t, left_p = mismatch_count(t[:mid], p[:mid], res, k)
    right_t, right_p = mismatch_count(t[mid:], p[mid:], res, k)
    if len(left_t) == 1 and left_t != left_p:
        res[0] += 1
    if len(right_t) == 1 and right_t != right_p:
        res[0] += 1

    return left_t + right_t, left_p + right_p


def find_approximate_matches(t, p, k):
    m, n = len(t), len(p)
    if m < n:
        return []

    result = []
    for i in range(m - n + 1):
        count_mis = [0,]
        slice_t = t[i:i + n]
        mismatch_count(slice_t, p, count_mis, k)
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
    #filein = open("cours_input.txt", "r")
    #fileout = open("my_output-2.txt", "w")
    #input_lines = filein.read().strip().split('\n')
    results = process_input(input_lines)
    for result in results:
        print(result)
        #print(result, file=fileout)

    #filein.close()
    #fileout.close()