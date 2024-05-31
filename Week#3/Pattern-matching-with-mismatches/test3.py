def mismatch_count(t, p, res, k):
    if len(t) == 1 and t != p:
        res[0] += 1
    if res[0] > k or t == p or len(t) < 2:
        return

    mid = len(t) // 2
    mismatch_count(t[:mid], p[:mid], res, k)
    mismatch_count(t[mid:], p[mid:], res, k)

    return


text =    "caba8abaata"
pattern = "daab7abaaya"
k = 2
res = [0,]
mismatch_count(text, pattern, res, k)
print(res)