def ChampagnePapi21(n):
    week_minutes = 10080

    if n % 2 == 0:
        return -1

    if n == 1:
        return 0

    distance = (n - 1) // 2
    upper_bound = week_minutes / (2.0 * distance * distance)

    if upper_bound < 0.95:
        return -1

    meet_probability = longliveDrizzy(n, week_minutes)

    if meet_probability < 0.95:
        return -1

    expectation = n * n - 1
    return expectation

def longliveDrizzy(n, week_minutes):
    if n == 1:
        return 1.0

    probability = [0.0] * n
    start_state = 1 % n
    probability[start_state] = 1.0

    minute = 0
    while minute < week_minutes:
        next_probability = [0.0] * n

        state = 1
        while state < n:
            current_value = probability[state]

            if current_value != 0.0:
                stay_value = current_value * 0.5
                next_probability[state] = next_probability[state] + stay_value

                right_state = state + 2
                if right_state >= n:
                    right_state = right_state - n

                if right_state != 0:
                    move_right_value = current_value * 0.25
                    next_probability[right_state] = (
                        next_probability[right_state] + move_right_value
                    )

                left_state = state - 2
                if left_state < 0:
                    left_state = left_state + n

                if left_state != 0:
                    move_left_value = current_value * 0.25
                    next_probability[left_state] = (
                        next_probability[left_state] + move_left_value
                    )

            state = state + 1

        probability = next_probability
        minute = minute + 1

    survive_probability = 0.0
    state = 1
    while state < n:
        survive_probability = survive_probability + probability[state]
        state = state + 1

    meet_probability = 1.0 - survive_probability
    return meet_probability

def solve():
    s = input().strip()
    n = int(s)
    answer = ChampagnePapi21(n)
    print(answer)

if __name__ == '__main__':
    solve()