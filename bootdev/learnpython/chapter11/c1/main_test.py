from main import *

run_cases = [
    (
        ["basketball", "football", "soccer", "baseball", "basketball"],
        {"basketball", "football", "soccer", "baseball"},
    ),
    (
        [
            "Age of Empires",
            "World of Warcraft",
            "Halo",
            "Call of Duty",
            "Age of Empires",
            "Magic the Gathering",
            "Halo",
        ],
        {
            "Age of Empires",
            "World of Warcraft",
            "Halo",
            "Call of Duty",
            "Magic the Gathering",
        },
    ),
]

submit_cases = run_cases + [
    (
        [
            "Lane",
            "Allan",
            "James",
            "Tiffany",
            "John",
            "Cameron",
            "Lane",
            "Allan",
            "James",
            "Tiffany",
            "John",
            "Cameron",
            "Chad",
            "Tj",
            "Tim",
            "Gertrude",
            "Stephanie",
        ],
        {
            "Lane",
            "Allan",
            "James",
            "Tiffany",
            "John",
            "Cameron",
            "Chad",
            "Tj",
            "Tim",
            "Gertrude",
            "Stephanie",
        },
    ),
    ([], set()),
    (["apple", "apple", "apple", "apple", "apple"], {"apple"}),
    (["a", "b", "c", "c", "b", "a"], {"a", "b", "c"}),
    (["123", "456", "789", "123", "456", "789"], {"123", "456", "789"}),
    (
        [
            "python",
            "java",
            "c++",
            "ruby",
            "python",
            "java",
            "c++",
            "ruby",
            "python",
            "java",
            "c++",
            "ruby",
            "python",
            "java",
            "c++",
            "ruby",
        ],
        {"python", "java", "c++", "ruby"},
    ),
]


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input list: {input}")
    print(f"Expected set: {expected_output}")
    result = remove_duplicates(input)
    print(f"Actual set: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()

