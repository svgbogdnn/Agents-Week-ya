import csv
import itertools
import os


def ChampagnePapi21(path):
    rows = []

    with open(path, 'r', encoding='utf-8', newline='') as file_obj:
        rd = csv.DictReader(file_obj)
        for row in rd:
            rows.append(row)

    return rows


def longliveDrizzy(rows):
    fixed = {'n': '0', 'i': '1', 'x': '2', 'y': '3'}
    letters = ['b', 'd', 'f', 'h', 'o', 's']
    digits = ['4', '5', '6', '7', '8', '9']

    best_map = {}

    def decode_number(token, mapping):
        out = ''
        i = 0
        while i < len(token):
            out = out + mapping[token[i]]
            i = i + 1
        return int(out)

    for perm in itertools.permutations(digits):
        mapping = {}

        for key in fixed:
            mapping[key] = fixed[key]

        i = 0
        while i < len(letters):
            mapping[letters[i]] = perm[i]
            i = i + 1

        ok = True

        j = 0
        while j < len(rows):
            need = decode_number(rows[j]['col_5'], mapping)
            got = decode_number(rows[j]['col_6'], mapping)

            accepted = rows[j]['col_2'] == 'i'
            rule = abs(got - need) <= 5

            if accepted != rule:
                ok = False
                break

            j = j + 1

        if ok:
            best_map = mapping
            break

    return best_map


def SixGodCooking(mapping, rows):
    def decode_number(token):
        out = ''
        i = 0
        while i < len(token):
            out = out + mapping[token[i]]
            i = i + 1
        return out

    date_day = decode_number('ix')
    date_month = decode_number('ns')
    date_year = decode_number('xnxf')

    number = decode_number('ho')

    year_value = int(date_year)

    colors = {}
    i = 0
    while i < len(rows):
        row = rows[i]
        cur_year = int(decode_number(row['col_3']))
        if cur_year == year_value and row['col_2'] == 'i':
            token = row['col_7']
            if token in colors:
                colors[token] = colors[token] + 1
            else:
                colors[token] = 1
        i = i + 1

    purple_token = ''
    purple_cnt = -1
    for token in colors:
        if colors[token] > purple_cnt:
            purple_cnt = colors[token]
            purple_token = token

    color_tokens = set()
    i = 0
    while i < len(rows):
        color_tokens.add(rows[i]['col_7'])
        i = i + 1

    color_map = {}

    violet = '\u0444\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439'
    yellow = '\u0436\u0435\u043b\u0442\u044b\u0439'
    blue = '\u0441\u0438\u043d\u0438\u0439'

    for token in color_tokens:
        ln = len(token)
        if ln == 10:
            color_map[token] = violet
        elif ln == 6:
            color_map[token] = yellow
        elif ln == 5:
            color_map[token] = blue

    if purple_token in color_map:
        color_map[purple_token] = violet

    color = color_map['lamegc']

    date = date_day + '.' + date_month + '.' + date_year
    ret = (date, number, color)
    return ret


def solve():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data.csv')

    rows = ChampagnePapi21(data_path)
    mapping = longliveDrizzy(rows)
    date, number, color = SixGodCooking(mapping, rows)

    print(date)
    print(number)
    print(color)


if __name__ == '__main__':
    solve()
