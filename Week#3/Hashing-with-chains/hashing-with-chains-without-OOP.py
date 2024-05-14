# python3

inF = open('input.txt', 'r')

def hash_func(word, bucket_count, _multiplier=263, _prime=1000000007):
    ans = 0
    for c in reversed(word):
        ans = (ans * _multiplier + ord(c)) % _prime
    return ans % bucket_count


def write_search_result(was_found):
    print('yes' if was_found else 'no')


def write_chain(chain):
    print(' '.join(chain))


def process_query(query, elems):
    if query[0] == "check":
        # use reverse order, because we append strings to the end
        key = int(query[1])
        if key in elems:
            write_chain(reversed(elems[key]))
        else:
            write_chain("")
    else:
        ind = hash_func(query[1], bucket_count)
        if query[0] == 'find':
            write_search_result(ind in elems and query[1] in elems[ind])
        elif query[0] == 'add':
            elems[ind] = elems.get(ind, [])
            if query[1] not in elems[ind]:
                elems[ind].append(query[1])
        else:
            if ind in elems and query[1] in elems[ind]:
                elems[ind].remove(query[1])
                if len(elems[ind]) == 0:
                    del elems[ind]



# bucket_count = int(input())
bucket_count = int(inF.readline())
# n = int(input())
n = int(inF.readline())
elems = {}
for i in range(n):
    query = inF.readline().split()
    process_query(query, elems)

inF.close()