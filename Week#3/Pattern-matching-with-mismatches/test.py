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

    return t, p


text =    "abaabaaa"
pattern = "aababaaa"
k = 2
res = [0,]
mismatch_count(text, pattern, res, k)
print(res)