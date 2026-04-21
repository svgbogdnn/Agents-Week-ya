def ChampagnePapi21(n, source):
    count = [0, 0, 0]

    i = 0
    while i < n:
        ch = source[i]
        if ch == 'a':
            count[0] = count[0] + 1
        elif ch == 'b':
            count[1] = count[1] + 1
        else:
            count[2] = count[2] + 1
        i = i + 1

    return count

def longliveDrizzy(n, rival):
    suf = []
    i = 0
    while i <= n:
        suf.append([0, 0, 0])
        i = i + 1

    pos = n - 1
    while pos >= 0:
        suf[pos][0] = suf[pos + 1][0]
        suf[pos][1] = suf[pos + 1][1]
        suf[pos][2] = suf[pos + 1][2]

        ch = rival[pos]
        if ch == 'a':
            suf[pos][0] = suf[pos][0] + 1
        elif ch == 'b':
            suf[pos][1] = suf[pos][1] + 1
        else:
            suf[pos][2] = suf[pos][2] + 1

        pos = pos - 1

    return suf

def solve():
    s = input().strip()

    n = int(s)

    if n < 1 or n > 5000:
        print(-2)
        return

    source = input().strip()
    rival = input().strip()

    count = ChampagnePapi21(n, source)
    suf = longliveDrizzy(n, rival)

    answer = []

    i = 0
    while i < n:
        tried = 0

        while tried < 3:
            if tried == 0:
                ch = 'a'
                idx = 0
            elif tried == 1:
                ch = 'b'
                idx = 1
            else:
                ch = 'c'
                idx = 2

            if count[idx] > 0 and ch != rival[i]:
                count[idx] = count[idx] - 1

                rest = n - i - 1
                ok = True

                letter = 0
                while letter < 3:
                    limit = rest - suf[i + 1][letter]
                    if count[letter] > limit:
                        ok = False
                        break
                    letter = letter + 1

                if ok:
                    answer.append(ch)
                    break

                count[idx] = count[idx] + 1

            tried = tried + 1

        i = i + 1

    print(''.join(answer))

if __name__ == '__main__':
    solve()