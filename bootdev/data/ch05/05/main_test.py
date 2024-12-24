import random
from main import *
from user import *
#from ref import *

run_cases = [
    (3),
    (5),
]

submit_cases = run_cases + [
    (10),
]

def ref_inorder(node, acc):
    if node is not None:
        ref_inorder(node.left, acc)
        acc.append(node.val)
        ref_inorder(node.right, acc)
    return acc

def ref_implementation(bst_node, user):
    if bst_node is None:
        return BSTNode(user)
    if user < bst_node.val:
        if bst_node.left is None:
            bst_node.left = BSTNode(user)
        else:
            ref_implementation(bst_node.left, user)
    else:
        if bst_node.right is None:
            bst_node.right = BSTNode(user)
        else:
            ref_implementation(bst_node.right, user)
    return bst_node

def test(num_users):
    users = get_users(num_users)
    expected_bst = BSTNode()
    for user in users:
        ref_implementation(expected_bst, user)
    print("=====================================")
    print("Expecting Tree:")
    print("-------------------------------------")
    print_tree(expected_bst)
    print("-------------------------------------\n")
    actual_bst = BSTNode()
    for user in users:
        print(f"Inserting {user} into tree...")
        actual_bst.insert(user)
    print("\n")
    print("Actual Tree:")
    print("-------------------------------------")
    print_tree(actual_bst)
    print("-------------------------------------")
    if ref_inorder(actual_bst, []) == ref_inorder(expected_bst, []):
        print("Pass \n")
        return True
    print("Fail \n")
    return False


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


def print_tree(bst_node):
    lines = []
    format_tree_string(bst_node, lines)
    print("\n".join(lines))


def format_tree_string(bst_node, lines, level=0):
    if bst_node is not None:
        format_tree_string(bst_node.right, lines, level + 1)
        lines.append(" " * 4 * level + "> " + str(bst_node.val))
        format_tree_string(bst_node.left, lines, level + 1)


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
