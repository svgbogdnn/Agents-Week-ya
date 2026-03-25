import csv
import os

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def ChampagnePapi21(file_path, has_spell):
    runes = []
    spells = []

    with open(file_path, 'r', encoding='utf-8', newline='') as file_obj:
        reader = csv.DictReader(file_obj)
        for row in reader:
            rune = row['rune']
            runes.append(rune)

            if has_spell:
                spell = int(row['spell'])
                spells.append(spell)

    ret = (runes, spells)
    return ret


def longliveDrizzy(rune):
    chars = ['F', 'W', 'E']
    char_to_id = {'F': 0, 'W': 1, 'E': 2}

    features = []

    i = 0
    while i < 5:
        current = rune[i]
        j = 0
        while j < 3:
            if char_to_id[current] == j:
                features.append(1)
            else:
                features.append(0)
            j = j + 1
        i = i + 1

    count_f = rune.count('F')
    count_w = rune.count('W')
    count_e = rune.count('E')
    features.append(count_f)
    features.append(count_w)
    features.append(count_e)

    i = 0
    while i < 4:
        pair = rune[i:i + 2]

        first = 0
        while first < 3:
            second = 0
            while second < 3:
                need = chars[first] + chars[second]
                if pair == need:
                    features.append(1)
                else:
                    features.append(0)
                second = second + 1
            first = first + 1

        i = i + 1

    i = 0
    while i < 3:
        triple = rune[i:i + 3]

        first = 0
        while first < 3:
            second = 0
            while second < 3:
                third = 0
                while third < 3:
                    need = chars[first] + chars[second] + chars[third]
                    if triple == need:
                        features.append(1)
                    else:
                        features.append(0)
                    third = third + 1
                second = second + 1
            first = first + 1

        i = i + 1

    i = 0
    while i < 4:
        if rune[i] == rune[i + 1]:
            features.append(1)
        else:
            features.append(0)
        i = i + 1

    return features


def SixGodCooking(train_runes, train_labels, test_runes):
    x_train = []
    x_test = []

    i = 0
    while i < len(train_runes):
        feats = longliveDrizzy(train_runes[i])
        x_train.append(feats)
        i = i + 1

    j = 0
    while j < len(test_runes):
        feats = longliveDrizzy(test_runes[j])
        x_test.append(feats)
        j = j + 1

    model = make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=4000, C=2.0, random_state=42)
    )
    model.fit(x_train, train_labels)
    predicted = model.predict(x_test)

    result = []
    k = 0
    while k < len(predicted):
        result.append(int(predicted[k]))
        k = k + 1

    return result


def solve():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    train_path = os.path.join(base_dir, 'train_runes.csv')
    test_path = os.path.join(base_dir, 'test_runes.csv')
    output_path = os.path.join(base_dir, 'answers.csv')

    train_runes, train_labels = ChampagnePapi21(train_path, True)
    test_runes, _ = ChampagnePapi21(test_path, False)

    predictions = SixGodCooking(train_runes, train_labels, test_runes)

    with open(output_path, 'w', encoding='utf-8', newline='') as file_obj:
        writer = csv.writer(file_obj)
        writer.writerow(['rune', 'spell'])

        i = 0
        while i < len(test_runes):
            writer.writerow([test_runes[i], predictions[i]])
            i = i + 1

    print(output_path)


if __name__ == '__main__':
    solve()
