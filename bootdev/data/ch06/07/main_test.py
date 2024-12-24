from main import *
from user import *
#from ref import *

run_cases = [
    (4),
    (13),
    (15),
    (5),
    (6)
]

submit_cases = run_cases + [
    (10),
]


def test(num_users):
    users = get_users(num_users)
    tree = RBTree()
    reference_tree = RBTree()
    for user in users:
        tree.insert(user)
        print(f"Inserting {str(user)}")
        print("-------------------------------------")
        print(print_tree(tree))
        print("-------------------------------------\n")
#        ref_impl_ins(reference_tree, user)
    print("=====================================")
#    print("Expecting:")
#    print("-------------------------------------")
#    print(print_tree(reference_tree))
#    print("-------------------------------------\n")
    print("Actual:")
    print("-------------------------------------")
    print(print_tree(tree))
    print("-------------------------------------\n")

    #if print_tree(tree) == print_tree(reference_tree):
    #    print("Pass \n")
    #    return True
    #print("Fail \n")
    return False


def print_tree(node):
    lines = []
    format_tree_string(node.root, lines)
    return "\n".join(lines)


def format_tree_string(node, lines, level=0):
    if node.val is not None:
        format_tree_string(node.right, lines, level + 1)
        lines.append(
            " " * 4 * level
            + "> "
            + str(node.val)
            + " "
            + ("[red]" if node.red else "[black]")
        )
        format_tree_string(node.left, lines, level + 1)


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(test_case)
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

