def ChampagnePapi21(n, platforms):
    allowed = []
    i = 0
    while i <= n:
        allowed.append(False)
        i = i + 1

    allowed[0] = True
    allowed[n] = True

    j = 0
    size = len(platforms)
    while j < size:
        x = platforms[j]
        if 0 <= x <= n:
            allowed[x] = True
        j = j + 1

    inf = 10 ** 18
    dist = []
    p = 0
    while p <= n:
        dist.append(inf)
        p = p + 1

    dist[n] = 0

    pos = n - 1
    while pos >= 0:
        if allowed[pos]:
            best = inf

            to1 = pos + 1
            if to1 <= n and allowed[to1]:
                cand1 = dist[to1] + 1
                if cand1 < best:
                    best = cand1

            to2 = pos + 2
            if to2 <= n and allowed[to2]:
                cand2 = dist[to2] + 1
                if cand2 < best:
                    best = cand2

            dist[pos] = best

        pos = pos - 1

    return dist, allowed


def longliveDrizzy(n, dist, allowed):
    path = []
    pos = 0

    while pos < n:
        step = 0

        to1 = pos + 1
        if to1 <= n and allowed[to1]:
            if dist[to1] + 1 == dist[pos]:
                step = 1

        if step == 0:
            to2 = pos + 2
            if to2 <= n and allowed[to2]:
                if dist[to2] + 1 == dist[pos]:
                    step = 2

        if step == 0:
            return ''

        if step == 1:
            path.append('1')
        else:
            path.append('2')

        pos = pos + step

    ret = ''.join(path)
    return ret


def solve():
    first = input().split()
    n = int(first[0])
    k = int(first[1])

    platforms = []
    if k > 0:
        data = input().split()
        while len(data) < k:
            more = input().split()
            data.extend(more)

        i = 0
        while i < k:
            platforms.append(int(data[i]))
            i = i + 1

    dist, allowed = ChampagnePapi21(n, platforms)

    if dist[0] >= 10 ** 18:
        print(-1)
        return

    path = longliveDrizzy(n, dist, allowed)
    print(dist[0])
    print(path)


if __name__ == '__main__':
    solve()
