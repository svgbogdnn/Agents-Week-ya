import os

import pandas as pd
from scipy.stats import chi2_contingency


def ChampagnePapi21(path):
    data = pd.read_csv(path)
    both_group = data.groupby('user_id')['group'].nunique()
    both_users = set(both_group[both_group > 1].index)
    log_rows = (data['payment'] == 1) & (data['payment_page'] == 0)
    log_users = set(data[log_rows]['user_id'])
    bad_users = both_users | log_users
    clean = data[~data['user_id'].isin(bad_users)].copy()
    return clean


def SixGodCooking(clean):
    table = pd.crosstab(clean['group'], clean['district'])
    stat, p_value, dof, expected = chi2_contingency(table)
    return stat, p_value


def solve():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'ab_test.csv')

    clean_data = ChampagnePapi21(data_path)
    stat, p_value = SixGodCooking(clean_data)

    print(str(stat) + ' ' + str(p_value))


if __name__ == '__main__':
    solve()
