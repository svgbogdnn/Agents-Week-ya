import csv
import os
import re


USER_ID_LIST = re.compile(r"user_id\s*\[([^\]]*)\]", re.IGNORECASE)
USER_ID_SINGLE = re.compile(r"user_id\s*(\d+)", re.IGNORECASE)
DIGITS = re.compile(r"\d+")


def extract_user_ids(info: str) -> list[str]:
    if not info:
        return []

    match = USER_ID_LIST.search(info)
    if match:
        return DIGITS.findall(match.group(1))

    match = USER_ID_SINGLE.search(info)
    if match:
        return [match.group(1)]

    return []


def count_whitelisted_users_2025(path: str) -> int:
    users = set()

    with open(path, "r", encoding="utf-8", newline="") as file_obj:
        reader = csv.DictReader(file_obj, delimiter=";")
        for row in reader:
            if row.get("type") != "whitelist":
                continue
            if not row.get("created_dttm", "").startswith("2025-"):
                continue

            users.update(extract_user_ids(row.get("info", "")))

    return len(users)


def solve() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "user_actions.csv")
    answer = count_whitelisted_users_2025(data_path)
    print(answer)


if __name__ == "__main__":
    solve()
