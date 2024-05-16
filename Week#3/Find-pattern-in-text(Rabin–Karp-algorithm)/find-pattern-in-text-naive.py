# python3
inF = open("06", "r")
outF = open("06.a", "w")

def read_input():
    # return (input().rstrip(), input().rstrip())
    return (inF.readline().rstrip(), inF.readline().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)), file=outF)

def get_occurrences(pattern, text):
    return [
        i
        for i in range(len(text) - len(pattern) + 1)
        if text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

inF.close()
outF.close()