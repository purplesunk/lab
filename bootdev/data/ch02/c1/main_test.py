from main import DebounceStack

run_cases = [
    (
        ["add_connection", "add_connection", "remove_connection"],
        ["add_connection", "remove_connection"],
    ),
    (
        ["like_post", "like_post", "unlike_post", "unlike_post", "like_post"],
        ["like_post", "unlike_post", "like_post"],
    ),
]

submit_cases = run_cases + [
    (
        [
            "send_message",
            "send_message",
            "edit_profile",
            "edit_profile",
            "send_message",
        ],
        ["send_message", "edit_profile", "send_message"],
    ),
    ([], []),
    (
        ["add_friend", "add_friend", "add_friend"],
        ["add_friend"],
    ),
]


def test(actions, expected_stack):
    print("---------------------------------")
    print(f"Actions: {actions}")
    print(f"Expected stack: {expected_stack}")

    stack = DebounceStack()
    for action in actions:
        stack.push(action)

    result = []
    while stack.size() != 0:
        result.insert(0, stack.pop())

    print(f"Actual stack: {result}")
    if result == expected_stack:
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
