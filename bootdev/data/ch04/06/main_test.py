from main import *

run_cases = [
    (["Major Marquis Warren", "John Ruth"], ["John Ruth", "Major Marquis Warren"]),
    (
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue"],
        ["Daisy Domergue", "John Ruth", "Major Marquis Warren"],
    ),
]

submit_cases = run_cases + [
    (
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],
        ["Chris Mannix", "Daisy Domergue", "John Ruth", "Major Marquis Warren"],
    ),
    (
        ["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix", "Bob"],
        ["Bob", "Chris Mannix", "Daisy Domergue", "John Ruth", "Major Marquis Warren"],
    ),
    (
        [
            "Major Marquis Warren",
            "John Ruth",
            "Daisy Domergue",
            "Chris Mannix",
            "Bob",
            "Oswaldo Mobray",
        ],
        [
            "Oswaldo Mobray",
            "Bob",
            "Chris Mannix",
            "Daisy Domergue",
            "John Ruth",
            "Major Marquis Warren",
        ],
    ),
]


def test(inputs, expected_state):
    print("---------------------------------")
    linked_list = LinkedList()
    for val in inputs:
        linked_list.add_to_head(Node(val))
    result = linked_list_to_list(linked_list)

    print(f"Input:  {inputs}")
    print(f"Expect: {expected_state}")
    print(f"Actual: {result}")

    if result == expected_state:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def linked_list_to_list(linked_list):
    return [node.val for node in linked_list]


def main(test_cases):
    passed = 0
    failed = 0

    for inputs, expected_state in test_cases:
        if test(inputs, expected_state):
            passed += 1
        else:
            failed += 1

    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


if "__RUN__" in globals():
    main(run_cases)
else:
    main(submit_cases)
