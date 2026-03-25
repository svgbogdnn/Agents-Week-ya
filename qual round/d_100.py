from collections import deque


def ChampagnePapi21(items, n):
    buckets = []
    i = 0
    while i < n:
        buckets.append(deque())
        i = i + 1

    covered = 0
    sum_min = 0
    left = 0

    best_width = -1
    best_sum = -1
    best_left = 0
    best_right = 0

    right = 0
    total = len(items)
    while right < total:
        value = items[right][0]
        color = items[right][1]

        bucket = buckets[color]
        if len(bucket) == 0:
            bucket.append(value)
            covered = covered + 1
            sum_min = sum_min + value
        else:
            bucket.append(value)

        while covered == n and left <= right:
            current_width = items[right][0] - items[left][0]
            current_sum = sum_min

            need_update = False
            if best_width == -1 or current_width < best_width:
                need_update = True
            elif current_width == best_width and current_sum < best_sum:
                need_update = True

            if need_update:
                best_width = current_width
                best_sum = current_sum
                best_left = left
                best_right = right

            left_color = items[left][1]
            left_bucket = buckets[left_color]

            old_min = left_bucket[0]
            left_bucket.popleft()

            if len(left_bucket) == 0:
                covered = covered - 1
                sum_min = sum_min - old_min
            else:
                new_min = left_bucket[0]
                sum_min = sum_min - old_min
                sum_min = sum_min + new_min

            left = left + 1

        right = right + 1

    ret = (best_left, best_right)
    return ret


def longliveDrizzy(items, n, best_left, best_right):
    chosen = []
    i = 0
    while i < n:
        chosen.append(-1)
        i = i + 1

    have = 0
    j = best_left
    while j <= best_right:
        value = items[j][0]
        color = items[j][1]

        if chosen[color] == -1:
            chosen[color] = value
            have = have + 1
            if have == n:
                break

        j = j + 1

    return chosen


def SixGodCooking(chosen):
    chosen.sort()

    parts = []
    i = 0
    size = len(chosen)
    while i < size:
        parts.append(str(chosen[i]))
        i = i + 1

    ret = ' '.join(parts)
    return ret


def solve():
    first = input().split()
    n = int(first[0])
    m = int(first[1])

    items = []
    color = 0
    while color < n:
        row = input().split()
        while len(row) < m:
            extra = input().split()
            row.extend(extra)

        idx = 0
        while idx < m:
            value = int(row[idx])
            items.append((value, color))
            idx = idx + 1

        color = color + 1

    items.sort()

    best_left, best_right = ChampagnePapi21(items, n)
    chosen = longliveDrizzy(items, n, best_left, best_right)
    answer = SixGodCooking(chosen)
    print(answer)


if __name__ == '__main__':
    solve()
