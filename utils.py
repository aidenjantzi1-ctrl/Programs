from tabulate import tabulate
import os

def clr_terminal(): os.system('cls')

def test(test_cases: dict, func_name):
    clr_terminal()

    rows = []

    for key, expected in test_cases.items():
        actual = func_name(key)

        rows.append([
            key,
            expected,
            actual,
            "Pass" if actual == expected else "Fail"
        ])

    print(tabulate(
        rows,
        headers=["Input", "Expected", "Actual", "Result"],
        tablefmt="grid"
    ))
