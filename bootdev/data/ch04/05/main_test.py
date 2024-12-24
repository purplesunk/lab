from main import *

run_cases = [
    (["Major Marquis Warren", "John Ruth"],),
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue"],),
]

submit_cases = run_cases + [
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix"],),
    (["Major Marquis Warren", "John Ruth", "Daisy Domergue", "Chris Mannix", "Bob"],),
    (
        [
            "Major Marquis Warren",
            "John Ruth",
            "Daisy Domergue",
            "Chris Mannix",
            "Bob",
            "Oswaldo Mobray",
        ],
    ),
]


def test(inputs):
    print("---------------------------------")
    linked_list = LinkedList()
    for val in inputs:
        linked_list.add_to_tail(Node(val))
    actual = linked_list_to_list(linked_list)

    print(f"Expected: {inputs}")
    print(f"Actual  : {actual}")

    if actual == inputs:
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

    for inputs in test_cases:
        if test(inputs[0]):
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
