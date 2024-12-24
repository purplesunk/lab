from main import *
from user import *
import random

run_cases = [
    (
        4,
        [User(0), User(7), User(8), User(11)],
    ),
    (
        6,
        [User(0), User(5), User(9), User(10), User(16), User(17)],
    ),
]

submit_cases = run_cases + [
    (
        12,
        [
            User(2),
            User(10),
            User(11),
            User(17),
            User(18),
            User(19),
            User(22),
            User(23),
            User(27),
            User(30),
            User(33),
            User(34),
        ],
    ),
]


def test(num_characters, expected):
    characters = get_users(
        num_characters
    )  # Ensure this reflects your project structure
    bst = BSTNode()
    for character in characters:
        bst.insert(character)
    print("=====================================")
    print("Tree:")
    print("-------------------------------------")
    print(print_tree(bst))
    print("-------------------------------------\n")
    print(f"Expecting: {expected}")
    try:
        actual = bst.inorder([])
        print(f"Actual: {actual}")
        if expected == actual:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
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


def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    return "\n".join(lines)


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
