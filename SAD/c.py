from fractions import Fraction

def ChampagnePapi21(v, children):
    subs = []

    i = 0
    size = len(children[v])
    while i < size:
        to = children[v][i]
        subs.append(ChampagnePapi21(to, children))
        i = i + 1

    subs.sort()
    ret = tuple(subs)
    return ret

def longliveDrizzy(node):
    result = []

    def dfs(cur, path, prob):
        k = len(cur)
        step = prob / Fraction(k + 1, 1)

        result.append((path, step))

        i = 0
        while i < k:
            child = cur[i]
            next_path = path + (i,)
            dfs(child, next_path, step)
            i = i + 1

    dfs(node, tuple(), Fraction(1, 1))
    return result

def SixGodCooking(node, path):
    if len(path) == 0:
        children = []

        i = 0
        size = len(node)
        while i < size:
            children.append(node[i])
            i = i + 1

        children.append(tuple())
        children.sort()

        ret = tuple(children)
        return ret

    idx = path[0]
    children = []

    i = 0
    size = len(node)
    while i < size:
        child = node[i]
        if i == idx:
            child = SixGodCooking(child, path[1:])
        children.append(child)
        i = i + 1

    children.sort()
    ret = tuple(children)
    return ret

def qliphotProbabilities(n):
    start = (tuple(),)

    states = {}
    states[start] = Fraction(1, 1)

    age = 1
    while age < n:
        next_states = {}

        for shape, prob in states.items():
            moves = longliveDrizzy(shape)

            j = 0
            while j < len(moves):
                path = moves[j][0]
                p_move = moves[j][1]

                new_shape = SixGodCooking(shape, path)
                add = prob * p_move

                if new_shape in next_states:
                    next_states[new_shape] = next_states[new_shape] + add
                else:
                    next_states[new_shape] = add

                j = j + 1

        states = next_states
        age = age + 1

    return states

def fractionToString(value):
    num = value.numerator
    den = value.denominator

    whole = num // den
    rem = num % den

    if rem == 0:
        ret = str(whole) + '.0'
        return ret

    digits = []
    limit = 30
    cnt = 0

    while rem != 0 and cnt < limit:
        rem = rem * 10
        digit = rem // den
        rem = rem % den
        digits.append(str(digit))
        cnt = cnt + 1

    ret = str(whole) + '.' + ''.join(digits)
    return ret

def solve():
    s = input().strip()
    n = int(s)

    children = []
    i = 0
    while i <= n:
        children.append([])
        i = i + 1

    need = 2 * n
    tokens = []

    while len(tokens) < need:
        try:
            line = input().split()
        except EOFError:
            break

        j = 0
        while j < len(line):
            tokens.append(int(line[j]))
            j = j + 1

    e = 0
    pos = 0
    while e < n and pos + 1 < len(tokens):
        a = tokens[pos]
        b = tokens[pos + 1]
        children[a].append(b)

        pos = pos + 2
        e = e + 1

    target = ChampagnePapi21(0, children)

    probs = qliphotProbabilities(n)
    if target in probs:
        ans = probs[target]
    else:
        ans = Fraction(0, 1)

    out = fractionToString(ans)
    print(out)

if __name__ == '__main__':
    solve()