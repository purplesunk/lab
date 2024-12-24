from main import *

run_cases = [
    (["developer", "marketer", "designer"], 1),
    (["marketer", "marketer", "developer", "marketer"], 3),
]

submit_cases = run_cases + [
    ([], 0),
    (["developer", "designer", "product manager"], 0),
    (["marketer"], 1),
    (["MARKETER", "Marketer", "marketer"], 1),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input job titles: {input1}")
    print(f"Expecting: {expected_output}")
    result = count_marketers(input1)
    print(f"Actual: {result}")
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
