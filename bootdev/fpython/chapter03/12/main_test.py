from main import *

run_cases = [
    (
        "My hovercraft is full of eels",
        {
            "My hovercraft is full of eels": 6,
            "He's a lumberjack and he's okay. He sleeps all night and he works all day": 15,
        },
        (
            6,
            {
                "My hovercraft is full of eels": 6,
                "He's a lumberjack and he's okay. He sleeps all night and he works all day": 15,
            },
        ),
    ),
    (
        "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, and spam",
        {},
        (
            12,
            {
                "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, and spam": 12
            },
        ),
    ),
]

submit_cases = run_cases + [
    (
        "This is an ex-parrot",
        {"This parrot is no more": 5},
        (4, {"This parrot is no more": 5, "This is an ex-parrot": 4}),
    ),
    (
        "This doc should 'incorrectly' have 9999 words to test that the memoization is working",
        {
            "My hovercraft is full of eels": 6,
            "This doc should 'incorrectly' have 9999 words to test that the memoization is working": 9999,
        },
        (
            9999,
            {
                "My hovercraft is full of eels": 6,
                "This doc should 'incorrectly' have 9999 words to test that the memoization is working": 9999,
            },
        ),
    ),
]


def test(memos, input_document, input_memos, expected_output):
    print("---------------------------------")
    print(f"Input document:\n  {input_document}")
    print(f"Input memos:")
    for key, value in input_memos.items():
        print(f"  {key}: {value}")
    print(f"Expected word count: {expected_output[0]}")
    print(f"Expected memos:")
    for key, value in expected_output[1].items():
        print(f"  {key}: {value}")
    result = word_count_memo(input_document, input_memos)
    print(f"Actual word count: {result[0]}")
    print(f"Actual memos:")
    for key, value in result[1].items():
        print(f"  {key}: {value}")
    if result == expected_output:
        print("Pass")
        return True, memos
    print("Fail")
    return False, memos


def main():
    test_cases = submit_cases
    if "__RUN__" in globals():
        test_cases = run_cases
    passed = 0
    failed = 0
    memos = {
        "This doc should 'incorrectly' have 9999 words to test that the memoization is working!": 9999
    }
    correct, memos_copy = test(memos, *test_cases[0])
    if correct:
        passed += 1
    else:
        failed += 1
    for test_case in test_cases[1:]:
        correct, memos_copy = test(memos_copy, *test_case)
        if correct:
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


main()
