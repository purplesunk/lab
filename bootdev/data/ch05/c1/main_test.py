from main import BSTNode
from user import User


def build_tree_from_users(users):
    if not users:
        return None
    bst = BSTNode(users[0])
    for user in users[1:]:
        bst.insert(user)
    return bst


run_cases = [
    ([User(1), User(10), User(5)], 0, 10, [User(1), User(5), User(10)]),
    ([User(6), User(2), User(3)], 0, 6, [User(2), User(3), User(6)]),
]

submit_cases = run_cases + [
    ([], 0, 0, []),
    ([User(1), User(2), User(3), User(4)], 0, 3, [User(1), User(2), User(3)]),
    ([User(10), User(15), User(20)], 10, 15, [User(10), User(15)]),
]


def test(input_users, lower_id, upper_id, expected_output):
    print("---------------------------------")
    root = build_tree_from_users(input_users)
    print(f"lower_bound: User({lower_id}), upper_bound: User({upper_id})")
    lower_user = User(lower_id)
    upper_user = User(upper_id)
    expected_user_objects = [User(user.id) for user in expected_output]
    result = root.search_range(lower_user, upper_user) if root else []
    print("Expected Users:", [str(user) for user in expected_user_objects])
    print("Actual Users:", [str(user) for user in result])
    if result == expected_user_objects:
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
