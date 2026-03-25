def ChampagnePapi21(values, freq):
    values.sort()
    freq.sort()

    total = 0
    i = 0
    size = len(values)
    while i < size:
        total = total + values[i] * freq[i]
        i = i + 1

    return total


def longliveDrizzy(n, q):
    diff = []
    i = 0
    while i < n + 1:
        diff.append(0)
        i = i + 1

    j = 0
    while j < q:
        line = input().split()
        l = int(line[0])
        r = int(line[1])

        diff[l - 1] = diff[l - 1] + 1
        if r < n:
            diff[r] = diff[r] - 1

        j = j + 1

    freq = []
    cur = 0
    k = 0
    while k < n:
        cur = cur + diff[k]
        freq.append(cur)
        k = k + 1

    return freq


def solve():
    first = input().split()
    n = int(first[0])
    q = int(first[1])

    data = input().split()
    values = []
    i = 0
    while i < n:
        values.append(int(data[i]))
        i = i + 1

    freq = longliveDrizzy(n, q)
    answer = ChampagnePapi21(values, freq)
    print(answer)


if __name__ == '__main__':
    solve()
